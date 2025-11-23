import reflex as rx
from .state.login_state import MyLoginState
from .state.register_state import MyRegistrationState
from .components.login_form import my_login_form
from .components.register_form import my_register_form

PADDING_TOP = "10vh"


def my_login_page()->rx.Component:
    return rx.center(
        rx.cond(
            MyLoginState.is_hydrated,  # type: ignore
            rx.box(my_login_form()),
        ),
        padding_top=PADDING_TOP,
    )

def my_register_page()->rx.Component:
    return rx.center(
            rx.cond(
                MyRegistrationState.success,
                rx.vstack(
                    rx.text("Registro completado correctamente!"),
                ),
                rx.box(my_register_form()),
            ),
            padding_top=PADDING_TOP,
        )


