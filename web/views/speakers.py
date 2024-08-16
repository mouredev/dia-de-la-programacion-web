import reflex as rx
from web.styles import styles
from web.styles.colors import Color
from web.styles.fonts import Font, FontWeight
from web.styles.styles import Size, SizeEM
from web.components.badge import badge


def speakers(text: str, icon: str, title: str) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                badge(text, icon),
                rx.heading(
                    title,
                    as_="h3", size=Size.BIG.value
                ),
                spacing=SizeEM.SMALL.value,
            ),
            rx.vstack(
                rx.hstack(
                    rx.icon(
                        "gamepad",
                        height=SizeEM.BIG.value,
                        width="auto"
                    ),
                    rx.text(
                        "Desarrollo de videojuegos",
                        size=Size.BIG.value
                    ),
                    spacing=SizeEM.DEFAULT.value,
                    align="center"
                ),
                rx.flex(
                    _speaker(
                        "Alva Majo",
                        "Indie gamedev | Majorariatto",
                        "5ro4",
                        "https://alvamajo.com"
                    ),
                    _speaker(
                        "Rocío Tomé",
                        "Gamedev | Patattie Games",
                        "rothiotome",
                        "https://linktr.ee/rothiotome"
                    ),
                    _speaker(
                        "Samuel Molina",
                        "Senior Game Content Designer | CloudImperium",
                        "fukuy",
                        "https://samuelmolina.site"
                    ),
                    spacing=Size.BIG.value,
                    flex_direction=["column", "column", "row"],
                    width="100%",
                ),
                background_color=Color.ACCENT_ALPHA.value,
                spacing=Size.MEDIUM.value,
                padding="var(--space-5)",
                border_radius="var(--radius-5)",
                width="100%"
            ),
            rx.text("Más anuncios próximamente..."),
            spacing=Size.BIG.value,
            style=styles.max_width_style
        ),
        width="100%"
    )


def _speaker(name, description, handler, url) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=f"/speakers/{handler}.png",
            width=rx.breakpoints(initial="100px", sm="150px"),
            height=rx.breakpoints(initial="100px", sm="150px"),
            border_radius="50%",
            background=Color.ACCENT.value,
            alt=f"Avatar de {name}",
            margin_bottom=SizeEM.DEFAULT.value
        ),
        rx.text(
            name,
            font_family=Font.DEFAULT.value,
            font_weight=FontWeight.BOLD.value,
            size=Size.MEDIUM_VERY_BIG.value
        ),
        rx.text(description),
        rx.link(
            f"@{handler}",
            href=url,
            color=Color.ACCENT.value,
            is_external=True
        ),
        width="100%",
        spacing=Size.ZERO.value
    )
