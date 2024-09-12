import reflex as rx
from web import constants
from web.styles import styles
from web.styles.colors import Color
from web.styles.fonts import Font, FontWeight
from web.styles.styles import Size, SizeEM
from web.components.logo import logo
from web.components.badge import badge
from web.components.button import button


def header() -> rx.Component:
    return rx.center(
        rx.container(
            rx.box(class_name="wave"),
            rx.box(class_name="wave"),
            rx.box(class_name="wave"),
            position="absolute",
            class_name="header_body",
            width="100%",
            height="100%"
        ),
        rx.vstack(
            rx.container(
                rx.text(
                    "Edición ",
                    rx.text(
                        "#",
                        as_="span",
                        color=Color.ACCENT.value
                    ),
                    "4",
                    size=Size.DEFAULT.value,
                    font_weight=FontWeight.BOLD.value,
                    text_align="right",
                    padding_bottom=SizeEM.SMALL.value,
                    width="100%"
                ),
                rx.tablet_and_desktop(
                    logo(Size.VERY_BIG)
                ),
                rx.mobile_only(
                    logo(Size.MEDIUM_VERY_BIG, multiline=True)
                ),
                rx.heading(
                    "Celebra el día ",
                    rx.text(
                        "256",
                        as_="span",
                        color=Color.ACCENT.value
                    ),
                    " del año",
                    as_="h2",
                    size=rx.breakpoints(
                        initial=Size.DEFAULT.value,
                        sm=Size.BIG.value
                    )
                ),
                rx.flex(
                    badge("Charlas", "message-circle", True),
                    badge("Regalos", "gift", True),
                    badge("Comunidad", "heart", True),
                    spacing=Size.SMALL.value,
                    padding_top=SizeEM.SMALL.value,
                ),
                padding=SizeEM.ZERO.value,
            ),
            rx.flex(
                button(
                    "twitch",
                    "twitch.tv/mouredev",
                    constants.TWITCH_URL
                ),
                button(
                    "calendar-check",
                    "Crea un recordatorio",
                    constants.DISCORD_EVENT_URL
                ),
                spacing=Size.DEFAULT.value,
                flex_direction=["column", "row"]
            ),
            rx.vstack(
                rx.text(
                    "Jueves 12 de septiembre de 2024",
                    size=Size.DEFAULT.value,
                    font_weight=FontWeight.BOLD.value,
                    width="100%"
                ),
                rx.hstack(
                    _countdown_text("countdown_days", "días"),
                    _countdown_text("countdown_hours", "horas"),
                    _countdown_text("countdown_minutes", "minutos"),
                    _countdown_text("countdown_seconds", "segundos"),
                    id="countdown",
                    spacing=Size.MEDIUM.value,
                    display="none"
                ),
                rx.link(
                    rx.hstack(
                        rx.icon(
                            "radio"
                        ),
                        rx.text("EN DIRECTO"),
                        class_name="blink"
                    ),
                    href=constants.TWITCH_URL,
                    color="red",
                    id="live",
                    display="none"
                ),
                text_align="center",
                align_items="center"
            ),
            spacing=Size.BIG.value,
            padding_y=SizeEM.VERY_BIG.value,
            align="center",
            style=styles.max_width_style,
            position="relative"
        ),
        rx.script(src="/js/countdown.js"),
        position="relative",
        width="100%",
    )


def _countdown_text(id: str, text: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            "00",
            id=id,
            size=rx.breakpoints(
                initial=Size.MEDIUM_VERY_BIG.value,
                md=Size.VERY_BIG.value
            ),
            font_family=Font.HEADER.value,
            font_weight=FontWeight.BOLD.value,
            text_align="center"
        ),
        rx.text(text, width="100%"),
        align="center",
        spacing=Size.ZERO.value
    )
