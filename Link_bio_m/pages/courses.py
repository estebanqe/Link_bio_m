import reflex as rx
import Link_bio_m.utils as utils
import Link_bio_m.estilo.estilo as styles
from Link_bio_m.routes import Route
from Link_bio_m.Componentes.navbar import navbar
from Link_bio_m.Componentes.footer import footer
from Link_bio_m.views.header import header
from Link_bio_m.views.courses_links import courses_links
from Link_bio_m.views.sponsors import sponsors
from Link_bio_m.estilo.estilo import Size, EmSize


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=EmSize.BIG.value,
                padding=EmSize.BIG.value
            )
        ),
        footer()
    )