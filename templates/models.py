from django.db import models

# Create your models here.
class Servicios():
    def __init__(self,
                id,
                icono,
                nombre,
                
                resumen,
                descripcion,
                caracteristicas,
                
                precio,
                plazo_estimado
                
                ):

        self.id                 = id
        self.icono              = icono
        self.nombre             = nombre
        
        self.resumen            = resumen
        self.descripcion        = descripcion
        self.caracteristicas    = caracteristicas
        
        self.precio             = precio
        self.plazo_estimado     = plazo_estimado
        

# Use IA para generar listaServicios 
# porque me dio flojera escribir todos los servicios a mano

def listaServicios():
    return [
        Servicios(
                id              = 1,
                icono           = 'WEB',
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
        Servicios(
                id          = 2,
                icono       = 'APP',
                nombre      = 'Aplicaciones Móviles',
                resumen     = 'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.',
                descripcion     = 'Desarrollamos aplicaciones móviles nativas e híbridas para Android e iOS, conectadas a tus sistemas existentes. Nuestro equipo de desarrolladores crea experiencias de usuario intuitivas y atractivas, garantizando un rendimiento óptimo en todos los dispositivos.',
                caracteristicas = [
                    'Desarrollo de aplicaciones nativas para Android e iOS',
                    'Creación de aplicaciones híbridas que funcionan en múltiples plataformas',
                    'Integración con sistemas existentes y bases de datos',
                    'Diseño de interfaces modernas y atractivas',
                    'Soporte y mantenimiento continuo',
                ],
                precio          = '$600.000',
                plazo_estimado  = '4 a 8 semanas',
            ),
        Servicios(
                id          = 3,
                icono       = 'CLOUD',
                nombre      = 'Consultoría en la Nube',
                resumen     = 'Migración y optimización de infraestructura en la nube para tu empresa.',
                descripcion     = 'Ofrecemos servicios de consultoría en la nube para ayudar a tu empresa a migrar y optimizar su infraestructura tecnológica. Nuestro equipo de expertos en la nube te guiará en la selección de las mejores soluciones, asegurando una transición sin problemas y un rendimiento óptimo.',
                caracteristicas = [
                    'Migración de sistemas a la nube',
                    'Optimización de infraestructura en la nube',
                    'Implementación de soluciones de seguridad en la nube',
                    'Gestión y mantenimiento de servicios en la nube',
                ],
                precio          = '$500.000',
                plazo_estimado  = '4 a 8 semanas',
            ),
        Servicios(
                id          = 4,
                icono       = 'SEC',
                nombre      = 'Ciberseguridad para Pymes',
                resumen     = 'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.',
                descripcion     = 'Ofrecemos servicios de ciberseguridad para pequeñas y medianas empresas, protegiendo tus datos y los de tus clientes con las mejores prácticas de seguridad.',
                caracteristicas = [
                    'Evaluación de riesgos y vulnerabilidades',
                    'Implementación de medidas de seguridad',
                    'Capacitación en ciberseguridad',
                    'Monitoreo y respuesta a incidentes',
                ],
                precio          = '$400.000',
                plazo_estimado  = '3 a 6 semanas',
            ),
    ]

