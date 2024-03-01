import reflex as rx
from Link_bio_m.routes import Route
from Link_bio_m.Componentes.link_button import Link_button
from Link_bio_m.Componentes.title import title
from Link_bio_m.estilo.estilo import Size as Size
import Link_bio_m.constants as const

def index_links() -> rx.Component:
    return rx.vstack(
        title("Nueva Pagina"),
        Link_button(
            "pagina nueva",
            "Nueva descripcion de la pagina nueva ",
            "/icons/facebook.svg",
            Route.COURSES.value,
            False
        ),
        
        Link_button(
            "Facebook",
            """Madera y Melamina: Donde la Creatividad Encuentra su Hogar.""",
            "/icons/facebook.svg",
            const.FACEBOOK
        ),
        
        Link_button(
            "Instagram",
            """Diseño en Madera: Crea Tu Espacio Perfecto con Nosotros.""",
            "/icons/instagram.svg",
            const.INSTAGRAM
            ),
        Link_button(
            "Youtube",
            """Estilo Personalizado, Calidad Artesanal: Nuestro Compromiso.""",
            "/icons/youtube.svg",
            const.YOUTUBE
            ),
        Link_button(
            "Tik-Tok",
            """Tu Visión, Nuestra Creación: Experiencia en Madera y Melamina.""",
            "/icons/linkedin.svg",
            const.LINKEDLINK
            ),
            
            
        title("Cátalogo"),
        Link_button(
            "Maderas Personalisadas",
            """Madera: Transformando Ideas en Realidad.""",
            "/icons/madera1.svg",
            const.MADERA_PERSONALIZADA
        ),
        Link_button(
            "Tablas de Picar",
            """Tablas de Picar: Elegancia y Funcionalidad en Cada Corte.""",
            "/icons/madera2.svg",
            const.TABLA_PICAR
        ),
        Link_button(
            "Muebles Personalizados",
            """Hecho para Ti: Muebles que Cuentan tu Historia.""",
            "/icons/madera3.svg",
            const.MUEBLES_PERSONLAZADOS
            ),
        Link_button(
            "Amoblado de Áreas Específicas",
            """Amoblado a tu Medida, Espacios con Propósito.""",
            "/icons/madera4.svg",
            const.AMOBLADO_AREA
            ),
        
        title("Contacto"),
        Link_button(
            "WhatsApp",
            "respuesta rápida y de preferencia",
            "/icons/whatsapp.svg",
            const.WHATSAPP
        ),
        Link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
            
            
        width="100%",
        spacing=Size.DEFAULT.value,
    )   