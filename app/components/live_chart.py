import reflex as rx
from app.states.dashboard_state import DashboardState
from app.components.chart_tooltip import TOOLTIP_PROPS


def chart_selector(tabs=["area-chart", "line-chart"]):
    return rx.el.div(
        rx.foreach(
            tabs,
            lambda tab, i: rx.el.button(
                rx.icon(
                    tag=tab,
                    class_name=rx.cond(
                        DashboardState.active_chart == i,
                        "w-5 h-5 text-indigo-600",
                        "w-5 h-5 text-gray-500 group-hover:text-gray-700",
                    ),
                ),
                on_click=lambda: DashboardState.toggle_chart_type(
                    i
                ),
                class_name=rx.cond(
                    DashboardState.active_chart == i,
                    "p-2 rounded-lg bg-indigo-100",
                    "p-2 rounded-lg bg-transparent group hover:bg-gray-100",
                ),
            ),
        ),
        class_name="inline-flex items-center p-1 space-x-1 bg-gray-50 border border-gray-200 rounded-xl",
    )


def chart_color_selector() -> rx.Component:

    def color_button(color_hex: str) -> rx.Component:
        return rx.el.button(
            on_click=lambda: DashboardState.set_chart_line_color(
                color_hex
            ),
            class_name=rx.cond(
                DashboardState.chart_line_color
                == color_hex,
                "w-6 h-6 rounded-md border-2 border-white ring-2 ring-indigo-500",
                "w-6 h-6 rounded-md border border-gray-300 hover:opacity-80",
            ),
            style={"backgroundColor": color_hex},
        )

    return rx.el.div(
        rx.foreach(
            DashboardState.default_chart_colors,
            color_button,
        ),
        class_name="flex flex-row space-x-2 items-center",
    )


def get_line_chart():
    return rx.recharts.line_chart(
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3",
            horizontal=True,
            vertical=False,
            class_name="text-gray-300",
        ),
        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
        rx.recharts.x_axis(
            data_key="time",
            type_="number",
            domain=["dataMin", "dataMax"],
            axis_line=False,
            tick_line=False,
        ),
        rx.recharts.y_axis(
            domain=[50, 250],
            axis_line=False,
            tick_line=False,
        ),
        rx.recharts.line(
            data_key="value",
            type_="monotone",
            stroke=DashboardState.chart_line_color,
            stroke_width=2.5,
            dot=False,
        ),
        data=DashboardState.data_stream,
        height=450,
        width="100%",
    )


def get_area_chart():
    return rx.recharts.area_chart(
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3",
            horizontal=True,
            vertical=False,
            class_name="text-gray-300",
        ),
        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
        rx.el.svg.defs(
            rx.el.svg.linear_gradient(
                rx.el.svg.stop(
                    offset="5%",
                    stop_color=DashboardState.chart_line_color,
                    stop_opacity=0.4,
                ),
                rx.el.svg.stop(
                    offset="95%",
                    stop_color=DashboardState.chart_line_color,
                    stop_opacity=0,
                ),
                id="area-gradient",
                x1="0",
                y1="0",
                x2="0",
                y2="1",
            )
        ),
        rx.recharts.x_axis(
            data_key="time",
            type_="number",
            domain=["dataMin", "dataMax"],
            axis_line=False,
            tick_line=False,
        ),
        rx.recharts.y_axis(
            domain=[50, 250],
            axis_line=False,
            tick_line=False,
        ),
        rx.recharts.area(
            data_key="value",
            type_="monotone",
            stroke=DashboardState.chart_line_color,
            fill="url(#area-gradient)",
            stroke_width=2.5,
            dot=False,
        ),
        data=DashboardState.data_stream,
        height=450,
        width="100%",
    )


def live_line_chart():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.cond(
                    DashboardState.is_streaming,
                    rx.el.span(
                        rx.el.span(
                            class_name="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"
                        ),
                        rx.el.span(
                            class_name="relative inline-flex rounded-full h-3 w-3 bg-green-500"
                        ),
                        class_name="relative flex h-3 w-3",
                    ),
                    rx.el.span(
                        class_name="inline-flex rounded-full h-3 w-3 bg-red-500"
                    ),
                ),
                rx.el.h2(
                    "Live Market Value",
                    class_name="text-lg font-semibold text-gray-800",
                ),
                class_name="flex items-center gap-x-3",
            ),
            rx.el.div(
                chart_color_selector(),
                chart_selector(),
                class_name="flex items-center space-x-4",
            ),
            class_name="w-full flex items-center justify-between pb-4 border-b border-gray-200",
        ),
        rx.el.div(
            rx.match(
                DashboardState.active_chart,
                (0, get_area_chart()),
                (1, get_line_chart()),
            ),
            class_name="w-full pt-4",
        ),
        class_name="col-span-1 lg:col-span-2 h-full flex flex-col p-6 bg-white rounded-2xl border border-gray-200 shadow-sm",
    )