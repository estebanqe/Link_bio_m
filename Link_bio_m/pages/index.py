import reflex as rx
import Link_bio_m.utils as utils
import Link_bio_m.estilo.estilo as styles
from Link_bio_m.Componentes.navbar import navbar
from Link_bio_m.Componentes.footer import footer
from Link_bio_m.views.header import header
#from Link_bio.views.index_links import index_links
from Link_bio_m.views.index_links import index_links
from Link_bio_m.views.sponsors import sponsors
from Link_bio_m.estilo.estilo import Size,EmSize


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        
        rx.center(
            rx.vstack(
                
                header(),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=EmSize.BIG.value,
                padding=EmSize.BIG.value,
                
            )
        ),
        footer(),
        
    )