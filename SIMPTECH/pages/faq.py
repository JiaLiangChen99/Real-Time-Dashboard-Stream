import reflex as rx
from SIMPTECH.components.page_layout import page_layout
from SIMPTECH.states.faq_state import FAQState, FAQItem


def faq_header() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "We're here to help.",
            class_name="text-5xl font-bold text-gray-800",
        ),
        rx.el.p(
            "Check out our FAQ below, or reach out to us with your questions.",
            class_name="mt-4 text-lg text-gray-600",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    tag="message-circle",
                    class_name="h-8 w-8 text-blue-500 mb-4",
                ),
                rx.el.h3(
                    "Live Chat",
                    class_name="text-xl font-semibold text-gray-800",
                ),
                rx.el.p(
                    "Message us instantly from anywhere on your journey.",
                    class_name="text-gray-500 mt-2",
                ),
                class_name="w-full md:w-1/2 p-6 text-center",
            ),
            rx.el.div(
                rx.icon(
                    tag="mail",
                    class_name="h-8 w-8 text-blue-500 mb-4",
                ),
                rx.el.h3(
                    "help@simptech.com",
                    class_name="text-xl font-semibold text-gray-800",
                ),
                rx.el.p(
                    "Drop us a line at your convenience. We'll get back to you within one business day.",
                    class_name="text-gray-500 mt-2",
                ),
                class_name="w-full md:w-1/2 p-6 text-center border-t md:border-t-0 md:border-l border-gray-200",
            ),
            class_name="mt-12 flex flex-col md:flex-row justify-center max-w-4xl mx-auto border border-gray-200 rounded-lg",
        ),
        class_name="text-center py-16 bg-gray-50",
    )


def faq_item_component(item: FAQItem) -> rx.Component:
    is_open = FAQState.open_items.get(item["id"], False)
    return rx.el.div(
        rx.el.button(
            rx.el.p(
                item["question"],
                class_name="text-lg font-medium text-left text-gray-800",
            ),
            rx.icon(
                tag=rx.cond(is_open, "minus", "plus"),
                class_name="h-6 w-6 text-gray-500",
            ),
            on_click=lambda: FAQState.toggle_item(
                item["id"]
            ),
            class_name="w-full flex justify-between items-center py-6 text-left",
        ),
        rx.cond(
            is_open,
            rx.el.div(
                rx.el.p(
                    item["answer"],
                    class_name="text-gray-600 leading-relaxed pb-6",
                ),
                class_name="prose max-w-none",
            ),
        ),
        class_name="border-b border-gray-200",
    )


def faq_list() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Frequently Asked Questions",
            class_name="text-4xl font-bold text-gray-800 text-center mb-12",
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    FAQState.faq_by_category.items(),
                    lambda category_items: rx.el.div(
                        rx.el.h3(
                            category_items[0],
                            id=category_items[0]
                            .to_string()
                            .lower()
                            .replace(" ", "-"),
                            class_name="text-2xl font-semibold text-gray-700 mt-12 mb-6 pt-4 border-t border-gray-200",
                        ),
                        rx.foreach(
                            category_items[1],
                            faq_item_component,
                        ),
                    ),
                ),
                class_name="w-full lg:w-2/3",
            ),
            rx.el.aside(
                rx.el.h3(
                    "Categories",
                    class_name="text-xl font-semibold text-gray-700 mb-4",
                ),
                rx.el.ul(
                    rx.foreach(
                        FAQState.categories,
                        lambda category: rx.el.li(
                            rx.el.a(
                                category,
                                href=f"#{category.to_string().lower().replace(' ', '-')}",
                                class_name="block py-2 text-gray-600 hover:text-blue-600 transition-colors",
                            )
                        ),
                    ),
                    class_name="space-y-2",
                ),
                class_name="hidden lg:block w-1/3 lg:pl-12 sticky top-24 h-screen",
            ),
            class_name="flex flex-col lg:flex-row container mx-auto px-4",
        ),
        class_name="py-16",
    )


def faq() -> rx.Component:
    return page_layout(
        rx.el.div(faq_header(), faq_list()),
        "Frequently Asked Questions",
    )