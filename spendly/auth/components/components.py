import reflex as rx

def my_heading(heading: str,src: str, error_component: rx.Component)->rx.Component:
    return rx.center(
        rx.image(
            src=src,
            width="2.5em",
            height="auto",
            border_radius="25%",
        ),
        rx.heading(
            heading,
            size="6",
            as_="h2",
            text_align="center",
            width="100%",
        ),
        error_component,
        direction="column",
        spacing="5",
        width="100%",
    )

def my_input(label: str, name:str, placeholder:str, icon:str, **props)->rx.Component:
    return rx.vstack(
        rx.text(
            label,
            size="3",
            weight="medium",
            text_align="left",
            width="100%",
        ),
        rx.input(
            rx.input.slot(rx.icon(icon)),
            placeholder=placeholder,
            id=name,
            name=name,
            size="3",
            width="100%",
            **props
        ),
        spacing="2",
        width="100%",
    ),