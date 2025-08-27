import reflex as rx
from app.pages.index import index
from app.pages.products import products
from app.pages.news import news
from app.pages.contact import contact
from app.pages.product_detail import product_detail
from app.pages.our_story import our_story
from app.pages.faq import faq
from app.pages.news_article import news_article
from app.states.article_state import ArticleState
from app.admin.pages.login import login_page
from app.admin.pages.dashboard import dashboard_page
from app.admin.states.auth_state import AuthState
from app.admin.states.admin_dashboard_state import (
    AdminDashboardState,
)
from app.admin.states.edit_article_state import (
    EditArticleState,
)
from app.admin.states.asset_state import AssetState
from app.admin.pages.edit_article import edit_article_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/home.css"],
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)



app.add_page(index, route="/")
app.add_page(products, route="/products")
app.add_page(product_detail, route="/products/[product_id]")
app.add_page(news, route="/news")
app.add_page(
    news_article,
    route="/news/[article_id]",
    on_load=ArticleState.get_article,
)
app.add_page(contact, route="/contact")
app.add_page(our_story, route="/our-story")
app.add_page(faq, route="/faq")
app.add_page(login_page, route="/admin/login")
app.add_page(
    dashboard_page,
    route="/admin/dashboard",
    on_load=[
        AdminDashboardState.load_news,
        AuthState.check_session,
    ],
)
app.add_page(
    edit_article_page,
    route="/admin/edit-article/[article_id]",
    on_load=[
        EditArticleState.get_article,
        AssetState.load_assets,
        AuthState.check_session,
    ],
)