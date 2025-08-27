import reflex as rx
from app.components.page_layout import page_layout
from app.states.state import State


def product_card(product: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                class_name="bg-gray-200 h-48 w-full rounded-t-lg"
            ),
            rx.el.div(
                rx.el.h3(
                    product["name"],
                    class_name="text-xl font-bold text-gray-900",
                ),
                rx.el.p(
                    product["description"],
                    class_name="text-gray-600 mt-2",
                ),
                rx.el.p(
                    f"${product['price']}",
                    class_name="text-lg font-semibold text-gray-800 mt-4",
                ),
                class_name="p-6",
            ),
            class_name="bg-white border border-gray-200 rounded-lg overflow-hidden transform hover:-translate-y-1 transition-transform duration-300 hover:shadow-lg",
        ),
        href=f"/products/{product['product_id']}",
    )


def products() -> rx.Component:
    return page_layout(
        rx.el.div(
            rx.foreach(State.products, product_card),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
        ),
        "Products",
    )