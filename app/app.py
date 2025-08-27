import reflex as rx
from app.states.dashboard_state import DashboardState
from app.components.live_chart import live_line_chart
from app.components.data_table import live_data_table


def action_button(
    text: str,
    on_click: rx.event.EventType,
    icon: str,
    color_class: str,
) -> rx.Component:
    return rx.el.button(
        rx.icon(tag=icon, class_name="w-4 h-4 mr-2"),
        text,
        on_click=on_click,
        class_name=f"flex items-center justify-center text-sm font-semibold px-4 py-2 rounded-lg border transition-colors {color_class}",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        tag="activity",
                        class_name="w-6 h-6 text-indigo-500",
                    ),
                    rx.el.h1(
                        "Real-Time Data Dashboard",
                        class_name="text-xl font-bold text-gray-800",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.div(
                    action_button(
                        rx.cond(
                            DashboardState.is_streaming,
                            "Stop Stream",
                            "Start Stream",
                        ),
                        DashboardState.toggle_streaming,
                        rx.cond(
                            DashboardState.is_streaming,
                            "square",
                            "play",
                        ),
                        rx.cond(
                            DashboardState.is_streaming,
                            "bg-red-50 text-red-700 border-red-200 hover:bg-red-100",
                            "bg-green-50 text-green-700 border-green-200 hover:bg-green-100",
                        ),
                    ),
                    action_button(
                        "Export CSV",
                        DashboardState.export_data_csv,
                        "cloud_download",
                        "bg-gray-50 text-gray-700 border-gray-200 hover:bg-gray-100",
                    ),
                    action_button(
                        "Export JSON",
                        DashboardState.export_data_json,
                        "file-code",
                        "bg-gray-50 text-gray-700 border-gray-200 hover:bg-gray-100",
                    ),
                    class_name="flex items-center space-x-3",
                ),
                class_name="sticky top-0 left-0 w-full py-3 px-6 flex items-center justify-between border-b border-gray-200 bg-white/70 backdrop-blur-md z-50",
            ),
            rx.el.div(
                live_line_chart(),
                live_data_table(),
                class_name="grid grid-cols-1 lg:grid-cols-3 p-4 sm:p-6 h-full gap-4 sm:gap-6",
            ),
            class_name="w-full h-full flex flex-col",
        ),
        class_name="min-h-screen w-full flex bg-gray-50 font-['Inter'] **:border-gray-200",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Real-Time Dashboard")