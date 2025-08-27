import reflex as rx
from app.states.dashboard_state import (
    DashboardState,
    DataPoint,
)


def render_table_row(
    row: DataPoint, index: int
) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            row["time"],
            class_name="px-5 py-3 whitespace-nowrap text-sm text-gray-600 font-medium",
        ),
        rx.el.td(
            f"${row['value']}",
            class_name="px-5 py-3 whitespace-nowrap text-sm text-gray-800 font-semibold",
        ),
        class_name="border-b border-gray-200 hover:bg-gray-50",
    )


def live_data_table():
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Data Log",
                class_name="text-lg font-semibold text-gray-800",
            ),
            rx.icon(
                tag="database",
                class_name="w-5 h-5 text-gray-400",
            ),
            class_name="w-full flex items-center justify-between pb-4 border-b border-gray-200",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Time (s)",
                            class_name="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Value",
                            class_name="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50 sticky top-0 backdrop-blur-sm",
                ),
                rx.el.tbody(
                    rx.foreach(
                        DashboardState.table_data,
                        render_table_row,
                    ),
                    class_name="bg-white",
                ),
                class_name="min-w-full",
            ),
            class_name="overflow-auto h-[480px] rounded-lg",
        ),
        class_name="col-span-1 h-full flex flex-col p-6 bg-white rounded-2xl border border-gray-200 shadow-sm",
    )