import reflex as rx
from web.styles.colors import Color


def badge(text: str, icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        text,
        size="3",
        color=Color.ACCENT.value,
        background_color=Color.ACCENT_ALPHA.value,
        radius="full",
        variant="soft"
    )
