import reflex as rx
from app.components.page_layout import page_layout
from app.states.news_state import NewsState, NewsArticle


def news_card(article: NewsArticle) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.img(
                src=article["image_url"],
                class_name="w-full h-48 object-cover rounded-t-lg",
            ),
            href=f"/news/{article['id']}",
        ),
        rx.el.div(
            rx.el.p(
                article["date"],
                class_name="text-sm text-gray-500 mb-2",
            ),
            rx.el.h3(
                article["title"],
                class_name="text-xl font-bold text-gray-900 mb-2",
            ),
            rx.el.p(
                article["description"],
                class_name="text-gray-600 mb-4",
            ),
            rx.el.a(
                "Read More",
                rx.icon(
                    tag="arrow-right",
                    class_name="ml-2 h-4 w-4",
                ),
                href=f"/news/{article['id']}",
                class_name="inline-flex items-center font-semibold text-blue-600 hover:text-blue-800 transition-colors",
            ),
            class_name="p-6",
        ),
        class_name="bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm hover:shadow-lg transition-shadow duration-300",
    )


def news_header() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Stay Updated",
            class_name="text-5xl font-bold text-gray-800",
        ),
        rx.el.p(
            "Follow the latest news, events, and stories from the Simptech team.",
            class_name="mt-4 text-lg text-gray-600 max-w-2xl mx-auto",
        ),
        class_name="text-center py-16 bg-gray-50 mb-12",
    )


def news() -> rx.Component:
    return page_layout(
        rx.el.div(
            news_header(),
            rx.el.div(
                rx.foreach(NewsState.articles, news_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 container mx-auto px-4",
            ),
        ),
        "News",
    )