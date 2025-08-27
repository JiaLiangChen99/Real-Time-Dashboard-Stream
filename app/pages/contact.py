import reflex as rx
from app.components.page_layout import page_layout


def contact() -> rx.Component:
    return page_layout(
        rx.el.div(class_name="text-center text-gray-600"),
        "Contact",
    )