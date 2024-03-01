import reflex as rx
import Link_bio_m.estilo.estilo as styles
from Link_bio_m.estilo.estilo import Size, EmSize
from Link_bio_m.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                border_radius=EmSize.DEFAULT.value,
            ),
            rx.text(
                featured.title,
                size=Size.VERY_SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Size.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
        href=featured.url,
        is_external=True
    )