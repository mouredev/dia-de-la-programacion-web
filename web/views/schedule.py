import reflex as rx
from web import constants
from web.components.button import button
from web.styles import styles
from web.styles.colors import Color
from web.styles.fonts import FontWeight
from web.styles.styles import Size, SizeEM
from web.components.badge import badge


def schedule() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                badge("Agenda", "calendar-clock"),
                rx.heading(
                    "Esto es todo lo que te espera",
                    as_="h3", size=Size.BIG.value
                ),
                spacing=Size.SMALL.value,
            ),
            _schedule_event(
                "16:00",
                "party-popper",
                "Bienvenida",
                "Con Brais Moure"
            ),
            _schedule_event(
                "16:30",
                "lock-keyhole",
                "Ciberseguridad y hacking + sorteo regalos",
                "Con Chema Alonso, Daniela Maissi y S4vitar"
            ),
            _schedule_event(
                "17:30",
                "trending-up",
                "De Junior a Senior + sorteo regalos",
                "Con Afor digital, AristiDevs y Carlos Azaustre"
            ),
            _schedule_event(
                "18:30",
                "file-question",
                "Presentación proyecto secreto + sorteo regalos",
                "Con Brais Moure"
            ),
            _schedule_event(
                "19:30",
                "gamepad",
                "Desarrollo de videojuegos + sorteo regalos",
                "Con Alva Majo, Rocío Tomé y Samuel Molina"
            ),
            _schedule_event(
                "20:30",
                "graduation-cap",
                "Aprendizaje efectivo + sorteo regalos",
                "Con Fernando Herrera, Todo Code y Manz"
            ),
            _schedule_event(
                "21:30",
                "handshake",
                "Los beneficios de una comunidad + sorteo regalos",
                "Con miembros destacados de la comunidad de Discord"
            ),
            _schedule_event(
                "22:30",
                "beer",
                "Más allá del código + sorteo regalos",
                "Con Héctor de León, Nicolás Schürmann y Brais Moure"
            ),
            _schedule_event(
                "23:30",
                "hand-metal",
                "Despedida",
                "Con Brais Moure"
            ),
            button(
                "calendar-check",
                "Crea un recordatorio",
                constants.DISCORD_EVENT_URL
            ),
            rx.text(
                "* Horario España (CEST). Consulta en el evento de ",
                rx.link(
                    "Discord",
                    color=Color.ACCENT.value,
                    href=constants.DISCORD_EVENT_URL,
                    is_external=True
                ),
                " el horario de inicio en tu país."
            ),
            spacing=Size.BIG.value,
            style=styles.max_width_style
        ),
        width="100%"
    )


def _schedule_event(time: str, icon: str, title: str, subtitle: str) -> rx.Component:
    return rx.flex(
        rx.text(
            time,
            size=Size.BIG.value,
            font_weight=FontWeight.BOLD.value,
            height="100%"
        ),
        rx.vstack(
            rx.mobile_only(
                rx.icon(
                    icon,
                    height=SizeEM.BIG.value,
                    width="auto"
                )
            ),
            rx.hstack(
                rx.tablet_and_desktop(
                    rx.icon(
                        icon,
                        height=SizeEM.BIG.value,
                        width="auto"
                    )
                ),
                rx.text(
                    title,
                    size=Size.BIG.value
                ),
                spacing=SizeEM.DEFAULT.value,
                align="center"
            ),
            rx.text(subtitle),
            width="100%"
        ),
        flex_direction=["column", "row"],
        background_color=Color.ACCENT_ALPHA.value,
        spacing=Size.MEDIUM.value,
        # align_items="center",
        padding="var(--space-5)",
        border_radius="var(--radius-5)",
        width="100%"
    )
