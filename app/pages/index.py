import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.states.state import State, Feature


def feature_card(feature: Feature) -> rx.Component:
    return rx.el.div(
        rx.icon(
            tag=feature["icon"],
            class_name="h-8 w-8 text-blue-400 mb-4",
        ),
        rx.el.h3(
            feature["title"],
            class_name="text-xl font-bold text-white mb-2",
        ),
        rx.el.p(
            feature["text"], class_name="text-gray-400"
        ),
        class_name="bg-gray-800 p-6 rounded-lg border border-gray-700 text-center h-full shadow-lg",
    )


def product_showcase_card(product: dict) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src=product["image_url"],
            class_name="w-full h-80 object-cover rounded-lg",
        ),
        rx.el.p(
            product["name"],
            class_name="mt-4 font-semibold text-lg text-center text-white",
        ),
        class_name="bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-700",
    )


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.section(
                rx.el.div(
                    rx.el.h1(
                        State.homepage_content["hero"][
                            "title"
                        ],
                        class_name="text-5xl md:text-7xl font-extrabold text-white tracking-tighter",
                    ),
                    rx.el.p(
                        State.homepage_content["hero"][
                            "subtitle"
                        ],
                        class_name="mt-4 max-w-2xl mx-auto text-lg text-gray-200 font-medium",
                    ),
                    rx.el.a(
                        State.homepage_content["hero"][
                            "button_text"
                        ],
                        href=State.homepage_content["hero"][
                            "button_url"
                        ],
                        class_name="mt-8 inline-block bg-blue-500 hover:bg-blue-600 backdrop-blur-sm text-white font-bold py-3 px-8 rounded-lg border border-blue-400/50 transition-colors duration-300",
                    ),
                    class_name="hero-bg relative w-full h-[70vh] flex flex-col items-center justify-center text-center text-white p-4",
                    style={
                        "background_image": f"url({State.homepage_content['hero']['background_image']})"
                    },
                )
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.h2(
                        "Shop The Collections",
                        class_name="text-4xl font-bold text-white text-center mb-12",
                    ),
                    rx.el.div(
                        rx.foreach(
                            State.index_products,
                            product_showcase_card,
                        ),
                        class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-8",
                    ),
                    class_name="container mx-auto px-4 py-16",
                ),
                class_name="bg-gray-900",
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.el.img(
                            src=State.homepage_content[
                                "showcase"
                            ]["image_url"],
                            class_name="w-full h-auto object-cover rounded-lg shadow-2xl",
                        ),
                        class_name="w-full lg:w-1/2",
                    ),
                    rx.el.div(
                        rx.el.h2(
                            State.homepage_content[
                                "showcase"
                            ]["title"],
                            class_name="text-3xl font-extrabold text-white",
                        ),
                        rx.el.p(
                            State.homepage_content[
                                "showcase"
                            ]["subtitle"],
                            class_name="mt-4 text-lg text-gray-400",
                        ),
                        rx.el.a(
                            State.homepage_content[
                                "showcase"
                            ]["button_text"],
                            href=State.homepage_content[
                                "showcase"
                            ]["button_url"],
                            class_name="mt-6 inline-block bg-blue-500 text-white font-bold py-3 px-8 rounded-lg hover:bg-blue-600 transition-colors",
                        ),
                        class_name="w-full lg:w-1/2 flex flex-col justify-center lg:pl-12 mt-8 lg:mt-0",
                    ),
                    class_name="container mx-auto px-4 py-16 flex flex-col lg:flex-row items-center",
                ),
                class_name="bg-gray-800",
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.h2(
                        State.homepage_content[
                            "brand_story"
                        ]["title"],
                        class_name="text-4xl font-bold text-white text-center mb-12",
                    ),
                    rx.el.div(
                        rx.foreach(
                            State.homepage_content[
                                "brand_story"
                            ]["features"],
                            feature_card,
                        ),
                        class_name="grid md:grid-cols-3 gap-8",
                    ),
                    class_name="container mx-auto px-4 py-16",
                ),
                class_name="bg-gray-900",
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.h2(
                        "What Our Customers Say",
                        class_name="text-4xl font-bold text-white text-center mb-12",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.foreach(
                                        range(5),
                                        lambda i: rx.icon(
                                            tag="star",
                                            class_name="h-6 w-6 text-yellow-400 fill-current",
                                        ),
                                    ),
                                    class_name="flex justify-center mb-6",
                                ),
                                rx.el.p(
                                    f'"{State.current_testimonial.quote}"',
                                    class_name="text-xl font-medium text-gray-200 italic mb-6 text-center",
                                ),
                                rx.el.p(
                                    f"- {State.current_testimonial.author}",
                                    class_name="font-bold text-white text-center text-lg",
                                ),
                                class_name="bg-blue-900/60 backdrop-blur-sm p-8 rounded-2xl shadow-lg border border-blue-700/50 max-w-3xl mx-auto",
                            ),
                            class_name="relative w-full",
                        ),
                        rx.el.button(
                            rx.icon(
                                tag="chevron-left",
                                class_name="h-8 w-8",
                            ),
                            on_click=State.prev_testimonial,
                            class_name="absolute left-0 top-1/2 -translate-y-1/2 bg-white/10 hover:bg-white/20 text-white p-3 rounded-full transition-all duration-300",
                        ),
                        rx.el.button(
                            rx.icon(
                                tag="chevron-right",
                                class_name="h-8 w-8",
                            ),
                            on_click=State.next_testimonial,
                            class_name="absolute right-0 top-1/2 -translate-y-1/2 bg-white/10 hover:bg-white/20 text-white p-3 rounded-full transition-all duration-300",
                        ),
                        class_name="relative flex items-center justify-center",
                    ),
                    rx.el.div(
                        rx.foreach(
                            State.testimonials,
                            lambda item, index: rx.el.button(
                                on_click=lambda: State.set_testimonial(
                                    index
                                ),
                                class_name=rx.cond(
                                    State.current_testimonial_index
                                    == index,
                                    "w-3 h-3 bg-blue-400 rounded-full transition-all duration-300",
                                    "w-3 h-3 bg-gray-600 hover:bg-gray-400 rounded-full transition-all duration-300",
                                ),
                            ),
                        ),
                        class_name="flex justify-center space-x-3 mt-8",
                    ),
                    class_name="container mx-auto px-4 py-20",
                ),
                class_name="bg-blue-950",
            ),
        ),
        footer(),
        class_name="min-h-screen flex flex-col bg-gray-900 text-gray-300 font-['Inter']",
    )