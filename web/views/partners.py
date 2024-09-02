import reflex as rx
from web import constants
from web.styles.colors import Color
import web.styles.styles as styles
from web.styles.styles import Size
from web.components.partner import partner
from web.components.button import button


def partners() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Patrocinado por",
                as_="h3",
                size=Size.BIG.value,
                color=Color.DARK.value
            ),
            rx.flex(
                partner(
                    "/partners/raiola.png",
                    "https://mouredev.com/raiola",
                    "20% en hosting"
                ),
                partner(
                    "/partners/nuwe.png",
                    "https://bit.ly/JobOffersNUWE",
                    "Compite y demuestra tu talento tech"
                ),
                partner(
                    "/partners/elgato.png",
                    "https://elgato.sjv.io/mouredev",
                    "5% código ZZ-MOUREDEV"
                ),
                partner(
                    "/partners/mypublicinbox.png",
                    "https://mypublicinbox.com",
                    "Contacta con perfiles relevantes"
                ),
                spacing=Size.DEFAULT.value,
                wrap="wrap"
            ),
            rx.spacer(),
            button(
                "mail",
                "¿Quieres ser patrocinador?",
                "mailto:braismoure@mouredev.com",
                True
            ),
            rx.text(
                "Puedes escribirme a ",
                rx.link(
                    "braismoure@mouredev.com",
                    href="mailto:braismoure@mouredev.com",
                    is_external=True,
                    color=Color.DARK.value
                ),
                " o contactarme a través de mis redes sociales como ",
                rx.link(
                    "@mouredev",
                    href=constants.MOUREDEV_URL,
                    is_external=True,
                    color=Color.DARK.value
                ),
                "."
            ),
            color=Color.DARK.value,
            spacing=Size.DEFAULT.value,
            style=styles.max_width_style
        ),
        background=Color.ACCENT.value,
        width="100%"
    )
