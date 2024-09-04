import reflex as rx
from web.styles import styles
from web.styles.colors import Color
from web.styles.fonts import Font, FontWeight
from web.styles.styles import Size, SizeEM
from web.components.badge import badge


class Speaker:
    def __init__(self, name: str, description: str, handler: str, url: str, mpi: str = ""):
        self.name = name
        self.description = description
        self.handler = handler
        self.url = url
        self.mpi = mpi


def speakers(text: str, icon: str, title: str) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                badge(text, icon),
                rx.heading(
                    title,
                    as_="h3", size=Size.BIG.value
                ),
                spacing=SizeEM.SMALL.value,
            ),
            _speakers_event(
                "lock-keyhole",
                "Ciberseguridad y hacking",
                [
                    Speaker(
                        "Chema Alonso",
                        "CDO de Telefónica | Doctor en Seguridad Informática",
                        "chemaalonso",
                        "https://elladodelmal.com",
                        "https://mypublicinbox.com/ChemaAlonso"
                    ),
                    Speaker(
                        "Daniela Maissi",
                        "Security  Researcher OWASP Foundation | Prev. EC-COUNCIL",
                        "blindma1den",
                        "https://danielamaissi.tech",
                        "https://mypublicinbox.com/blindma1den"
                    ),
                    Speaker(
                        "Marcelo Vázquez",
                        "Hack4u CEO & Founder | Creador de contenido sobre hacking",
                        "s4vitar",
                        "https://youtube.com/s4vitar",
                        "https://mypublicinbox.com/S4vitar"
                    )
                ]
            ),
            _speakers_event(
                "gamepad",
                "Desarrollo de videojuegos",
                [
                    Speaker(
                        "Alva Majo",
                        "Indie gamedev | Majorariatto",
                        "5ro4",
                        "https://alvamajo.com"
                    ),
                    Speaker(
                        "Rocío Tomé",
                        "Gamedev | Patattie Games",
                        "rothiotome",
                        "https://linktr.ee/rothiotome"
                    ),
                    Speaker(
                        "Samuel Molina",
                        "Senior Game Content Designer | CloudImperium",
                        "fukuy",
                        "https://samuelmolina.site"
                    )
                ]
            ),
            _speakers_event(
                "trending-up",
                "De Junior a Senior",
                [
                    Speaker(
                        "Afor Digital",
                        "Frontend developer | CEO de Afordin",
                        "afor_digital",
                        "https://twitch.tv/afor_digital"
                    ),
                    Speaker(
                        "Aris Guimerá",
                        "Mobile developer | Github Star & Microsoft MVP",
                        "aristidevs",
                        "https://aristi.dev"
                    ),
                    Speaker(
                        "Carlos Azaustre",
                        "SWE + Profesor en Universidad Europea | Microsoft MVP & GDE",
                        "carlosazaustre",
                        "https://carlosazaustre.es",
                        "https://mypublicinbox.com/carlosazaustre"
                    )
                ]
            ),
            _speakers_event(
                "beer",
                "Más allá del código",
                [
                    Speaker(
                        "Héctor de León",
                        "Programador y creador de contenido | Microsoft MVP",
                        "powerhdeleon",
                        "https://hdeleon.net"
                    ),
                    Speaker(
                        "Nicolás Schürmann",
                        "Programador y creador de contenido | Hola Mundo",
                        "_nasch_",
                        "https://holamundo.io"
                    ),
                    Speaker(
                        "Brais Moure",
                        "Programador y creador de contenido | Github Star & Microsoft MVP",
                        "mouredev",
                        "https://moure.dev",
                        "https://mypublicinbox.com/mouredev"
                    )
                ]
            ),
            _speakers_event(
                "handshake",
                "Los beneficios de una comunidad",
                [
                    Speaker(
                        "Comunidad Discord",
                        "Miembros destacados de nuestra comunidad",
                        "discord",
                        "https://discord.gg/mouredev"
                    ),
                ]
            ),
            rx.text("Más anuncios próximamente..."),
            spacing=Size.BIG.value,
            style=styles.max_width_style
        ),
        width="100%"
    )


def _speakers_event(icon: str, title: str, speakers: list[Speaker]) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(
                icon,
                height=SizeEM.BIG.value,
                width="auto"
            ),
            rx.text(
                title,
                size=Size.BIG.value
            ),
            spacing=SizeEM.DEFAULT.value,
            align="center"
        ),
        rx.flex(
            *[
                _speaker(speaker)
                for speaker in speakers
            ],
            spacing=Size.BIG.value,
            flex_direction=["column", "column", "row"],
            width="100%",
        ),
        background_color=Color.ACCENT_ALPHA.value,
        spacing=Size.MEDIUM.value,
        padding="var(--space-5)",
        border_radius="var(--radius-5)",
        width="100%"
    )


def _speaker(speaker: Speaker) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=f"/speakers/{speaker.handler}.png",
            width=rx.breakpoints(initial="100px", sm="150px"),
            height=rx.breakpoints(initial="100px", sm="150px"),
            border_radius="50%",
            background=Color.ACCENT.value,
            alt=f"Avatar de {speaker.name}",
            margin_bottom=SizeEM.DEFAULT.value
        ),
        rx.text(
            speaker.name,
            font_family=Font.DEFAULT.value,
            font_weight=FontWeight.BOLD.value,
            size=Size.MEDIUM_VERY_BIG.value
        ),
        rx.text(speaker.description),
        rx.hstack(
            rx.link(
                f"@{speaker.handler}",
                href=speaker.url,
                color=Color.ACCENT.value,
                is_external=True
            ),
            rx.cond(
                speaker.mpi != "",
                rx.tooltip(
                    rx.image(
                        "/mpi.png",
                        width="1.6em",
                        height="1.6em",
                        on_click=rx.redirect(
                            path=speaker.mpi,
                            external=True
                        ),
                        cursor="pointer"
                    ),
                    content=f"""
Contacta directamente a @{speaker.handler} a través de MyPublicInbox: {speaker.mpi}
"""
                )
            ),
            align="center"
        ),
        width="100%",
        spacing=Size.ZERO.value
    )
