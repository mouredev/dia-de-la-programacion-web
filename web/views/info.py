import reflex as rx
from web.styles import styles
from web.styles.styles import Size, SizeEM
from web.styles.colors import Color


def info() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "¿Por qué se celebra el día 12 de septiembre?",
                as_="h2", size=Size.BIG.value
            ),
            rx.vstack(
                _info_text(
                    "square-chevron-up",
                    "Es el día 256 de este año (2 elevado a 8)."
                ),
                _info_text(
                    "square-plus",
                    "Es la mayor potencia de 2 menor que 365."
                ),
                _info_text(
                    "square-asterisk",
                    "Es el número de valores que se pueden representar con un byte."
                )
            ),
            rx.callout(
                "¡Es nuestro día! Gratis y para todo el mundo. Siéntete orgullos@, ayuda y comparte. ¡Somos una gran comunidad!",
                icon="heart-handshake",
                color=Color.ACCENT.value,
                background_color=Color.ACCENT_ALPHA.value,
                size="3"
            ),
            spacing=Size.DEFAULT.value,
            style=styles.max_width_style
        ),
        width="100%"
    )


def _info_text(icon, text) -> rx.Component:
    return rx.hstack(
        rx.icon(
            icon,
            color=Color.ACCENT.value,
            height=SizeEM.BIG.value,
            width="auto"
        ),
        rx.text(
            text,
            size=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        align="center"
    ),
