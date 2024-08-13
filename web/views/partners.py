import reflex as rx
from web.styles.colors import Color
import web.styles.styles as styles
from web.styles.styles import Size
from web.components.partner import partner


def partners() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Patrocinado por",
                as_="h3", size=Size.BIG.value
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
                    "Aplica a vacantes Tech"
                ),
                partner(
                    "/partners/elgato.png",
                    "https://elgato.sjv.io/mouredev",
                    "5% código ZZ-MOUREDEV"
                ),
                spacing=Size.SMALL.value,
                wrap="wrap"
            ),
            # rx.spacer(),
            # rx.text("¿Quieres patrocinar el evento? ¡NO TENGO PALABRAS!"),
            # rx.text(
            #     "Puedes escribirme a ",
            #     rx.link(
            #         "braismoure@mouredev.com",
            #         href="mailto:braismoure@mouredev.com",
            #         is_external=True
            #     ),
            #     " o contactarme a través de mis redes sociales como ",
            #     rx.link(
            #         "@mouredev",
            #         href=constants.MOUREDEV_URL,
            #         is_external=True
            #     ),
            #     "."
            # ),
            spacing=Size.DEFAULT.value,
            style=styles.max_width_style
        ),
        background=Color.ACCENT.value,
        width="100%"
    )
