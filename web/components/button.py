import reflex as rx
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM

LOCAL_ICONS = ["x", "discord"]


def button(icon: str, text: str, url: str, secondary=False) -> rx.Component:
    return rx.button(
        _button_icon(icon),
        text,
        size=Size.DEFAULT.value,
        background=Color.LIGHT.value if secondary else Color.ACCENT.value,
        on_click=rx.redirect(url, external=True)
    )


def _button_icon(icon: str) -> rx.Component:
    return rx.cond(
        icon in LOCAL_ICONS,
        rx.image(
            src=f"/{icon}.svg",
            width=SizeEM.MEDIUM.value,
            height=SizeEM.MEDIUM.value,
            alt=f"Botón {icon.capitalize}"
        ),
        rx.icon(
            tag="chevron-right" if icon in LOCAL_ICONS else icon,
            width=SizeEM.MEDIUM.value,
            height=SizeEM.MEDIUM.value,
            alt=f"Botón {icon.capitalize}"
        )
    ),
