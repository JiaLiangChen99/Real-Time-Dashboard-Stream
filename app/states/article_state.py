import reflex as rx
from typing import TypedDict


class Article(TypedDict):
    id: str
    title: str
    date: str
    content: str


class ArticleState(rx.State):
    """State for a single news article."""

    articles_db: dict[str, Article] = {
        "brand-story": {
            "id": "brand-story",
            "title": "Simptech Brand Story",
            "date": "November 1, 2023",
            "content": '\n<h3>The Simptech Brand Story</h3>\n<p>In this fast-paced era, travel and commuting have become an integral part of modern urban life. We found that people\'s troubles on the road are often not about the distance to the destination, but about the seemingly trivial yet extremely energy-consuming small things along the way: overweight luggage, dead devices, lost important items, and disorganized storage.</p>\n<p>The birth of Simptech was precisely to change all this.</p>\n<p>The founding team comes from a background in technology and industrial design. They know that tech products are often burdened by "feature stacking," which ignores real-life usage scenarios. Thus, we proposed a simple yet powerful mission: to simplify travel with technology.</p>\n<p>We don\'t do technology for technology\'s sake. Instead, we skillfully blend smart functions with minimalist aesthetics, making luggage a true and capable partner for users.</p>\n<p>The first-generation <strong>Smart Suitcase</strong> had a built-in power bank and GPS positioning function, making long-distance travel worry-free.</p>\n<p>The subsequently launched <strong>Smart Backpack</strong> integrated an anti-theft system, RFID-blocking pockets, and cable management, becoming a safety guardian for commuters.</p>\n<p>We also developed a <strong>Modular Bag System</strong>. Through magnetic quick-release buckles and detachable liners, one bag can meet the usage needs of different scenarios.</p>\n<p>With continuous user feedback, Simptech constantly iterates its products and combines smart functions with a digital travel experience through a <strong>mobile application</strong>, keeping luggage and users "interconnected" at all times.</p>\n<p>Today, Simptech is not just a luggage company; it represents a way of life: an efficient, simple, and calm travel philosophy.</p>\n<p>We believe that every trip should be easy and pleasant, not a burden.</p>\n<p>We insist on making technology truly serve people, rather than adding complexity.</p>\n<p>We promise to make every product a "masterpiece of balance between minimalist aesthetics and smart technology."</p>\n<p><strong>Simptech — Travel Smart, Travel Simple.</strong></p>\n',
        }
    }
    article: Article | None = None

    async def get_article(self):
        """Get the article from the database based on the article_id param."""
        article_id = self.router.page.params.get(
            "article_id", "no-id"
        )
        async with self:
            self.article = self.articles_db.get(article_id)