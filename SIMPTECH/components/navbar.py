import reflex as rx
from SIMPTECH.states.state import State


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-gray-300 hover:text-white transition-colors duration-300 font-medium",
    )


def mobile_navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="block py-2 px-4 text-sm text-gray-300 hover:bg-gray-700 rounded-md",
        on_click=State.toggle_mobile_menu,
    )


def help_dropdown() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            "Help",
            rx.icon(
                tag="chevron-down",
                class_name="h-4 w-4 ml-1",
            ),
            on_click=State.toggle_help_menu,
            class_name="flex items-center text-gray-300 hover:text-white transition-colors duration-300 font-medium",
        ),
        rx.cond(
            State.show_help_menu,
            rx.el.div(
                rx.el.a(
                    "Our Story",
                    href="/our-story",
                    class_name="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700 rounded-md",
                    on_click=State.toggle_help_menu,
                ),
                rx.el.a(
                    "FAQ",
                    href="/faq",
                    class_name="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700 rounded-md",
                    on_click=State.toggle_help_menu,
                ),
                class_name="absolute right-0 mt-2 w-48 bg-gray-800 rounded-md shadow-lg z-50 py-1",
            ),
        ),
        class_name="relative",
    )


def navbar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.img(
                        src="/logo.png",
                        alt="Simptech Logo",
                        class_name="h-12 w-auto",
                    ),
                    href="/",
                ),
                rx.el.div(class_name="flex-grow"),
                rx.el.div(
                    navbar_link("Home", "/"),
                    navbar_link("Products", "/products"),
                    navbar_link("News", "/news"),
                    help_dropdown(),
                    class_name="hidden md:flex items-center space-x-8",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon(
                            tag="menu",
                            class_name="h-6 w-6 text-white",
                        ),
                        on_click=State.toggle_mobile_menu,
                        class_name="md:hidden",
                    ),
                    class_name="flex items-center md:hidden",
                ),
                class_name="container mx-auto flex items-center justify-between p-4",
            ),
            class_name="bg-gray-900/80 backdrop-blur-md text-white fixed top-0 left-0 right-0 z-50 border-b border-gray-800",
        ),
        rx.cond(
            State.is_mobile_menu_open,
            rx.el.div(
                mobile_navbar_link("Home", "/"),
                mobile_navbar_link("Products", "/products"),
                mobile_navbar_link("News", "/news"),
                mobile_navbar_link(
                    "Our Story", "/our-story"
                ),
                mobile_navbar_link("FAQ", "/faq"),
                class_name="md:hidden bg-gray-800 p-4 space-y-2 fixed top-16 left-0 right-0 z-40 rounded-b-lg shadow-lg border-t border-gray-700",
            ),
        ),
    )