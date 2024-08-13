import reflex as rx
from web import constants
from web.styles import styles
from web.styles.colors import Color


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.link(
                rx.hstack(
                    rx.icon("github"),
                    rx.text.strong("Día de la programación 2024"),
                    color=Color.DARK.value
                ),
                href=constants.REPO_URL,
                is_external=True,
                underline="none"
            ),
            rx.text.strong(
                "Organizado con ♥ (y gracias a ti) por ",
                rx.link(
                    "@mouredev",
                    href=constants.MOUREDEV_URL,
                    is_external=True,
                    color=Color.LIGHT.value
                )
            ),
            align="center",
            style=styles.max_width_style,
        ),
        color=Color.DARK.value,
        width="100%",
        z_index="2"
    )
