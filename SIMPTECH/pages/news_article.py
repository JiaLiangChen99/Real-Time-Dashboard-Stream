import reflex as rx
from SIMPTECH.components.page_layout import page_layout
from SIMPTECH.states.article_state import ArticleState


def article_display() -> rx.Component:
    return rx.el.div(
        rx.cond(
            ArticleState.article,
            rx.el.article(
                rx.el.h1(
                    ArticleState.article["title"],
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4 text-center",
                ),
                rx.el.p(
                    ArticleState.article["date"],
                    class_name="text-gray-500 text-center mb-12 text-lg",
                ),
                rx.el.div(
                    rx.html(
                        ArticleState.article["content"]
                    ),
                    class_name="prose lg:prose-xl max-w-none mx-auto",
                ),
                class_name="bg-white p-8 md:p-12 rounded-lg shadow-lg border border-gray-200",
            ),
            rx.el.div(
                rx.el.h2(
                    "Article not found",
                    class_name="text-2xl text-red-500",
                ),
                rx.el.p(
                    "The article you are looking for does not exist."
                ),
                class_name="text-center",
            ),
        ),
        class_name="max-w-4xl mx-auto py-12",
    )


def news_article() -> rx.Component:
    return page_layout(article_display(), "News Article")