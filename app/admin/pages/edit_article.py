import reflex as rx
from app.admin.states.auth_state import AuthState
from app.admin.states.edit_article_state import (
    EditArticleState,
)
from app.admin.states.asset_state import AssetState



def edit_article_page() -> rx.Component:
    return rx.text('123')