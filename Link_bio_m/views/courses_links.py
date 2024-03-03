import reflex as rx
from Link_bio_m.routes import Route
from Link_bio_m.Componentes.link_button import Link_button
from Link_bio_m.Componentes.title import title
from Link_bio_m.estilo.estilo import Size as Size
import Link_bio_m.constants as const

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Creyente"),
        Link_button(
            "pagina Creyente",
            "Nueva descripcion de la pagina Creyente para que se den cuenta ",
            "/AvatarC.jpeg",
            const.Creyente
        ),
        
        width="100%",
        spacing=Size.DEFAULT.value,
    )   