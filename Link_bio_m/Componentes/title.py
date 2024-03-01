import reflex as rx
import Link_bio_m.estilo.estilo as style


def title(text: str) -> rx.Component:
    return rx.heading(
       text,
       style=style.title_style
    )