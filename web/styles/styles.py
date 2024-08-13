import reflex as rx
from enum import Enum
from .colors import Color
from .fonts import Font, FontWeight


STYLESHEETS = [
    "/css/background.css",
    "https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Roboto:wght@400;500;700&display=swap"
]

MAX_WIDTH = "1000px"


class SizeEM(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.3em"
    BIG = "2em"
    VERY_BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4"  # 1em
    MEDIUM = "6"
    BIG = "7"
    MEDIUM_VERY_BIG = "8"
    VERY_BIG = "9"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.REGULAR.value,
    "color": Color.LIGHT.value,
    "background": Color.DARK.value,
    rx.heading: {
        "font_family": Font.HEADER.value,
        "font_weight": FontWeight.BOLD.value,
    },
    rx.button: {
        "cursor": "pointer",
        "color": Color.DARK.value,
        "background": Color.ACCENT.value,
        "_hover": {
            "color": Color.LIGHT.value,
            "background": Color.SECONDARY.value
        }
    }
}

max_width_style = dict(
    padding_x=SizeEM.BIG.value,
    padding_y=SizeEM.VERY_BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
