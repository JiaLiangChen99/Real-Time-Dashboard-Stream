import reflex as rx
from typing import TypedDict
import random
import asyncio
import json


class DataPoint(TypedDict):
    time: int
    value: float


class DashboardState(rx.State):
    data_stream: list[DataPoint] = []
    table_data: list[DataPoint] = []
    is_streaming: bool = False
    current_time_step: int = 0
    active_chart: int = 0
    MAX_CHART_POINTS: int = 50
    MAX_TABLE_ROWS: int = 100
    STREAM_INTERVAL_S: float = 0.5
    chart_line_color: str = "#6366F1"
    default_chart_colors: list[str] = [
        "#6366F1",
        "#EC4899",
        "#10B981",
        "#F59E0B",
        "#EF4444",
    ]

    def _generate_new_data_point(
        self, time_step: int
    ) -> DataPoint:
        if not self.data_stream:
            current_value = 150 + random.uniform(-15, 15)
        else:
            last_value = self.data_stream[-1]["value"]
            change = random.uniform(-8, 8)
            trend_factor = 0.05 * (
                time_step / self.MAX_CHART_POINTS
            )
            current_value = (
                last_value + change + trend_factor
            )
            current_value = max(50, min(250, current_value))
        return {
            "time": time_step,
            "value": round(current_value, 2),
        }

    @rx.event
    def set_chart_line_color(self, color: str):
        self.chart_line_color = color

    @rx.event
    def toggle_chart_type(self, index: int):
        self.active_chart = index

    @rx.event
    def toggle_streaming(self):
        self.is_streaming = not self.is_streaming
        if self.is_streaming:
            self.data_stream = []
            self.table_data = []
            self.current_time_step = 0
            return DashboardState.stream_data

    @rx.event(background=True)
    async def stream_data(self):
        while True:
            time_step_for_this_iteration = 0
            async with self:
                if not self.is_streaming:
                    break
                self.current_time_step += 1
                time_step_for_this_iteration = (
                    self.current_time_step
                )
            new_point = self._generate_new_data_point(
                time_step_for_this_iteration
            )
            async with self:
                if not self.is_streaming:
                    break
                self.data_stream.append(new_point)
                if (
                    len(self.data_stream)
                    > self.MAX_CHART_POINTS
                ):
                    self.data_stream = self.data_stream[
                        -self.MAX_CHART_POINTS :
                    ]
                self.table_data.insert(0, new_point)
                if (
                    len(self.table_data)
                    > self.MAX_TABLE_ROWS
                ):
                    self.table_data = self.table_data[
                        : self.MAX_TABLE_ROWS
                    ]
            yield
            await asyncio.sleep(self.STREAM_INTERVAL_S)
        async with self:
            if self.is_streaming:
                self.is_streaming = False

    @rx.event
    def export_data_csv(self) -> rx.event.EventSpec:
        if not self.table_data:
            return rx.toast(
                "No data to export.", duration=3000
            )
        header = "time,value\n"
        csv_data = header + "\n".join(
            [
                f"{dp['time']},{dp['value']}"
                for dp in self.table_data
            ]
        )
        return rx.download(
            data=csv_data, filename="live_data.csv"
        )

    @rx.event
    def export_data_json(self) -> rx.event.EventSpec:
        if not self.table_data:
            return rx.toast(
                "No data to export.", duration=3000
            )
        json_data = json.dumps(self.table_data, indent=2)
        return rx.download(
            data=json_data, filename="live_data.json"
        )