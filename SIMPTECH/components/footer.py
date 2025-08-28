import reflex as rx


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-gray-400 hover:text-white transition-colors",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Simptech",
                        class_name="text-2xl font-bold text-white",
                    ),
                    rx.el.p(
                        "Travel Smart, Travel Simple.",
                        class_name="text-gray-400 mt-2",
                    ),
                    class_name="w-full md:w-1/4 mb-8 md:mb-0",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Shop",
                            class_name="text-lg font-semibold text-white mb-4",
                        ),
                        rx.el.div(
                            footer_link("Home", "/"),
                            footer_link(
                                "Products", "/products"
                            ),
                            footer_link("News", "/news"),
                            class_name="flex flex-col space-y-2",
                        ),
                        class_name="w-1/2 sm:w-1/4 md:w-1/4 mb-8 sm:mb-0",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Help",
                            class_name="text-lg font-semibold text-white mb-4",
                        ),
                        rx.el.div(
                            footer_link(
                                "Our Story", "/our-story"
                            ),
                            footer_link("FAQ", "/faq"),
                            class_name="flex flex-col space-y-2",
                        ),
                        class_name="w-1/2 sm:w-1/4 md:w-1/4 mb-8 sm:mb-0",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "123 Tech Avenue, New York, NY 10001, USA",
                                class_name="text-gray-400",
                            ),
                            rx.el.p(
                                "help@foxelli.com",
                                class_name="text-gray-400 mt-2",
                            ),
                            rx.el.p(
                                "1-888-985-3650 (Toll-Free)",
                                class_name="text-gray-400 mt-2",
                            ),
                            class_name="flex flex-col space-y-1",
                        ),
                        class_name="w-full sm:w-1/2 md:w-1/4 mt-8 md:mt-0",
                    ),
                    class_name="flex flex-wrap w-full md:w-3/4 md:pl-8",
                ),
                class_name="flex flex-wrap justify-between",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2025 Simptech. All Rights Reserved.",
                    class_name="text-sm text-gray-500",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            tag="twitter",
                            class_name="h-5 w-5 text-gray-400 hover:text-white",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            tag="github",
                            class_name="h-5 w-5 text-gray-400 hover:text-white",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            tag="linkedin",
                            class_name="h-5 w-5 text-gray-400 hover:text-white",
                        ),
                        href="#",
                    ),
                    class_name="flex space-x-4",
                ),
                class_name="border-t border-gray-800 mt-8 pt-6 flex flex-col sm:flex-row justify-between items-center",
            ),
            class_name="container mx-auto px-6 py-12",
        ),
        class_name="bg-gray-900 border-t border-gray-800 mt-auto",
    )