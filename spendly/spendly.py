"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .auth.state.login_state import my_require_login
from . import auth

class State(rx.State):
    """The app state."""

@my_require_login
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
app.add_page(
    auth.pages.my_login_page,
    route=auth.routes.LOGIN_ROUTE,
    title="Inicio de sesión",
)
app.add_page(
    auth.pages.my_register_page,
    route=auth.routes.REGISTER_ROUTE,
    title="Crear una cuenta",
)