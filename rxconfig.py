import reflex as rx

config = rx.Config(
    app_name="app", plugins=[rx.plugins.TailwindV3Plugin()],
    show_built_with_reflex=False
)