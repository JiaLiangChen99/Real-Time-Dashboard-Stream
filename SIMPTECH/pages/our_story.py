import reflex as rx


def hero_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Our Story",
                class_name="text-5xl md:text-7xl font-extrabold text-white tracking-tighter",
            ),
            rx.el.p(
                "The journey behind Simptech: Simplifying modern travel with technology.",
                class_name="mt-4 max-w-2xl mx-auto text-lg text-gray-200 font-medium",
            ),
            class_name="relative z-10 w-full h-full flex flex-col items-center justify-center text-center text-white p-4",
        ),
        rx.el.div(
            class_name="absolute inset-0 bg-black opacity-50"
        ),
        style={
            "background_image": "url('/simptech_brand_story.png')",
            "background_size": "cover",
            "background_position": "center",
            "background_repeat": "no-repeat",
        },
        class_name="relative w-full h-[60vh]",
    )


def story_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "The Birth of an Idea",
                    class_name="text-3xl font-bold text-gray-800 mb-4",
                ),
                rx.el.p(
                    "In this fast-paced era, travel and commuting have become integral parts of modern urban life. We noticed a common frustration: the real hassle of being on the move isn't the distance, but the small, seemingly trivial things that drain our energy—overweight luggage, dead devices, lost valuables, and disorganized belongings.",
                    class_name="text-lg text-gray-600 mb-6 leading-relaxed",
                ),
                rx.el.p(
                    "Simptech was born to change all that.",
                    class_name="text-xl font-semibold text-gray-700 leading-relaxed",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.el.h2(
                    "Our Mission: Simplify Travel with Technology",
                    class_name="text-3xl font-bold text-gray-800 mb-4",
                ),
                rx.el.p(
                    "Our founding team, with a background in technology and industrial design, knew that tech products are often burdened by 'feature stacking,' which overlooks real-world use cases. So, we set out with a simple yet powerful mission: to use technology to simplify the way we travel.",
                    class_name="text-lg text-gray-600 mb-6 leading-relaxed",
                ),
                rx.el.p(
                    "We don’t innovate for the sake of technology. Instead, we artfully blend smart functionality with minimalist aesthetics, transforming luggage into a reliable and capable partner for every journey.",
                    class_name="text-lg text-gray-600 leading-relaxed",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.el.h2(
                    "Innovation in Motion",
                    class_name="text-3xl font-bold text-gray-800 mb-6",
                ),
                rx.el.ul(
                    rx.el.li(
                        rx.el.strong(
                            "The first-generation Smart Luggage"
                        ),
                        " featured a built-in power bank and GPS tracking, eliminating anxiety from long-distance travel.",
                        class_name="mb-4",
                    ),
                    rx.el.li(
                        rx.el.strong("Our Smart Backpack"),
                        " integrated an anti-theft system, RFID-blocking pockets, and advanced cable management, becoming a trusted guardian for daily commuters.",
                        class_name="mb-4",
                    ),
                    rx.el.li(
                        rx.el.strong(
                            "The Modular Bag System"
                        ),
                        " was developed with magnetic quick-release buckles and detachable liners, allowing one bag to adapt to various needs, from business to leisure.",
                        class_name="mb-4",
                    ),
                    class_name="list-disc list-inside text-lg text-gray-600 leading-relaxed",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.el.h2(
                    "More Than Just Luggage",
                    class_name="text-3xl font-bold text-gray-800 mb-4",
                ),
                rx.el.p(
                    "Today, Simptech is more than a luggage company—it represents a lifestyle philosophy: efficient, simple, and composed. Through continuous user feedback and our mobile app, we keep our products connected and constantly evolving.",
                    class_name="text-lg text-gray-600 leading-relaxed",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.el.h2(
                    "Our Promise to You",
                    class_name="text-3xl font-bold text-gray-800 mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            tag="check_check",
                            class_name="h-6 w-6 text-blue-500 mr-4",
                        ),
                        rx.el.p(
                            rx.el.strong(
                                "Effortless Journeys:"
                            ),
                            " We believe every trip should be enjoyable, not a burden.",
                        ),
                        class_name="flex items-center text-lg text-gray-700 mb-4",
                    ),
                    rx.el.div(
                        rx.icon(
                            tag="check_check",
                            class_name="h-6 w-6 text-blue-500 mr-4",
                        ),
                        rx.el.p(
                            rx.el.strong(
                                "Meaningful Tech:"
                            ),
                            " We insist that technology should serve people, not add complexity.",
                        ),
                        class_name="flex items-center text-lg text-gray-700 mb-4",
                    ),
                    rx.el.div(
                        rx.icon(
                            tag="check_check",
                            class_name="h-6 w-6 text-blue-500 mr-4",
                        ),
                        rx.el.p(
                            rx.el.strong(
                                "Balanced Design:"
                            ),
                            " We are committed to creating products that perfectly balance minimalist aesthetics with smart technology.",
                        ),
                        class_name="flex items-center text-lg text-gray-700 mb-4",
                    ),
                ),
                class_name="bg-gray-50 p-8 rounded-lg border border-gray-200",
            ),
            rx.el.div(
                rx.el.p(
                    "Simptech — Travel Smart, Travel Simple.",
                    class_name="text-2xl font-bold text-blue-600 italic",
                ),
                class_name="mt-12 text-center",
            ),
            class_name="max-w-4xl mx-auto",
        ),
        class_name="py-16 px-4 md:px-8 bg-white",
    )


def our_story() -> rx.Component:
    from SIMPTECH.components.navbar import navbar
    from SIMPTECH.components.footer import footer

    return rx.el.div(
        navbar(),
        rx.el.main(
            hero_section(),
            story_content(),
            class_name="flex-grow",
        ),
        footer(),
        class_name="min-h-screen flex flex-col bg-white text-gray-800 font-['Inter']",
    )