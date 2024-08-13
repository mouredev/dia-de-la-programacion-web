import reflex as rx
from web import constants
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM
from web.components.button import button
from web.components.logo import logo


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.link(
                rx.tablet_and_desktop(
                    logo(Size.BIG)
                ),
                rx.mobile_only(
                    logo(Size.MEDIUM)
                ),
                color=Color.LIGHT.value,
                href="/"
            ),
            rx.box(
                flex_grow="1",
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    button(
                        "twitch",
                        "",
                        constants.TWITCH_URL
                    ),
                    button(
                        "discord",
                        "",
                        constants.DISCORD_URL
                    ),
                    spacing=Size.DEFAULT.value
                )
            ),
            align="center",
            width="100%"
        ),
        bg=Color.DARK.value,
        position="sticky",
        padding_x=SizeEM.BIG.value,
        padding_y=SizeEM.DEFAULT.value,
        z_index="5",
        top="0",
        width="100%"
    )
