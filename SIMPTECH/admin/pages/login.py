import reflex as rx
from SIMPTECH.admin.states.auth_state import AuthState


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Admin Login",
                class_name="text-2xl font-bold text-center text-gray-800",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Username",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        id="username",
                        placeholder="admin",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Password",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        id="password",
                        type="password",
                        placeholder="Password",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-6",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.el.p(
                        AuthState.error_message,
                        class_name="text-red-500 text-sm mb-4 text-center",
                    ),
                ),
                rx.el.button(
                    "Login",
                    type="submit",
                    class_name="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
                ),
                on_submit=AuthState.sign_in,
                reset_on_submit=False,
            ),
            class_name="w-full max-w-sm p-8 space-y-6 bg-white rounded-lg shadow-xl border",
        ),
        class_name="flex items-center justify-center min-h-screen bg-gray-50 font-['Inter']",
    )