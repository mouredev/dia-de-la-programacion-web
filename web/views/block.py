import reflex as rx
from web.styles import styles
from web.styles.styles import Size
from web.components.badge import badge


def block(text: str, icon: str, title: str) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                badge(text, icon),
                rx.heading(
                    title,
                    as_="h3", size=Size.BIG.value
                ),
                spacing=Size.SMALL.value,
            ),
            rx.text("Próximamente..."),
            spacing=Size.DEFAULT.value,
            style=styles.max_width_style
        ),
        width="100%"
    )
