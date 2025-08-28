import reflex as rx
from typing import TypedDict


class NewsArticle(TypedDict):
    id: str
    title: str
    date: str
    description: str
    image_url: str


class NewsState(rx.State):
    """State for the News page."""

    articles: list[NewsArticle] = [
        {
            "id": "Looking Ahead: Simptech’s Vision for the Future of Travel",
            "title": "Looking Ahead: Simptech’s Vision for the Future of Travel",
            "date": "November 12, 2024",  # 十一月份
            "description": "At Simptech, innovation never stops.",
            "image_url": "/smart_travel_article.png",
        },
        {
            "id": "Smart Backpacks & Modular Bags: Simptech Expands Its Core Collection",
            "title": "Smart Backpacks & Modular Bags: Simptech Expands Its Core Collection",
            "date": "October 26, 2024",
            "description": "As commuting and business travel evolve, so do the needs of professionals.",
            "image_url": "/smart_pag_article.png",
        },
        {
            "id": "Introducing Simptech Smart Luggage: A New Era of Intelligent Travel",
            "title": "Introducing Simptech Smart Luggage: A New Era of Intelligent Travel",
            "date": "May 15, 2024", # 五月份
            "description": "We are proud to unveil our flagship line: Simptech Smart Luggage.",
            "image_url": "/smartsuitcase_article.png",
        },
        {
            "id": "Simptech’s Origin: Redefining Travel with Simplified Technology",
            "title": "Simptech’s Origin: Redefining Travel with Simplified Technology",
            "date": "March 28, 2024", # 三月分
            "description": "At Simptech, our journey began with a simple question: why should travel feel complicated?",
            "image_url": "/markorigin.png",
        },
    ]