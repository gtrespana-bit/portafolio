# -*- coding: utf-8 -*-
from lib import *

# (grupo, [(servicio, entregable, prueba, precio, plazo), ...])
CATALOG = [
 ('A', 'Marketplaces, SaaS y aplicaciones web completas', [
  ('Marketplace de clasificados completo', 'Anuncios, registro, b\u00fasqueda, chat, panel de administraci\u00f3n y despliegue', 'P01 a P04', '900 a 4.500', '3 a 6 sem'),
  ('Marketplace vertical con filtros t\u00e9cnicos', 'Veh\u00edculos, maquinaria u otro nicho, con atributos propios por categor\u00eda', 'P03, P04', '1.200 a 5.000', '4 a 7 sem'),
  ('Portal inmobiliario con mapa', 'Fichas, mapa con agrupaci\u00f3n, filtros, agencias y planes', 'P02', '1.000 a 4.500', '4 a 7 sem'),
  ('Producto SaaS m\u00ednimo viable', 'Registro, planes de pago, panel de usuario y de administraci\u00f3n', 'P03, P06', '800 a 3.500', '3 a 6 sem'),
  ('Directorio de empresas o profesionales', 'Fichas con URL propia, categor\u00edas, rese\u00f1as y buscador', 'P01, P03', '400 a 1.500', '2 a 3 sem'),
  ('Adaptar un marketplace a otro pa\u00eds o sector', 'Cambio de marca, idioma, moneda, categor\u00edas y textos legales', 'P04', '600 a 2.500', '2 a 4 sem'),
  ('Chat en tiempo real para una app existente', 'Conversaciones, no le\u00eddos y avisos', 'P01', '150 a 500', '4 a 8 d\u00edas'),
  ('Sistema de rese\u00f1as y reputaci\u00f3n', 'Valoraciones, medias, denuncias y moderaci\u00f3n', 'P01', '120 a 400', '3 a 6 d\u00edas'),
  ('Favoritos, b\u00fasquedas guardadas y alertas', 'Avisos por correo o push cuando hay novedades o baja el precio', 'P01, P02', '150 a 500', '4 a 8 d\u00edas'),
  ('Convertir una web en PWA', 'Instalable, p\u00e1gina sin conexi\u00f3n y notificaciones', 'P01, P05, P07', '100 a 400', '2 a 5 d\u00edas'),
  ('Traducir una app Next.js a varios idiomas', 'Rutas por idioma, textos extra\u00eddos y selector', 'P01, P14', '120 a 450', '3 a 6 d\u00edas'),
  ('Asistente de publicaci\u00f3n con subida de fotos', 'Formulario por pasos, compresi\u00f3n y subida directa al almacenamiento', 'P01', '150 a 500', '4 a 7 d\u00edas'),
 ]),
 ('B', 'Webs y landings', [
  ('Landing de una p\u00e1gina con v\u00eddeo', 'Dise\u00f1o, textos colocados, formulario, WhatsApp y despliegue', 'P15', '80 a 350', '2 a 5 d\u00edas'),
  ('Web corporativa de 5 a 8 p\u00e1ginas', 'Inicio, servicios, proyectos, sobre nosotros, contacto y textos legales', 'P07 a P10', '250 a 900', '5 a 10 d\u00edas'),
  ('Web en varios idiomas', 'De 2 a 5 idiomas con selector y etiquetas hreflang', 'P07, P14, P15', '150 a 700', '4 a 9 d\u00edas'),
  ('Web con animaci\u00f3n avanzada o 3D', 'GSAP, animaci\u00f3n al hacer scroll, three.js o Spline', 'P10, P15', '200 a 900', '5 a 10 d\u00edas'),
  ('Web para restaurante', 'Carta con filtros, reservas, mapa y horario', 'P15', '100 a 400', '3 a 6 d\u00edas'),
  ('Web para cl\u00ednica o centro de est\u00e9tica', 'Tratamientos, equipo, opiniones y reserva', 'P14, P15', '100 a 450', '3 a 6 d\u00edas'),
  ('Web inmobiliaria sencilla', 'Rejilla de propiedades, buscador y formulario', 'P15', '150 a 600', '4 a 8 d\u00edas'),
  ('Web para empresa de reformas o construcci\u00f3n', 'Servicios, casos con antes y despu\u00e9s, zonas y presupuesto', 'P07 a P09', '300 a 1.400', '6 a 14 d\u00edas'),
  ('Web con gestor de contenidos', 'Sanity, o un panel propio que edita el contenido sin base de datos', 'P10, P14', '250 a 900', '5 a 10 d\u00edas'),
  ('Redise\u00f1o de una web existente', 'Nueva maqueta manteniendo URL y posicionamiento', 'P07 a P10', '150 a 800', '4 a 10 d\u00edas'),
  ('Web de estudio o portfolio', 'Next.js y Tailwind, con casos y formulario por pasos', 'P10', '200 a 700', '4 a 8 d\u00edas'),
  ('Pasar un dise\u00f1o a c\u00f3digo', 'HTML, Astro o Next.js fiel al dise\u00f1o que entregue el cliente', 'P10, P15', '100 a 600', '3 a 8 d\u00edas'),
  ('Blog con RSS en Astro', 'Colecci\u00f3n de art\u00edculos, categor\u00edas, RSS y datos estructurados', 'P07', '150 a 500', '3 a 6 d\u00edas'),
 ]),
 ('C', 'SEO t\u00e9cnico, local y program\u00e1tico', [
  ('Auditor\u00eda SEO t\u00e9cnica', 'Informe priorizado por impacto, con la causa y la correcci\u00f3n de cada punto', 'P01, P07', '60 a 400', '2 a 5 d\u00edas'),
  ('Correcci\u00f3n de errores SEO t\u00e9cnicos', 'Canonical, hreflang, redirecciones, sitemap, robots y t\u00edtulos duplicados', 'P07', '100 a 500', '3 a 6 d\u00edas'),
  ('Landings por ciudad y servicio', 'P\u00e1ginas generadas desde datos, con contenido propio por zona', 'P01, P03, P07', '250 a 1.500', '5 a 14 d\u00edas'),
  ('Datos estructurados', 'JSON-LD de negocio local, producto, art\u00edculo, preguntas frecuentes y migas', 'P01, P07', '50 a 250', '1 a 3 d\u00edas'),
  ('Mejora de velocidad y Core Web Vitals', 'Im\u00e1genes, fuentes, CSS cr\u00edtico y carga diferida, con informe antes y despu\u00e9s', 'P08', '80 a 400', '2 a 5 d\u00edas'),
  ('Search Console, sitemaps e IndexNow', 'Alta, verificaci\u00f3n, env\u00edo de sitemaps y aviso autom\u00e1tico de cambios', 'P04, P07', '40 a 150', '1 a 2 d\u00edas'),
  ('SEO local para un negocio', 'Estructura por zonas, datos de negocio local y contenidos de servicio', 'P07 a P09', '150 a 600', '4 a 8 d\u00edas'),
  ('SEO internacional', 'Estructura por pa\u00eds e idioma con hreflang rec\u00edproco', 'P06, P07', '120 a 500', '3 a 6 d\u00edas'),
  ('Controles SEO autom\u00e1ticos en el build', 'Scripts que detienen la publicaci\u00f3n si hay enlaces rotos o metadatos incorrectos', 'P07, P09', '120 a 450', '3 a 5 d\u00edas'),
  ('Im\u00e1genes para compartir generadas', 'Imagen Open Graph autom\u00e1tica por p\u00e1gina o por anuncio', 'P01', '50 a 200', '1 a 3 d\u00edas'),
  ('Preparaci\u00f3n para buscadores de IA', 'Archivo llms.txt, estructura clara y datos estructurados', 'P07, P08', '40 a 150', '1 a 2 d\u00edas'),
  ('Auditor\u00eda de conversi\u00f3n', 'Revisi\u00f3n del recorrido del usuario con cambios concretos', 'P01', '80 a 350', '2 a 4 d\u00edas'),
 ]),
 ('D', 'Supabase, Postgres y backend', [
  ('Dise\u00f1o de base de datos', 'Esquema, relaciones, \u00edndices y migraciones versionadas', 'P01 a P06', '90 a 600', '2 a 6 d\u00edas'),
  ('Seguridad por filas en Supabase', 'Pol\u00edticas RLS por tabla, con pruebas de acceso', 'P01 a P06', '100 a 700', '2 a 6 d\u00edas'),
  ('Registro, acceso y roles', 'Correo, enlaces de acceso, recuperaci\u00f3n y permisos', 'P01, P05', '80 a 350', '2 a 4 d\u00edas'),
  ('Almacenamiento de archivos', 'Buckets privados, URL firmadas y subida directa a Cloudflare R2', 'P01, P03', '80 a 350', '2 a 4 d\u00edas'),
  ('Funciones SQL y triggers', 'L\u00f3gica en la base de datos, llamadas RPC y contadores', 'P01 a P04', '80 a 500', '2 a 5 d\u00edas'),
  ('B\u00fasqueda y filtros avanzados', 'Texto completo y atributos en JSONB con \u00edndices GIN', 'P01, P03', '100 a 400', '2 a 5 d\u00edas'),
  ('Cambios de esquema sin parada', 'Renombrados con triggers de sincronizaci\u00f3n y verificaci\u00f3n', 'P03', '150 a 600', '3 a 6 d\u00edas'),
  ('L\u00edmite de peticiones', 'At\u00f3mico en Postgres o distribuido con Redis', 'P01, P06', '80 a 300', '1 a 3 d\u00edas'),
  ('API con Next.js', 'Rutas de servidor con validaci\u00f3n y control de acceso', 'P01 a P04', '100 a 800', '2 a 8 d\u00edas'),
  ('API con FastAPI', 'Servicio en Python con documentaci\u00f3n autom\u00e1tica', 'P06, P11, P12', '120 a 900', '3 a 8 d\u00edas'),
  ('Tareas programadas', 'Procesos diarios o semanales: caducidades, res\u00famenes y limpieza', 'P01, P03', '80 a 300', '1 a 3 d\u00edas'),
  ('Correos transaccionales', 'Plantillas y env\u00edo con Resend o SMTP, con baja en un clic', 'P01, P02', '80 a 350', '2 a 4 d\u00edas'),
  ('Notificaciones push web', 'Suscripci\u00f3n, env\u00edo y preferencias del usuario', 'P01', '80 a 300', '2 a 4 d\u00edas'),
  ('Tests automatizados', 'Jest o tests de Node, y pruebas de base de datos sin servidor', 'P01 a P04', '100 a 600', '2 a 6 d\u00edas'),
  ('Integraci\u00f3n continua', 'GitHub Actions con tests y build en cada cambio', 'P01', '50 a 200', '1 a 2 d\u00edas'),
  ('Monitorizaci\u00f3n de errores', 'Sentry o un monitor propio con aviso', 'P01, P02', '50 a 250', '1 a 3 d\u00edas'),
 ]),
 ('E', 'Pagos y monetizaci\u00f3n', [
  ('Pago \u00fanico con Stripe', 'P\u00e1gina de pago, confirmaci\u00f3n por webhook y registro del pedido', 'P03', '80 a 250', '2 a 3 d\u00edas'),
  ('Suscripciones con Stripe', 'Planes mensual y anual, portal de cliente y webhooks', 'P03', '150 a 650', '3 a 7 d\u00edas'),
  ('Impagos, cupones y pruebas gratuitas', 'Reintentos, periodo de gracia, c\u00f3digos de descuento y planes de regalo', 'P03', '120 a 450', '3 a 5 d\u00edas'),
  ('Cr\u00e9ditos y anuncios destacados', 'Saldo, compra, consumo e historial', 'P01, P03', '150 a 500', '3 a 6 d\u00edas'),
  ('Cobro manual con justificante', 'Transferencia, Pago M\u00f3vil, Bizum o Binance, con aprobaci\u00f3n en el panel', 'P01, P02', '150 a 500', '3 a 6 d\u00edas'),
  ('Lectura de justificantes con OCR', 'Extracci\u00f3n de importe y referencia, con bloqueo de duplicados', 'P02', '150 a 500', '3 a 6 d\u00edas'),
  ('L\u00edmites por plan', 'Funciones y cuotas distintas seg\u00fan el plan contratado', 'P02, P03', '120 a 450', '2 a 5 d\u00edas'),
 ]),
 ('F', 'Paneles, ERP, CRM y herramientas internas', [
  ('Panel de administraci\u00f3n a medida', 'Indicadores, listados, moderaci\u00f3n, usuarios y auditor\u00eda', 'P01', '300 a 1.500', '1 a 3 sem'),
  ('ERP a medida para una pyme', 'M\u00f3dulos de operaci\u00f3n, clientes, cuentas e informes', 'P05', '800 a 4.000', '3 a 7 sem'),
  ('CRM sencillo', 'Contactos, estados, seguimiento y recordatorios', 'P05, P06', '300 a 1.200', '1 a 3 sem'),
  ('Facturaci\u00f3n y contabilidad b\u00e1sica', 'Facturas, gastos e impuestos, adaptado a Espa\u00f1a', 'P05', '300 a 1.500', '1 a 3 sem'),
  ('Calculadoras fiscales', 'Transmisiones, matriculaci\u00f3n, IVA u otro impuesto con sus reglas', 'P03, P05', '100 a 500', '2 a 5 d\u00edas'),
  ('Roles y permisos', 'Perfiles como propietario, gerente, comercial y contable', 'P05', '100 a 450', '2 a 5 d\u00edas'),
  ('Panel de indicadores y anal\u00edtica propia', 'Visitas, embudo y rendimiento, sin depender de terceros', 'P02, P03', '150 a 700', '3 a 7 d\u00edas'),
  ('Importaci\u00f3n y exportaci\u00f3n de datos', 'Carga masiva por CSV y exportaci\u00f3n a CSV o JSON', 'P01, P03', '60 a 250', '1 a 3 d\u00edas'),
  ('Bot de Telegram', 'Aprobar, rechazar o recibir avisos desde el m\u00f3vil', 'P01, P11', '80 a 300', '2 a 4 d\u00edas'),
  ('Generador de documentos', 'Contratos, presupuestos o informes en PDF desde la aplicaci\u00f3n', 'P03, P06', '100 a 450', '2 a 5 d\u00edas'),
  ('Calculadora o valorador para captar contactos', 'Herramienta p\u00fablica que da un resultado y recoge el contacto', 'P02, P03, P04', '120 a 500', '3 a 6 d\u00edas'),
  ('Moderaci\u00f3n y antifraude', 'Reglas autom\u00e1ticas, cola de revisi\u00f3n y verificaci\u00f3n de identidad', 'P01', '150 a 600', '3 a 7 d\u00edas'),
 ]),
 ('G', 'Inteligencia artificial', [
  ('Integrar un modelo de lenguaje en una app', 'Gemini, Groq u otra API compatible, con modelo de reserva', 'P02, P06, P12', '120 a 600', '3 a 6 d\u00edas'),
  ('Chatbot con conocimiento propio', 'Respuestas basadas en tus documentos o tu c\u00f3digo (RAG)', 'P12', '200 a 900', '4 a 9 d\u00edas'),
  ('Agente con herramientas', 'Ejecuta acciones y pide aprobaci\u00f3n antes de las sensibles', 'P12', '250 a 1.200', '5 a 12 d\u00edas'),
  ('Asistente privado con modelos locales', 'Ollama en tu equipo, sin enviar datos fuera', 'P12', '150 a 600', '3 a 7 d\u00edas'),
  ('Mejora autom\u00e1tica de textos', 'Bot\u00f3n que reescribe descripciones de anuncios o productos', 'P02', '100 a 350', '2 a 4 d\u00edas'),
  ('An\u00e1lisis de im\u00e1genes', 'Lectura de capturas o fotos con modelos de visi\u00f3n', 'P12', '120 a 500', '3 a 6 d\u00edas'),
  ('Tareas aut\u00f3nomas programadas', 'El asistente ejecuta trabajos por s\u00ed solo a una hora fijada', 'P12', '150 a 600', '3 a 7 d\u00edas'),
 ]),
 ('H', 'Python, extracci\u00f3n de datos e informes', [
  ('Scraper web a medida', 'Script que extrae y entrega los datos en CSV, JSON o base de datos', 'P05', '70 a 500', '2 a 6 d\u00edas'),
  ('Seguimiento de precios de mercado', 'Captura peri\u00f3dica, hist\u00f3rico y comparaci\u00f3n', 'P05', '150 a 700', '4 a 8 d\u00edas'),
  ('Modelo de precios', 'Regresi\u00f3n sobre datos de mercado para estimar valor', 'P05', '150 a 600', '3 a 7 d\u00edas'),
  ('Informes y PDF con Python', 'Documento maquetado con tablas y gr\u00e1ficos, generado desde datos', 'P13', '80 a 450', '2 a 5 d\u00edas'),
  ('Automatizaci\u00f3n con scripts', 'Tareas repetitivas con archivos, hojas de c\u00e1lculo o API', 'P05, P07', '50 a 300', '1 a 4 d\u00edas'),
  ('Tratamiento de fotos por lotes', 'Borrado de metadatos, ocultaci\u00f3n de matr\u00edculas y conversi\u00f3n', 'P05', '80 a 300', '2 a 4 d\u00edas'),
 ]),
 ('I', 'V\u00eddeo, visi\u00f3n artificial y escritorio', [
  ('Aplicaci\u00f3n de videovigilancia', 'Directo, grabaci\u00f3n y avisos para c\u00e1maras IP', 'P11', '150 a 900', '4 a 14 d\u00edas'),
  ('Detecci\u00f3n de movimiento u objetos', 'OpenCV o YOLO, con zonas y sensibilidad', 'P11', '150 a 700', '4 a 9 d\u00edas'),
  ('Conexi\u00f3n con c\u00e1maras', 'RTSP, ONVIF, descubrimiento en red y control de movimiento', 'P11', '100 a 450', '2 a 6 d\u00edas'),
  ('Aplicaci\u00f3n de escritorio para Windows', 'Python con interfaz web, empaquetada con instalador', 'P11, P12', '150 a 800', '4 a 10 d\u00edas'),
  ('Avisos por varios canales', 'Telegram, Discord, ntfy, Pushover, correo o webhook', 'P11', '60 a 250', '1 a 3 d\u00edas'),
 ]),
 ('J', 'Auditor\u00eda y consultor\u00eda t\u00e9cnica', [
  ('Auditor\u00eda de seguridad de una app con Supabase', 'Revisi\u00f3n de pol\u00edticas, claves, almacenamiento y rutas, con correcciones', 'P02, P03', '150 a 700', '3 a 7 d\u00edas'),
  ('Revisi\u00f3n de c\u00f3digo y arquitectura', 'Informe con riesgos y mejoras ordenadas por prioridad', 'P01 a P04', '80 a 400', '2 a 5 d\u00edas'),
  ('Revisi\u00f3n previa al lanzamiento', 'Lista de comprobaci\u00f3n de seguridad, SEO, legal y rendimiento', 'P02', '100 a 450', '2 a 5 d\u00edas'),
  ('Estimaci\u00f3n de alcance y coste de un proyecto', 'Desglose por m\u00f3dulos, horas y fases', 'P01', '60 a 250', '1 a 3 d\u00edas'),
  ('Documentaci\u00f3n t\u00e9cnica', 'README, manual de uso y gu\u00eda de despliegue', 'P05', '60 a 350', '2 a 4 d\u00edas'),
 ]),
 ('K', 'Negocio y finanzas', [
  ('Plan de negocio completo', 'Documento maquetado en PDF con mercado, operaciones y finanzas', 'P13', '150 a 1.600', '5 a 14 d\u00edas'),
  ('Modelo financiero', 'Resultados a 5 a\u00f1os, VAN, TIR, tesorer\u00eda y sensibilidad', 'P13', '120 a 700', '3 a 7 d\u00edas'),
  ('Estudio de mercado local', 'Competencia, precios y demanda en una zona', 'P05, P13', '100 a 500', '3 a 6 d\u00edas'),
  ('Estructura de costes y tarifas', 'Coste real por servicio, margen y precio de venta', 'P13', '100 a 450', '2 a 5 d\u00edas'),
  ('Presentaci\u00f3n para banco o inversores', 'Resumen visual del plan en PDF', 'P05, P13', '100 a 400', '2 a 5 d\u00edas'),
 ]),
 ('L', 'Construcci\u00f3n y reformas', [
  ('Presupuesto de obra o reforma', 'Partidas, mediciones y precios, listo para entregar al cliente', 'P06, P13', '60 a 650', '2 a 7 d\u00edas'),
  ('Base de precios para un pa\u00eds', 'Recursos y partidas con precio de referencia, rango y fuente', 'P06', '150 a 900', '4 a 10 d\u00edas'),
  ('Plantillas de presupuesto', 'Modelos reutilizables por tipo de obra: ba\u00f1o, cocina, integral', 'P13', '50 a 250', '1 a 3 d\u00edas'),
  ('Web y SEO para empresa de reformas', 'Web por zonas y servicios con casos de antes y despu\u00e9s', 'P07 a P09', '400 a 2.000', '7 a 20 d\u00edas'),
  ('Asesor\u00eda para montar una empresa de reformas', 'Costes, coste laboral, tarifas y tesorer\u00eda', 'P13', '80 a 400', '2 a 5 d\u00edas'),
  ('Cronograma de obra', 'Fases, duraciones y dependencias', 'P05', '50 a 250', '1 a 3 d\u00edas'),
  ('Software de presupuestos a medida', 'Editor por capítulos y partidas con costes, márgenes y PDF con tu marca', 'P06', '600 a 3.500', '2 a 5 sem'),
  ('Importación y exportación BC3 o Excel', 'Lectura de bancos de precios y presupuestos en FIEBDC-3 o Excel, y exportación', 'P06', '150 a 700', '3 a 8 días'),
  ('Medición sobre planos', 'Herramienta web para medir longitudes, áreas y conteos, con exportación a DXF y CSV', 'P06', '250 a 1.200', '5 a 12 días'),
 ]),
 ('M', 'Contenido y marketing', [
  ('Art\u00edculos de blog con SEO', 'En espa\u00f1ol o ingl\u00e9s: reformas, motor, inmobiliario. Precio por art\u00edculo', 'P01, P07', '30 a 120', '1 a 3 d\u00edas'),
  ('Creatividades para Facebook', 'Flyers en serie generados desde una plantilla', 'P01, P07', '40 a 200', '1 a 3 d\u00edas'),
  ('Secuencia de correos', 'Bienvenida, consejos y recuperaci\u00f3n de usuarios inactivos', 'P06', '80 a 350', '2 a 4 d\u00edas'),
  ('Textos para la web de un negocio local', 'Inicio, servicios, sobre nosotros y preguntas frecuentes', 'P07 a P09', '50 a 300', '1 a 4 d\u00edas'),
  ('Generador de anuncios para portales', 'Texto del anuncio a partir de la ficha del producto', 'P05', '80 a 300', '2 a 4 d\u00edas'),
 ]),
 ('N', 'Mantenimiento y despliegue', [
  ('Correcci\u00f3n de errores en Next.js o React', 'Diagn\u00f3stico, arreglo y explicaci\u00f3n de la causa', 'P01 a P05', '30 a 300', '1 a 4 d\u00edas'),
  ('Despliegue en Vercel', 'Proyecto, dominio, variables de entorno y tareas programadas', 'P01 a P09', '30 a 150', '1 a 2 d\u00edas'),
  ('Migraci\u00f3n de una web a Astro o Next.js', 'Mismo contenido y URL, con m\u00e1s velocidad', 'P07 a P09', '200 a 1.200', '5 a 12 d\u00edas'),
  ('Actualizaci\u00f3n de versiones', 'Subida de Next.js, React y dependencias con pruebas', 'P01, P05', '80 a 400', '2 a 5 d\u00edas'),
  ('Mantenimiento mensual', 'Correcciones, cambios peque\u00f1os y vigilancia. Precio por mes', 'P01 a P06', '100 a 400', 'mensual'),
  ('Optimizaci\u00f3n de im\u00e1genes y v\u00eddeo', 'WebP, AVIF, webm, tama\u00f1os y carga diferida', 'P07, P14', '40 a 200', '1 a 3 d\u00edas'),
 ]),
]

