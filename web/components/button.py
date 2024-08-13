import reflex as rx
from web.styles.styles import Size, SizeEM

LOCAL_ICONS = ["x", "discord"]


def button(icon: str, text: str, url: str) -> rx.Component:
    return rx.button(
        _button_icon(icon),
        text,
        size=Size.DEFAULT.value,
        on_click=rx.redirect(url, external=True)
    )


def _button_icon(icon: str) -> rx.Component:
    return rx.cond(
        icon in LOCAL_ICONS,
        rx.image(
            src=f"/{icon}.svg",
            width=SizeEM.MEDIUM.value,
            height=SizeEM.MEDIUM.value
        ),
        rx.icon(
            tag="chevron-right" if icon in LOCAL_ICONS else icon,
            width=SizeEM.MEDIUM.value,
            height=SizeEM.MEDIUM.value
        )
    ),
