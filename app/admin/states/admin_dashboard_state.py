import reflex as rx
from app.states.news_state import NewsState, NewsArticle


class AdminDashboardState(rx.State):
    news_articles: list[NewsArticle] = []

    async def load_news(self):
        news_state = await self.get_state(NewsState)
        self.news_articles = news_state.articles