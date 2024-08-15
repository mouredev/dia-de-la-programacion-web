import reflex as rx
from web.styles.fonts import FontWeight
from web.styles.styles import Size, SizeEM, Color


def partner(image: str, url: str, text: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                height="80px",
                width="auto",
                object_fit="contain",
                padding_right=SizeEM.BIG.value,
                alt=f"Patrocinador: {image.capitalize}"
            ),
            rx.text(
                text,
                size=Size.SMALL.value,
                color=Color.DARK.value,
                font_weight=FontWeight.BOLD
            ),
            spacing=Size.ZERO.value
        ),
        href=url,
        is_external=True
    )
