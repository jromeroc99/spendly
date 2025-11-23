import reflex as rx
from ..state.register_state import MyRegistrationState
from ..state.login_state import MyLoginState
from .components import my_heading, my_input

def my_login_error() -> rx.Component:
    """Render the login error message."""
    return rx.cond(
        MyLoginState.error_message != "",
        rx.callout(
            MyLoginState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )


def my_login_form() -> rx.Component:
    return rx.form(
        rx.card(
            rx.vstack(
                my_heading(
                    "Inicia sesión en tu cuenta",
                    src="/favicon.ico",
                    error_component=my_login_error(),
                ),
                my_input(
                    label="Usuario",
                    name="username",
                    placeholder="Introduce tu nombre de usuario",
                    icon="user",
                ),
                my_input(
                    label="Contraseña",
                    name="password",
                    placeholder="Introduce tu contraseña",
                    icon="lock",
                    type="password",
                ),
                rx.button("Iniciar sesión", size="3", width="100%"),
                rx.center(
                    rx.text("¿Eres nuevo?", size="3"),
                    rx.link("Regístrate", on_click=MyRegistrationState.redir, size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            min_width="50vh",
            max_width="28em",
            size="4",
            width="100%",
        ),
        on_submit=MyLoginState.on_submit
    )


