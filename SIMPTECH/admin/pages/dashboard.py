import reflex as rx
from SIMPTECH.admin.states.auth_state import AuthState
from SIMPTECH.admin.states.admin_dashboard_state import (
    AdminDashboardState,
)
from SIMPTECH.states.news_state import NewsArticle


def admin_sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Simptech Admin",
            class_name="text-2xl font-bold text-white mb-8",
        ),
        rx.el.nav(
            rx.el.a(
                rx.icon(
                    tag="layout-dashboard",
                    class_name="mr-3",
                ),
                "Dashboard",
                href="/admin/dashboard",
                class_name="flex items-center px-4 py-2.5 text-gray-300 bg-gray-700 rounded-lg",
            )
        ),
        rx.el.div(class_name="flex-grow"),
        rx.el.button(
            rx.icon(tag="log-out", class_name="mr-3"),
            "Logout",
            on_click=AuthState.sign_out,
            class_name="flex items-center w-full px-4 py-2.5 text-gray-300 hover:bg-gray-700 rounded-lg",
        ),
        class_name="w-64 bg-gray-800 text-white p-6 flex flex-col h-screen",
    )


def news_management_table() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "News Management",
            class_name="text-3xl font-bold mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Title",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        AdminDashboardState.news_articles,
                        lambda article: rx.el.tr(
                            rx.el.td(
                                article["title"],
                                class_name="px-6 py-4 whitespace-nowrap",
                            ),
                            rx.el.td(
                                article["date"],
                                class_name="px-6 py-4 whitespace-nowrap",
                            ),
                            rx.el.td(
                                rx.el.a(
                                    "Edit",
                                    href=f"/admin/edit-article/{article['id']}",
                                    class_name="text-indigo-600 hover:text-indigo-900",
                                ),
                                class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
                            ),
                            class_name="bg-white",
                        ),
                    ),
                    class_name="divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
        ),
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        admin_sidebar(),
        rx.el.main(
            news_management_table(),
            class_name="flex-1 p-10 bg-gray-100",
        ),
        class_name="flex font-['Inter']",
    )