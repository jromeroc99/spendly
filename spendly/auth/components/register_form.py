import reflex as rx
from ..state.register_state import MyRegistrationState

def my_register_error() -> rx.Component:
    """Render the registration error message."""
    return rx.cond(
        MyRegistrationState.error_message != "",
        rx.callout(
            MyRegistrationState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )

def my_register_form() -> rx.Component:
    from .components import my_heading, my_input
    return rx.form(
        rx.card(
            rx.vstack(
                my_heading(
                    "Crea una cuenta",
                    src="/favicon.ico",
                    error_component=my_register_error(),
                ),
                my_input(
                    label="Email",
                    name="email",
                    placeholder="Introduce tu correo electrónico",
                    icon="mail",
                    type="email"
                ),
                my_input(
                    label="Nombre de usuario",
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
                my_input(
                    label="Confirma contraseña",
                    name="confirm_password",
                    placeholder="Introduce tu contraseña",
                    icon="lock",
                    type="password",
                ),
                #rx.box(
                    #rx.checkbox(
                        #"Acepto los Términos y Condiciones",
                        #default_checked=True,
                        #spacing="2",
                    #),
                    #width="100%",
                #),
                rx.button(
                    "Registrarse", 
                    size="3", 
                    width="100%",
                ),
                rx.center(
                    rx.text("¿Ya tienes cuenta?", size="3"),
                    rx.link("Inicia sesión", href="/login", size="3"),
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
        on_submit=MyRegistrationState.handle_registration_email
    )