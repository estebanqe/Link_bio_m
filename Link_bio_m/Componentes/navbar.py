import reflex as rx
import Link_bio_m.estilo.estilo as style
from Link_bio_m.routes import Route
from Link_bio_m.estilo.estilo import EmSize
from Link_bio_m.estilo.color import Color
from Link_bio_m.Componentes.ant_components import float_button


def navbar() -> rx.Component:
    return rx.hstack(            #encabezado
            rx.link(     
                rx.box(
                    rx.text("Crey",as_="span",color=Color.PRIMARY.value),
                    rx.text("ente",as_="span",color=Color.SECONDARY.value),
                    style=style.navbar_title_style
                ),
                href=Route.INDEX.value,
            ),   
            float_button(),
            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=EmSize.BIG.value,
            padding_y=EmSize.DEFAULT.value,
            z_index="999",                                  #para que siempre apareciera arriba
            top="0px"                                         #para que se mantenga la parte superior estatica
        )