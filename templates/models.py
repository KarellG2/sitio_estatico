from django.db import models

# Create your models here.
class Servicios():
    def __init__(self,
                id,
                icono,
                nombre,
                resumen,
                ):

        self.id         = id
        self.icono      = icono
        self.nombre     = nombre
        self.resumen    = resumen

# Use IA para generar listaServicios y luego la listaDetalles

def listaServicios():
    return [
        Servicios(
                id          = 1,
                icono       = 'WEB',
                nombre      = 'Desarrollo de Sitios Web',
                resumen     = 'Sitios y aplicaciones web a medida',
            ),
        Servicios(
                id          = 2,
                icono       = 'APP',
                nombre      = 'Aplicaciones Móviles',
                resumen     = 'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.',
            ),
        Servicios(
                id          = 3,
                icono       = 'CLOUD',
                nombre      = 'Consultoría en la Nube',
                resumen     = 'Migración y optimización de infraestructura en la nube para tu empresa.',
            ),
        Servicios(
                id          = 4,
                icono       = 'SEC',
                nombre      = 'Ciberseguridad para Pymes',
                resumen     = 'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.',
            ),
    ]

class Detalle():
    def __init__(
        self,
        numero_Servicio: int,
        nombre,
        resumen,

        descripcion,
        caracteristicas,
        precio,

        plazo_estimado,

    ):

        self.numero_Servicio        = numero_Servicio
        self.nombre                 = nombre
        self.resumen                = resumen

        self.descripcion            = descripcion
        self.caracteristicas        = caracteristicas
        self.precio                 = precio

        self.plazo_estimado         = plazo_estimado

def listaDetalles():
    return [
        Detalle(
            numero_Servicio = 1,
            nombre          = 'Desarrollo de Sitios Web',
            resumen         = 'Sitios y aplicaciones web a medida',

            descripcion     = 'Creamos sitios web y aplicaciones web a medida, adaptadas a las necesidades de tu negocio. Desde páginas corporativas hasta plataformas complejas, nuestro equipo de expertos en desarrollo web utiliza las últimas tecnologías para garantizar un rendimiento óptimo y una experiencia de usuario excepcional.',
            caracteristicas = [
                'Diseño web responsivo y adaptativo',
                'Optimización para motores de búsqueda (SEO)',
                'Integración con redes sociales y herramientas de marketing',
                'Desarrollo de funcionalidades personalizadas según tus requerimientos',
                'Soporte y mantenimiento continuo',
            ],
            precio          = '$450.000',
            plazo_estimado  = '3 a 6 semanas',
        ),
        Detalle(
            numero_Servicio = 2,
            nombre          = 'Aplicaciones Móviles',
            resumen         = 'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.',

            descripcion     = 'Desarrollamos aplicaciones móviles nativas e híbridas para Android e iOS, diseñadas para ofrecer una experiencia de usuario fluida y atractiva. Nuestras apps se integran perfectamente con tus sistemas existentes, permitiéndote llegar a tus clientes de manera efectiva y mejorar la interacción con tu marca.',
            caracteristicas = [
                'Desarrollo de apps nativas para Android e iOS',
                'Desarrollo de apps híbridas multiplataforma',
                'Integración con APIs y servicios externos',
                'Diseño de interfaces intuitivas y atractivas',
                'Pruebas exhaustivas y soporte post-lanzamiento',
            ],
            precio          = '$890.000',
            plazo_estimado  = '6 a 10 semanas',
        ),
        Detalle(
            numero_Servicio = 3,
            nombre          = 'Consultoría en la Nube',
            resumen         = 'Migración y optimización de infraestructura en la nube para tu empresa.',

            descripcion     = 'Ofrecemos servicios de consultoría en la nube para ayudarte a migrar y optimizar tu infraestructura tecnológica. Nuestro equipo de expertos te guiará en la selección de las mejores soluciones en la nube, asegurando una transición sin problemas y un rendimiento óptimo para tus aplicaciones y datos.',
            caracteristicas = [
                'Evaluación de necesidades y planificación de migración',
                'Selección de proveedores de servicios en la nube',
                'Optimización de costos y recursos en la nube',
                'Implementación de soluciones escalables y seguras',
                'Monitoreo y soporte continuo post-migración',
            ],
            precio          = '$600.000',
            plazo_estimado  = '2 a 4 semanas',
        ),
        Detalle(
            numero_Servicio = 4,
            nombre          = 'Ciberseguridad para Pymes',
            resumen         = 'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.',

            descripcion     = 'Brindamos servicios de ciberseguridad diseñados específicamente para pequeñas y medianas empresas (Pymes). Nuestro enfoque se centra en proteger los datos de tu empresa y de tus clientes mediante la implementación de buenas prácticas de seguridad, auditorías y soluciones personalizadas que se adaptan a tus necesidades.',
            caracteristicas = [
                'Evaluación de riesgos y vulnerabilidades',
                'Implementación de medidas de seguridad efectivas',
                'Capacitación en ciberseguridad para empleados',
                'Monitoreo y respuesta ante incidentes de seguridad',
                'Cumplimiento con normativas y regulaciones de seguridad',
            ],
            precio          = '$350.000',
            plazo_estimado  = '2 a 3 semanas',
        ),
    ]