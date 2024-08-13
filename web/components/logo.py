import reflex as rx
from web.styles.colors import Color
from web.styles.styles import Size


def logo(size: Size, multiline=False) -> rx.Component:
    return rx.heading(
        rx.text(
            "#",
            as_="span",
            color=Color.ACCENT.value
        ),
        rx.cond(
            multiline,
            "DÍADELA\nPROGRAMACIÓN",
            "DÍADELAPROGRAMACIÓN"
        ),
        color=Color.LIGHT.value,
        as_="h1",
        size=size.value
    )
