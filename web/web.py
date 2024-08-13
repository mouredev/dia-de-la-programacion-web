import reflex as rx
import web.constants as constants
import web.utils as utils
import web.styles.styles as styles
from web.styles.colors import Color
from web.views.navbar import navbar
from web.views.header import header
from web.views.info import info
from web.views.block import block
from web.views.partners import partners
from web.views.about import about
from web.views.footer import footer


def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.vstack(
            header(),
            info(),
            rx.divider(background=Color.SECONDARY.value),
            block(
                "Charlas", "message-circle",
                "Mesas redondas formadas por referentes del sector"
            ),
            rx.divider(background=Color.SECONDARY.value),
            block(
                "Regalos", "gift",
                "Sorteo de regalos entre todos los asistentes"
            ),
            rx.divider(background=Color.SECONDARY.value),
            block(
                "Agenda", "calendar-clock",
                "Esto es todo lo que te espera"
            ),
            rx.divider(background=Color.SECONDARY.value),
            partners(),
            about(),
            footer(),
            spacing=styles.Size.ZERO.value,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={
                constants.GOOGLE_ANALYTICS_TAG}"
        ),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{constants.GOOGLE_ANALYTICS_TAG}');
"""
        ),
    ],
)

title = "Día de la Programación | 12/09/2024 | Charlas, regalos y comunidad"
description = "Ven a celebrar el día de la programación en comunidad. Mesas redondas formadas por referentes del sector y regalos para developers. 12 de septiembre desde twitch.tv/mouredev."
preview = "https://diadelaprogramacion.com/preview.jpg"

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@mouredev"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview}
    ]
)
