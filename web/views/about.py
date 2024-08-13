import reflex as rx
import web.styles.styles as styles
from web import constants
from web.styles.styles import Size
from web.components.button import button


def about() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.vstack(
                rx.heading(
                    "Hola, soy Brais Moure",
                    as_="h3", size=Size.BIG.value
                ),
                rx.text("Me dedico al desarrollo de software desde 2010."),
                rx.text("En 2018 comencé a divulgar contenido sobre programación en redes sociales como @mouredev, descubriendo el mayor superpoder del sector: La calidad de una comunidad que ni descansa ni cesa en su labor de compartir conocimiento y ayudar día a día."),
                rx.text.strong(
                    "Por cuarto año consecutivo, me gustaría celebrarlo como nos merecemos."),
                button(
                    "link",
                    "moure.dev",
                    constants.MOUREDEV_URL
                ),
                spacing=Size.DEFAULT.value
            ),
            rx.image(
                src="/avatar.jpg",
                width="220px",
                height="220px",
                border_radius="50%",
                alt="Avatar de Brais Moure"

            ),
            flex_direction=["column-reverse", "row"],
            spacing=Size.DEFAULT.value,
            style=styles.max_width_style
        ),
        width="100%"
    )
