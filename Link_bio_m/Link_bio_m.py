import reflex as rx
import Link_bio_m.constants as const
import Link_bio_m.estilo.estilo as styles
from Link_bio_m.pages.index import index
from Link_bio_m.pages.courses import courses

class State(rx.State):
    """Define your app state here"""
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)