COUNT = sum(len(g[2]) for g in CATALOG)


def stack_section():
    s = section('03', 'Tecnolog\u00eda que has usado de verdad',
                'Cada fila est\u00e1 respaldada por c\u00f3digo en al menos un repositorio. Es la lista que puedes defender si un comprador te pregunta.')
    s.append(table([
        ['\u00c1rea', 'Tecnolog\u00eda', 'D\u00f3nde'],
        ['Frameworks web', 'Next.js 14, 15 y 16 (App Router), React 18 y 19, Astro 5 y 6, Vite 8', 'P01 a P10'],
        ['Lenguajes', 'TypeScript, JavaScript, Python, SQL (PL/pgSQL), HTML y CSS', 'Todos'],
        ['Estilos y animaci\u00f3n', 'Tailwind CSS 3 y 4, componentes al estilo shadcn con Radix, Framer Motion, GSAP con ScrollTrigger, Lenis', 'P01 a P05, P10, P15'],
        ['3D', 'three.js, React Three Fiber, drei, Spline', 'P10, P15'],
        ['Base de datos', 'PostgreSQL en Supabase: RLS, funciones, triggers, JSONB con \u00edndices GIN, texto completo, Realtime, PGlite en tests, Alembic', 'P01 a P06'],
        ['Autenticaci\u00f3n y permisos', 'Supabase Auth, roles, verificaci\u00f3n de identidad, acceso con PIN', 'P01 a P05, P12'],
        ['Archivos', 'Supabase Storage con URL firmadas, Cloudflare R2 con subida prefirmada, sharp', 'P01 a P03'],
        ['Pagos', 'Stripe (suscripciones, portal, webhooks, impagos, cupones), cobro manual con justificante y OCR', 'P02, P03, P06'],
        ['Mapas', 'Leaflet con agrupaci\u00f3n de marcadores', 'P02, P05'],
        ['Correo y avisos', 'Resend, SMTP, web-push, bots de Telegram, ntfy, Discord, Pushover', 'P01, P02, P06, P11'],
        ['SEO', 'Sitemaps, datos estructurados, hreflang, canonical, IndexNow, im\u00e1genes OG, RSS, llms.txt, Search Console', 'P01 a P09'],
        ['Idiomas', 'next-intl, rutas por idioma en Astro, traducciones en JSON', 'P01, P06 a P08, P14'],
        ['Inteligencia artificial', 'Gemini, Groq, Ollama y otros ocho proveedores; agentes con herramientas, RAG, visi\u00f3n; OCR con tesseract.js', 'P02, P06, P12'],
        ['Python', 'FastAPI, SQLAlchemy, Alembic, Jinja2, pytest, OpenCV, ffmpeg, YOLO, ReportLab, pypdf, openpyxl, svglib, scrapers, regresión, pywebview, PyInstaller, Inno Setup', 'P05, P06, P11 a P13'],
        ['Calidad', 'Jest, tests de Node, pytest, GitHub Actions, pip-audit, búsqueda de secretos, Sentry, comprobaciones propias en el build, informes Lighthouse', 'P01 a P09'],
        ['Despliegue', 'Vercel (tareas programadas, cabeceras, redirecciones, dos aplicaciones por dominio), PWA con service worker', 'Todos'],
        ['Anal\u00edtica', 'Google Analytics 4 con modo de consentimiento, anal\u00edtica propia an\u00f3nima, embudos', 'P01 a P03'],
        ['Gestor de contenidos', 'Sanity; panel propio sobre la API de GitHub', 'P10, P14'],
        ['Formatos de la construcción', 'BC3 (FIEBDC-3), descompuestos en Excel, DXF para CAD, PDF de presupuesto', 'P06'],
    ], [19, 60, 21], first_bold=True))
    s += h2('Lo que no aparece en tus repositorios', toc=False)
    s.append(P('Conviene saberlo para no abrir gigs que luego no puedas respaldar con un ejemplo. No he encontrado c\u00f3digo de nada de esto:'))
    s += bullets([
        'Aplicaciones m\u00f3viles nativas (React Native, Flutter, Swift, Kotlin). S\u00ed tienes PWA instalables.',
        'WordPress, Shopify, Webflow, Wix u otros constructores. Es la subcategor\u00eda con m\u00e1s demanda en Fiverr y no tienes muestras.',
        'PHP, Laravel, Vue, Angular, .NET o Java.',
        'Docker, Kubernetes, AWS o servidores propios. Todo est\u00e1 en Vercel y Supabase.',
        'Archivos de dise\u00f1o (Figma). Tus dise\u00f1os est\u00e1n hechos directamente en c\u00f3digo.',
        'Tests de extremo a extremo con Playwright o Cypress.',
    ])
    s.append(note('En tus repositorios se ve que trabajas con asistentes de inteligencia artificial: ramas y pull requests creados por agentes, y documentos de revisi\u00f3n hechos con IA. No es un problema, es una forma de trabajar cada vez m\u00e1s habitual y te permite entregar r\u00e1pido. Pero tenlo en cuenta al describirte: lo que vendes es criterio de producto, direcci\u00f3n y resultado, no "diez a\u00f1os picando c\u00f3digo". Y aseg\u00farate de poder explicar y mantener lo que entregas.', title='Sobre el desarrollo asistido por IA'))
    return s


def build():
    s = section('05', 'Cat\u00e1logo completo de servicios',
                '%d servicios que puedes ofrecer, cada uno con la prueba que lo respalda. La columna "Prueba" remite a las fichas de la secci\u00f3n 04.' % COUNT)
    s.append(P('Los precios est\u00e1n en d\u00f3lares, que es la moneda de Fiverr, y van del paquete m\u00e1s sencillo al m\u00e1s completo. Son orientativos. Un servicio puede venderse como gig propio, como paquete dentro de otro gig o como extra.'))
    n = 0
    for code, title, rows in CATALOG:
        s += [CondPageBreak(60 * mm), H2('%s. %s' % (code, title), True)]
        data = [['N.\u00ba', 'Servicio', 'Qu\u00e9 entregas', 'Prueba', 'Precio (USD)', 'Plazo']]
        for r in rows:
            n += 1
            data.append(['%03d' % n, r[0], r[1], r[2], r[3], r[4]])
        s.append(table(data, [6, 25, 33, 11, 14, 11], mono_cols=(0,), first_bold=False))
    return s
