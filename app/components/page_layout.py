import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def page_layout(
    child: rx.Component, title: str
) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    title,
                    class_name="text-4xl font-bold text-gray-900 mb-8 text-center",
                ),
                child,
                class_name="container mx-auto px-4 py-8 pt-24",
            ),
            class_name="flex-grow",
        ),
        footer(),
        class_name="min-h-screen flex flex-col bg-white text-gray-800 font-['Inter']",
    )