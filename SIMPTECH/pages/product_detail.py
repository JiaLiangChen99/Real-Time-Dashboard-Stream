import reflex as rx
from SIMPTECH.components.page_layout import page_layout
from SIMPTECH.states.state import State


def product_detail() -> rx.Component:
    return page_layout(
        rx.cond(
            State.current_product,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.img(
                            src=State.current_product["img_url"],
                            alt=State.current_product["name"],
                            class_name="w-full h-full object-cover rounded-lg",
                        ),
                        # class_name="w-full lg:w-1/2 bg-gray-200 rounded-lg h-96"
                    ),
                    rx.el.div(
                        rx.el.h2(
                            State.current_product["name"],
                            class_name="text-4xl font-extrabold text-gray-900",
                        ),
                        rx.el.p(
                            State.current_product[
                                "description"
                            ],
                            class_name="text-lg text-gray-600 mt-4",
                        ),
                        # rx.el.p(
                        #     f"${State.current_product['price']}",
                        #     class_name="text-3xl font-bold text-gray-800 my-6",
                        # ),
                        # rx.el.button(
                        #     "Add to Cart",
                        #     rx.icon(
                        #         tag="shopping-cart",
                        #         class_name="mr-2",
                        #     ),
                        #     class_name="flex items-center justify-center bg-gray-900 hover:bg-gray-700 text-white font-bold py-3 px-8 rounded-lg transition-colors duration-300",
                        # ),
                        class_name="w-full lg:w-1/2 lg:pl-12 mt-8 lg:mt-0",
                    ),
                    class_name="flex flex-col lg:flex-row items-center",
                )
            ),
            rx.el.div(
                rx.el.h2(
                    "Product Not Found",
                    class_name="text-2xl text-red-500",
                ),
                class_name="text-center",
            ),
        ),
        title="Product Detail",
    )