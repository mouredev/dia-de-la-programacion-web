import reflex as rx
from sqlalchemy import true
from web.styles import styles
from web.styles.colors import Color
from web.styles.fonts import Font, FontWeight
from web.styles.styles import Size, SizeEM
from web.components.badge import badge


def gifts() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                badge("Regalos", "gift"),
                rx.heading(
                    "Sorteo de regalos entre todos los asistentes",
                    as_="h3", size=Size.BIG.value
                ),
                spacing=Size.SMALL.value,
            ),
            rx.grid(
                _gift(
                    "sd", "Stream Deck + más USB Hub",
                    "https://elgato.com/es/es/p/stream-deck-plus-black"
                ),
                _gift(
                    "keychron", "Teclado Keychron",
                    "https://keychron.com/collections/all-keyboards"
                ),
                _gift(
                    "ks", "Logitech MX Keys S",
                    "https://www.logitech.com/es-es/products/keyboards/mx-keys-s.html"
                ),
                _gift(
                    "m3", "Logitech MX Master 3S",
                    "https://www.logitech.com/es-es/products/mice/mx-master-3s.910-006559.html"
                ),
                _gift(
                    "hm", "Suscripciones Hola Mundo",
                    "https://holamundo.io"
                ),
                _gift(
                    "hdl", "Suscripciones Héctor de León",
                    "https://udemy.com/user/hector-de-leon-3"
                ),
                _gift(
                    "h4u", "Suscripciones Hack4u",
                    "https://hack4u.io"
                ),
                _gift(
                    "dt", "Suscripciones DevTalles",
                    "https://cursos.devtalles.com"
                ),
                _gift(
                    "tc", "Suscripciones a TodoCode",
                    "https://todocodeacademy.com"
                ),
                _gift(
                    "js", "Libros dominando JavaScript",
                    "https://leanpub.com/dominandojavascript"
                ),
                _gift(
                    "ntep", "Libros no todo es programar",
                    "https://notodoesprogramar.com/"
                ),
                _gift(
                    "git", "Muchos libros de Git y GitHub",
                    "https://mouredev.link/libro-git"
                ),
                spacing=Size.BIG.value,
                columns=rx.breakpoints(initial="1", sm="2"),
                width="100%"
            ),
            rx.text("Más regalos próximamente..."),
            spacing=Size.BIG.value,
            style=styles.max_width_style
        ),
        width="100%"
    )


def _gift(image: str, title: str, url: str) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=f"/gifts/{image}.png",
            height=rx.breakpoints(initial="100px", sm="150px"),
            width="auto",
            border_radius="var(--radius-5)",
            background=Color.ACCENT.value,
            alt=f"Sorteo: {title}"
        ),
        rx.text(
            title,
            font_family=Font.DEFAULT.value,
            font_weight=FontWeight.BOLD.value,
            size=Size.BIG.value
        ),
        on_click=rx.redirect(url, True),
        cursor="pointer",
        background_color=Color.ACCENT_ALPHA.value,
        spacing=Size.MEDIUM.value,
        padding="var(--space-5)",
        border_radius="var(--radius-5)",
        width="100%"
    )
