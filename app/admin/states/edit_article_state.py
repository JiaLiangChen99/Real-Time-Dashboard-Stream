import reflex as rx
from app.states.article_state import Article, ArticleState
from app.states.news_state import NewsState


class EditArticleState(rx.State):
    article: Article | None = None

    async def get_article(self):
        article_id = self.router.page.params.get(
            "article_id", "no-id"
        )
        article_state = await self.get_state(ArticleState)
        article = article_state.articles_db.get(article_id)
        if article is None:
            yield rx.redirect("/admin/dashboard")
        else:
            self.article = article

    def set_article_field(self, field: str, value: str):
        if self.article:
            self.article[field] = value

    def set_content(self, value: str):
        if self.article:
            self.article["content"] = value

    async def save_article(self):
        if self.article is None:
            return
        article_state = await self.get_state(ArticleState)
        news_state = await self.get_state(NewsState)
        article_id_to_update = self.article["id"]
        article_state.articles_db[article_id_to_update] = (
            self.article
        )
        for i, article_summary in enumerate(
            news_state.articles
        ):
            if (
                article_summary["id"]
                == article_id_to_update
            ):
                news_state.articles[i]["title"] = (
                    self.article["title"]
                )
                news_state.articles[i]["date"] = (
                    self.article["date"]
                )
                break
        yield rx.toast("Article saved successfully!")
        yield rx.redirect("/admin/dashboard")

    def insert_image_url(self, url: str):
        if self.article:
            img_tag = f'\n<img src="{url}" alt="asset" style="max-width: 100%; height: auto;"/>\n'
            current_content = self.article.get(
                "content", ""
            )
            new_content = current_content + img_tag
            self.article["content"] = new_content