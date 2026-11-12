# -*- coding: utf-8 -*-
from lib import *

M = lambda t: '<font name="Mono">%s</font>' % t


def proj(tag, name, what, facts, feats, proves, show, extra=None):
    s = h2(name, tag=tag)
    s.append(P(what))
    s.append(kv(facts))
    if feats:
        s.append(h3('Lo que hay construido'))
        s += bullets(feats)
    s.append(h3('Lo que demuestra ante un comprador'))
    s.append(P(proves))
    s.append(kv([('En Fiverr', show)]))
    if extra:
        s.append(extra)
    return s


def build():
    s = section('04', 'Los proyectos, uno a uno',
                'Diecis\u00e9is fichas. Las cifras est\u00e1n contadas sobre el c\u00f3digo de cada repositorio el 11 de noviembre de 2026.')
    s.append(table([
        ['Proyecto', 'P\u00e1ginas', 'Rutas API', 'Componentes', 'L\u00edneas TS', 'SQL (l\u00edneas)', 'Tablas', 'Tests'],
        ['VendeT (clasificados)', '32', '73', '40', '31.027', '3.729', '21', '24'],
        ['Venezuela Inmuebles', '48', '72', '62', '54.597', '8.151', '36', '39'],
        ['CamperOcasi\u00f3n', '48', '112', '68', '64.304', '14.002', '31', '86'],
        ['MaquinariaOcasi\u00f3n', '47', '107', '54', '59.184', '17.306', '34', '72'],
    ], [26, 9, 10, 12, 11, 12, 9, 9], first_bold=True, mono_cols=(1, 2, 3, 4, 5, 6, 7)))
    s.append(P('P\u00e1ginas y rutas son archivos <font name="Mono">page.tsx</font> y <font name="Mono">route.ts</font>. MaquinariaOcasi\u00f3n comparte motor con CamperOcasi\u00f3n: gran parte de su c\u00f3digo es el mismo, adaptado.', 'small'))

    # P01
    s += proj('P01', 'VendeT, marketplace de clasificados para Venezuela',
        'Plataforma de compraventa entre particulares, pensada para m\u00f3vil y para un pa\u00eds donde no se puede cobrar con tarjeta. Es tu proyecto con m\u00e1s historial: 705 commits.',
        [('Repositorio', M('Marketplace-vzla')),
         ('Dominio', 'vendet.online'),
         ('Periodo', '28 abr a 1 nov 2026, 705 commits'),
         ('Stack', 'Next.js 16, React 18, TypeScript, Tailwind, Supabase (Auth, Postgres, RLS, Storage, Realtime), Cloudflare R2, next-intl, web-push, Resend, Sentry, GA4, Jest, GitHub Actions'),
         ('Tama\u00f1o', '32 p\u00e1ginas, 73 rutas de API, 40 componentes, 38 m\u00f3dulos de librer\u00eda, 31.027 l\u00edneas TS, 44 archivos SQL, 21 tablas, 78 pol\u00edticas, 46 funciones SQL, 24 archivos de test, 19 art\u00edculos de blog, 4 tareas programadas')],
        ['Publicaci\u00f3n en pasos que empieza por las fotos, con subida directa a Cloudflare R2 mediante URL prefirmadas.',
         'Filtros, b\u00fasqueda de texto completo, favoritos, b\u00fasquedas guardadas con aviso push, alertas de bajada de precio y resumen semanal por correo.',
         'Chat en tiempo real entre comprador y vendedor, rese\u00f1as y verificaci\u00f3n de identidad.',
         'Cr\u00e9ditos y anuncios destacados, pagados por transferencia y aprobados con justificante.',
         'Moderaci\u00f3n autom\u00e1tica y un bot de Telegram para aprobar o rechazar anuncios desde el m\u00f3vil.',
         'Panel de administraci\u00f3n de 11 secciones: indicadores, moderaci\u00f3n, usuarios, transacciones, auditor\u00eda, categor\u00edas, banners, exportaci\u00f3n CSV y JSON, estado del sistema.',
         'L\u00edmite de peticiones at\u00f3mico en base de datos, tasa oficial del BCV, espa\u00f1ol e ingl\u00e9s, instalable como PWA.',
         'SEO: 330 landings de ciudad y ciudad por categor\u00eda, sitemaps, datos estructurados (Product, ItemList, FAQPage), im\u00e1genes OG generadas y an\u00e1lisis SEO y de conversi\u00f3n documentados.',
         'Integraci\u00f3n continua con GitHub Actions: tests y build en cada cambio.'],
        'Que sabes construir un marketplace entero y mantenerlo durante meses. Tu propio documento de estimaci\u00f3n lo valora entre 1.500 y 2.000 horas de agencia. Es la prueba principal de los gigs 01, 04 y 07.',
        '<b>Ense\u00f1ar.</b> Capturas de la home, el asistente de publicaci\u00f3n, el chat y el panel de administraci\u00f3n. Es tu caso estrella.')

    # P02
    s += proj('P02', 'Venezuela Inmuebles, portal inmobiliario',
        'Portal de venta y alquiler de inmuebles con planes de pago para profesionales y agencias.',
        [('Repositorio', M('vendet-inmuebles')),
         ('Dominio', 'venezuela-inmuebles.online'),
         ('Periodo', '20 jul a 2 nov 2026, 315 commits'),
         ('Stack', 'Next.js 15, TypeScript, Supabase, Leaflet con agrupaci\u00f3n de marcadores, tesseract.js y sharp, Gemini, Sentry, PGlite para tests'),
         ('Tama\u00f1o', '48 p\u00e1ginas, 72 rutas de API, 62 componentes, 81 m\u00f3dulos de librer\u00eda, 54.597 l\u00edneas TS, 8.151 l\u00edneas SQL, 36 tablas, 96 pol\u00edticas, 70 funciones SQL, 39 tests de Node')],
        ['Mapa interactivo con agrupaci\u00f3n de marcadores y b\u00fasqueda por zona.',
         'Planes Gratuita, Profesional (9,99 $) y Agencia (39,99 $), con miembros, invitaciones y cartera por agencia.',
         'Lectura autom\u00e1tica de justificantes de pago (Pago M\u00f3vil y Binance) con OCR en servidor, validaci\u00f3n provisional y bloqueo contra reutilizaci\u00f3n.',
         'Bot\u00f3n que mejora la descripci\u00f3n del anuncio con Gemini, con modelos alternativos si el primero falla.',
         'Agenda de visitas, comparador de inmuebles y estimador financiero (d\u00f3lares y bol\u00edvares, financiaci\u00f3n, rentabilidad).',
         'Alertas de b\u00fasquedas guardadas, res\u00famenes por correo con baja en un clic y escaparate propio por vendedor.',
         'Monitor interno de errores, anal\u00edtica de embudo y p\u00e1ginas SEO por operaci\u00f3n, estado y ciudad.',
         'Auditor\u00eda de seguridad y de lanzamiento documentada, con sus correcciones por bloques.'],
        'Mapas, inteligencia artificial y OCR aplicados a un problema real de cobro. Tests de base de datos que se ejecutan sin servidor. Apoya los gigs 01, 04, 07 y 10.',
        '<b>Ense\u00f1ar.</b> El mapa, la ficha de inmueble, los planes y el panel de agencia.')

    # P03
    s += proj('P03', 'CamperOcasi\u00f3n, marketplace de campers y autocaravanas (Espa\u00f1a)',
        'Vertical para el mercado espa\u00f1ol, en euros, con suscripci\u00f3n profesional cobrada por Stripe. Es el proyecto m\u00e1s grande por volumen de c\u00f3digo y de pruebas.',
        [('Repositorio', M('camperocasion')),
         ('Dominio', 'camperocasion.online'),
         ('Periodo', '15 sep a 4 nov 2026, 154 commits'),
         ('Stack', 'Next.js, TypeScript, Supabase, Stripe 22, Node 24, Vercel con 9 tareas programadas'),
         ('Tama\u00f1o', '48 p\u00e1ginas, 112 rutas de API, 68 componentes, 85 m\u00f3dulos de librer\u00eda, 64.304 l\u00edneas TS, 68 archivos SQL con 14.002 l\u00edneas, 31 tablas, 216 pol\u00edticas, 147 funciones SQL, 79 triggers, 86 archivos de test (9.086 l\u00edneas)')],
        ['Suscripci\u00f3n Profesional de 19 \u20ac al mes o 190 \u20ac al a\u00f1o: portal de cliente, webhooks, gesti\u00f3n de impagos, NIF e IVA incluido.',
         'Cr\u00e9ditos sueltos con Bizum, transferencia o PayPal; cupones, planes de regalo y prueba de 30 d\u00edas con periodo de gracia.',
         '16 filtros t\u00e9cnicos guardados en JSONB con \u00edndices GIN.',
         'Dossier de homologaci\u00f3n verificado, en un bucket privado con URL firmadas de 5 minutos.',
         'Calculadora del impuesto de transmisiones con 19 landings por comunidad aut\u00f3noma.',
         'Valorador "\u00bfcu\u00e1nto vale mi camper?", generador de contrato de compraventa, reservas, inspecciones y gestor\u00eda.',
         'Tiendas de profesionales con URL propia, importaci\u00f3n por CSV y p\u00e1ginas por marca y modelo.',
         'Landings de provincia por subcategor\u00eda con estad\u00edsticas reales y preguntas frecuentes en datos estructurados.',
         'Anal\u00edtica propia y an\u00f3nima, rendimiento por vendedor, y un cambio de esquema sin parada usando triggers de sincronizaci\u00f3n.',
         'Revisi\u00f3n documentada de una auditor\u00eda de seguridad externa y scripts en Python que verifican el SQL.'],
        'Stripe de principio a fin, no solo un bot\u00f3n de pago. Base de datos avanzada y disciplina de pruebas. Apoya los gigs 01, 04, 05 y 06.',
        '<b>Ense\u00f1ar.</b> La p\u00e1gina de planes, el flujo de pago en modo de prueba, el valorador y la calculadora de impuestos.')

    # P04
    s += proj('P04', 'MaquinariaOcasi\u00f3n y el generador de verticales',
        'Marketplace de maquinaria entre empresas, creado a partir del motor de CamperOcasi\u00f3n con una herramienta propia que clona y renombra un vertical.',
        [('Repositorio', M('maquinaria-ocasion')),
         ('Dominio', 'maquinaria.click'),
         ('Periodo', '24 a 27 oct 2026, 77 commits'),
         ('Tama\u00f1o', '47 p\u00e1ginas, 107 rutas de API, 54 componentes, 59.184 l\u00edneas TS, 74 archivos SQL con 17.306 l\u00edneas, 34 tablas, 72 archivos de test, 384 p\u00e1ginas generadas en el build')],
        ['Herramienta ' + M('tools/clon-vertical') + ' con un archivo de marca: cambia nombre, dominio, textos y categor\u00edas en todo el c\u00f3digo.',
         'Identidad centralizada en un \u00fanico m\u00f3dulo de marca.',
         'A\u00f1adidos propios: foro, comparador, tasador, p\u00e1ginas de marca y v\u00eddeos incrustados.',
         'IndexNow con tarea programada y gu\u00eda de Search Console.'],
        'Que tu marketplace es un motor reutilizable. En cuatro d\u00edas y 77 commits sacaste un vertical nuevo. Es el argumento para vender "tu marketplace en tres a cinco semanas" en el gig 01.',
        '<b>Ense\u00f1ar junto a P03</b>, como prueba de reutilizaci\u00f3n. Aclara que comparten motor.',
        note('El documento de estado de este repositorio tiene los nombres de marca sustituidos en bloque y cita un dominio de relleno. El dominio real, seg\u00fan PROJECT.md, es maquinaria.click. Conviene corregirlo si vas a ense\u00f1ar el repositorio.', kind='warn'))

    # P05
    s += proj('P05', 'KHC Auto Import, web p\u00fablica y ERP',
        'Negocio de importaci\u00f3n de coches en A Coru\u00f1a. Un solo proyecto de Vercel sirve dos aplicaciones seg\u00fan el dominio: la web p\u00fablica y el ERP interno.',
        [('Repositorio', M('KHC-Auto-Import')),
         ('Dominios', 'khcimport.autos (web) y app.khcimport.autos (ERP)'),
         ('Periodo', '13 may a 15 oct 2026, 239 commits'),
         ('Stack', 'Next.js 16 y React 19 en la web; React 19, Vite 8 y Tailwind 4 en el ERP; Supabase en regi\u00f3n europea; Python para an\u00e1lisis y PDF'),
         ('Tama\u00f1o', 'ERP: 62.471 l\u00edneas JS y JSX. Web: 7.583. Scripts: 4.101. Python: 13.264. 15 tablas, 26 pol\u00edticas, 74 comprobaciones autom\u00e1ticas, 17 documentos')],
        ['16 m\u00f3dulos de ERP: panel, flota con proceso de 10 pasos, cat\u00e1logo de 1.104 variantes de 37 marcas, simulador de importaci\u00f3n, CRM, contabilidad, facturaci\u00f3n, generador de anuncios, documentos, fotos, informes, publicaci\u00f3n en la web, contactos de la web, calculadora de viajes con mapa y lista de inspecci\u00f3n.',
         'Motor y calendario fiscal espa\u00f1ol: modelos 576 y 620, impuesto de matriculaci\u00f3n, IVTM, r\u00e9gimen de bienes usados, IRPF y Sociedades.',
         'Roles de propietario, gestor, comercial y gestor\u00eda con seguridad por filas, y funcionamiento sin conexi\u00f3n.',
         'Tratamiento de fotos: borrado de metadatos y ocultaci\u00f3n de matr\u00edculas.',
         'Scrapers de autoscout24 (Alemania y Espa\u00f1a), mobile.de y milanuncios: 474 observaciones de mercado.',
         'Modelo de precios por regresi\u00f3n con R\u00b2 de 0,892.',
         'Plan de negocio en PDF generado con Python, con an\u00e1lisis de sensibilidad.'],
        'Que puedes hacer la herramienta interna completa de una empresa, con su fiscalidad, y adem\u00e1s los datos de mercado que la alimentan. Apoya los gigs 07, 08 y 09.',
        '<b>Ense\u00f1ar con datos de ejemplo.</b> Capturas del panel, la flota y el simulador. Oculta cifras reales del negocio.')

    # P06
    s += proj('P06', 'CotizaT, SaaS de presupuestos de obra',
        'Aplicación web para presupuestar construcción y reformas, con versión de escritorio para Windows. Es tu proyecto más grande: 966 commits y 222 pull requests en tres meses.',
        [('Repositorio', M('generador-comercial')),
         ('Dominio', 'cotizat.online'),
         ('Periodo', '13 ago a 11 nov 2026, 966 commits, 222 pull requests'),
         ('Stack', 'Python, FastAPI, SQLAlchemy 2, Alembic, Jinja2, ReportLab; Postgres 17 y Auth en Supabase; Stripe, Resend, Groq, Redis de Upstash; Vercel con tres tareas programadas'),
         ('Tamaño', '98.027 líneas de Python en la aplicación, 378 rutas en 17 routers, 102 módulos de servicio, 60 modelos, 272 plantillas HTML (41.925 líneas), 15.867 líneas de JavaScript y 69 migraciones'),
         ('Pruebas', '2.614 tests en 239 archivos (61.895 líneas), más una batería de seguridad por filas sobre Postgres real'),
         ('Herramientas', '151 scripts propios (37.240 líneas) para construir el catálogo, cargar precios y auditar'),
         ('Producción', '61 tablas, 223 políticas de seguridad por filas y 220 índices; cerca de 177.000 partidas y 8.500 precios de mercado para 18 países'),
         ('Uso real', 'Tu documento del 2 de noviembre cuenta 41 cuentas y 4 empresas de pago, medidas en la base de producción')],
        ['Editor de presupuestos por capítulos y partidas, con mediciones, costes internos, márgenes, versiones, plantillas, atajos de teclado, pegado desde Excel y guardado automático.',
         'PDF profesional con marca propia, portada, firma del cliente, anexos fusionados y marca de agua según el estado. El motor son 2.169 líneas sobre ReportLab.',
         'Importación y exportación BC3 (FIEBDC-3) e importación de descompuestos de Excel conservando la matriz original.',
         'Medición sobre planos: calibrar la escala, medir longitudes, áreas y conteos, aplicar la medición a una partida y exportar a DXF, CSV o PNG.',
         'Catálogo propio de más de 3.000 partidas con su descompuesto, generado y validado por scripts, y precios de referencia investigados país por país.',
         'Multiempresa: organizaciones, miembros e invitaciones, con cada empresa aislada por seguridad por filas.',
         'Cobro: Stripe Checkout y suscripciones con webhook firmado, programado sin la librería oficial; licencias, prueba gratuita, recibos en PDF y cobro manual donde Stripe no opera.',
         'Asistente con herramientas propias que busca, revisa presupuestos, calcula mediciones y detecta lo que falta en el alcance, sin gastar tokens. Groq es opcional para redactar.',
         '23 países configurados con moneda, impuestos y etiquetas fiscales; módulos fiscales de Estados Unidos, Reino Unido e Irlanda; interfaz en español e inglés.',
         'Web pública con SEO programático: páginas de precios por país, capítulo y partida, comparador internacional, calculadora, tarifas de mano de obra, sitemaps por país, hreflang y llms.txt.',
         'Panel de operador con 68 rutas: ventas, cobros, renovaciones, clientes, conversaciones, finanzas, automatizaciones y auditoría. 47 plantillas de correo.',
         'Seguridad: sesión en cookies HttpOnly, protección CSRF por origen, CSP estricta, archivos privados con URL firmadas y límite de peticiones distribuido.',
         'Integración continua: dependencias fijadas, pip-audit, búsqueda de secretos, comprobación de plantillas y JavaScript, simulación del sistema de archivos de Vercel y la suite completa.',
         'Copia de seguridad y restauración, exportación y baja de la organización, plan de respuesta a incidentes y simulacro de caída documentados.'],
        'Que sabes llevar un SaaS de verdad de principio a fin: producto, cobro, varios países, pruebas y operación. Es otro stack distinto del de los marketplaces, y es tu oficio de la obra convertido en software. Apoya los gigs 07, 10, 13 y 14.',
        '<b>Enseñar con capturas y vídeo,</b> no con el repositorio: el editor, la medición sobre plano, un PDF generado y el panel de operador con datos de ejemplo.',
        note(['Has abierto el repositorio para este análisis, pero es tu producto comercial. Ahora mismo cualquiera puede clonar el código, el catálogo de partidas con sus precios y tus documentos de estrategia.',
              'Uno de esos documentos nombra a dos empresas clientes. Vuelve a hacerlo privado: para Fiverr te bastan las capturas y las cifras de esta ficha. Detalle en la sección 08.'],
             kind='warn', title='Vuelve a hacerlo privado'))

    # P07
    s += proj('P07', 'RemodelaT.net, web de reformas en Venezuela',
        'Web corporativa de una empresa de remodelaci\u00f3n, en espa\u00f1ol e ingl\u00e9s, con SEO local llevado al detalle. 408 commits.',
        [('Repositorio', M('reformat-venezuela')),
         ('Dominio', 'remodelat.net'),
         ('Periodo', '28 may a 27 ago 2026, 408 commits'),
         ('Stack', 'Astro 6 (generaci\u00f3n est\u00e1tica), sitemap y RSS, Vercel'),
         ('Tama\u00f1o', '273 p\u00e1ginas generadas, 24 componentes, 47 art\u00edculos de blog en dos idiomas, 13 p\u00e1ginas de servicio, 7 casos de proyecto, 40 scripts de generaci\u00f3n y correcci\u00f3n')],
        ['Landings de remodelaci\u00f3n de ba\u00f1o y de cocina para m\u00e1s de 30 zonas de Carabobo, Caracas y La Guaira.',
         'Datos estructurados LocalBusiness, BreadcrumbList, BlogPosting y Service; canonical y hreflang; Open Graph con dimensiones le\u00eddas de la propia imagen.',
         'Casos de proyecto con deslizador de antes y despu\u00e9s, galer\u00eda por fases y visor de im\u00e1genes.',
         'PWA con service worker, p\u00e1gina sin conexi\u00f3n, fuentes locales y CSS en l\u00ednea.',
         'El build comprueba im\u00e1genes, SEO y PWA, y avisa a los buscadores con IndexNow.',
         'An\u00e1lisis completo documentado (visual, SEO, c\u00f3digo, rendimiento) que detect\u00f3, por ejemplo, 10.217 enlaces internos con redirecci\u00f3n y 3 hreflang rotos.',
         'Material de marketing: flyers para Facebook en varias tandas, generados por script.'],
        'SEO local program\u00e1tico y una forma de trabajar: auditar, medir y corregir con scripts. Apoya los gigs 03 y 06.',
        '<b>Ense\u00f1ar.</b> Es tu mejor ejemplo de web para negocio local.',
        note('En la ra\u00edz de este repositorio p\u00fablico hay un presupuesto en PDF de un cliente. Ret\u00edralo del repositorio antes de enlazarlo.', kind='warn'))

    # P08
    s += proj('P08', 'Reformat Houston',
        'Adaptaci\u00f3n de la web de reformas al mercado de Houston, con el ingl\u00e9s como idioma principal y versi\u00f3n en espa\u00f1ol.',
        [('Repositorio', M('reformat-houston')),
         ('Periodo', '16 a 18 jul 2026, 84 commits'),
         ('Stack', 'Astro 5, Tailwind, sitemap y RSS'),
         ('Tama\u00f1o', '63 archivos de p\u00e1gina; 12 zonas (Katy, Sugar Land, The Woodlands, River Oaks y otras) y 9 servicios, en dos idiomas'),
         ('Rendimiento', 'Informes Lighthouse guardados en el repositorio: rendimiento 98 a 100, accesibilidad 95 a 96, buenas pr\u00e1cticas 100, SEO 100')],
        [],
        'Que puedes llevar una web a otro pa\u00eds e idioma en tres d\u00edas y dejarla con puntuaciones altas. Apoya los gigs 03 y 06.',
        '<b>Ense\u00f1ar</b> las puntuaciones Lighthouse. El README est\u00e1 vac\u00edo y mal codificado: reescr\u00edbelo antes.')

    # P09
    s += proj('P09', 'RemodelaT Coru\u00f1a',
        'Web de tu futura empresa de reformas en A Coru\u00f1a, adaptada desde la de Venezuela.',
        [('Repositorio', M('RemodelaT-Galicia')),
         ('Periodo', '4 a 6 sep 2026, 16 commits'),
         ('Stack', 'Astro 6'),
         ('Tama\u00f1o', '62 archivos de p\u00e1gina: 30 landings (3 servicios por 10 municipios), 11 servicios, 7 proyectos, blog, textos legales')],
        ['Siete scripts en el build que lo hacen fallar si hay enlaces rotos, canonical incorrectos o problemas de PWA.',
         'Precios orientativos en euros sin IVA y portfolio de obras reales ejecutadas en Espa\u00f1a.'],
        'Que tienes una plantilla de web para empresas de servicios que se adapta a una ciudad nueva en d\u00edas. Apoya el gig 03.',
        '<b>Ense\u00f1ar cuando tenga dominio.</b> Todav\u00eda faltan dominio, tel\u00e9fono y logotipo definitivos.')

    # P10
    s += proj('P10', 'Webs con 3D y gestor de contenidos',
        'Cuatro proyectos en Next.js 14 con animaci\u00f3n y gr\u00e1ficos 3D.',
        [('REFORMATNEW', 'Next.js, TypeScript y Sanity como gestor de contenidos. React Three Fiber, Spline y Framer Motion. Plano de planta interactivo y 8 p\u00e1ginas de servicio. 24 commits.'),
         ('Majestic', 'Web de un estudio de dise\u00f1o digital, "MajesticWeb": servicios, portfolio, SEO, rendimiento, UX y contacto con formulario por pasos. Robot 3D de Spline, cursor propio y componentes al estilo shadcn. 44 commits.'),
         ('majesticweb-sandbox', 'Variante con una escena de la Tierra en three.js y animaci\u00f3n con GSAP. 34 commits.'),
         ('rincon-carabobo', 'Landing de restaurante con escena 3D en la cabecera. 3 commits.')],
        [],
        'Dise\u00f1o con movimiento y 3D, y conexi\u00f3n con un gestor de contenidos. Apoya el gig 02.',
        '<b>Ense\u00f1ar Majestic.</b> Puede ser tu propia web de estudio y tu marca en Fiverr. Los README son los de la plantilla: c\u00e1mbialos.')

    # P11
    s += proj('P11', 'Vig\u00eda, videovigilancia autoalojada',
        'Aplicaci\u00f3n para Windows que graba y vigila c\u00e1maras IP sin depender de la nube del fabricante.',
        [('Repositorio', M('Vigia')),
         ('Periodo', '24 abr a 1 sep 2026, 36 commits'),
         ('Stack', 'Python, FastAPI, OpenCV, ffmpeg, YOLO opcional, pywebview, PyInstaller, Inno Setup'),
         ('Tama\u00f1o', '8.510 l\u00edneas de Python y 3.817 de interfaz web')],
        ['Descubrimiento de c\u00e1maras por RTSP, ONVIF y DVRIP; c\u00e1maras de varias lentes y control de movimiento.',
         'V\u00eddeo en directo, modos de grabaci\u00f3n, zonas de detecci\u00f3n, m\u00e1scaras de privacidad y aviso de manipulaci\u00f3n.',
         'Avisos por Telegram, ntfy, webhook, Discord, Pushover, correo y notificaciones push.',
         'Interfaz instalable como PWA, ventana de escritorio e instalador para Windows.'],
        'Python de sistemas: v\u00eddeo, protocolos de c\u00e1mara, detecci\u00f3n y empaquetado de una aplicaci\u00f3n de escritorio. Apoya el gig 12.',
        '<b>Ense\u00f1ar.</b> Corrige antes la descripci\u00f3n del repositorio en GitHub: ahora pone "Goofy Burger website".')

    # P12
    s += proj('P12', 'MiClaw, asistente de IA local',
        'Asistente que funciona en tu ordenador y puede usar herramientas, con modelos locales o en la nube.',
        [('Repositorio', M('testing')),
         ('Periodo', '12 may a 30 ago 2026, 32 commits'),
         ('Stack', 'Python, FastAPI, interfaz web con respuesta en streaming'),
         ('Tama\u00f1o', '3.117 l\u00edneas de Python y 2.636 de interfaz. Versi\u00f3n 1.6')],
        ['11 proveedores de modelos: Ollama, Gemini, Groq, OpenRouter, Qwen, Mistral, Cerebras, Z.ai, GitHub Models, SambaNova y cualquier API compatible con OpenAI.',
         'Agente que ejecuta herramientas pidiendo aprobaci\u00f3n, b\u00fasqueda sobre tu c\u00f3digo (RAG), bucle de depuraci\u00f3n y b\u00fasqueda web.',
         'Memoria, recordatorios y tareas aut\u00f3nomas programadas.',
         'Visi\u00f3n y capturas de pantalla, comparaci\u00f3n visual, voz y acceso desde varios dispositivos con PIN.',
         'Instaladores para Windows.'],
        'Integraci\u00f3n de modelos de lenguaje con criterio: varios proveedores, agentes, RAG y control humano. Apoya el gig 10.',
        '<b>Ense\u00f1ar.</b> Cambia el nombre del repositorio de "testing" a "miclaw" y dale una descripci\u00f3n.')

    # P13
    s += proj('P13', 'Planes de negocio con modelo financiero',
        'Tres planes de negocio, con los n\u00fameros calculados por c\u00f3digo.',
        [('KHC-Tienda', 'Tienda de ropa infantil en Oleiros. Python con reportlab y svglib genera un HTML interactivo y un PDF de 49 p\u00e1ginas con gr\u00e1ficos, cuenta de resultados a 5 a\u00f1os, VAN, TIR y an\u00e1lisis de sensibilidad. Modelos en CSV y documentos sobre proveedores, subvenciones, local y forma jur\u00eddica. 2.857 l\u00edneas de Python.'),
         ('RINCOCARABOBO', 'Plan de RemodelaT Coru\u00f1a en 10 cap\u00edtulos: estructura de costes por tipo de obra, coste laboral real, calibraci\u00f3n de tarifas, tesorer\u00eda, siete proyectos documentados y plantillas de presupuesto.'),
         ('KHC-Auto-Import', 'Carpeta de plan de negocio con presupuesto de arranque, escandallo por coche, flujo de caja, estudio de nave, cronograma de reforma y cuatro PDF generados con Python.')],
        [],
        'Que sabes plantear un negocio con cifras defendibles y entregarlo en un documento cuidado. Apoya el gig 09.',
        '<b>Ense\u00f1ar solo extractos.</b> Usa p\u00e1ginas de muestra con datos anonimizados. Los repositorios contienen informaci\u00f3n personal y de negocio: ver la secci\u00f3n 08.')

    # P14
    s += proj('P14', 'GG Beauty Premium, landing en tres idiomas con panel propio',
        'Web de un centro de est\u00e9tica de Lanzarote, la m\u00e1s trabajada de las landings: 98 commits.',
        [('Repositorio', M('ggbeautyPremium')),
         ('Stack', 'HTML, CSS y JavaScript sin framework'),
         ('Periodo', '15 a 20 may 2026')],
        ['Espa\u00f1ol, ingl\u00e9s y alem\u00e1n, con traducciones en un archivo JSON y el idioma recordado en el navegador.',
         'Servicios cargados desde un JSON y pintados seg\u00fan el idioma.',
         'Panel de administraci\u00f3n en ' + M('/admin') + ' que edita el contenido a trav\u00e9s de la API de GitHub: un gestor de contenidos sin servidor ni base de datos.',
         'V\u00eddeo de cabecera distinto para m\u00f3vil y escritorio, datos estructurados, Open Graph y cabeceras de cach\u00e9 en Vercel.'],
        'Que puedes entregar una web que el cliente edita solo, sin cuotas de gestor de contenidos. Apoya el gig 02.',
        '<b>Ense\u00f1ar</b>, si fue un encargo o tienes permiso del negocio.')

    # P15
    s += h2('Veintiuna landings de negocio en un solo archivo', tag='P15')
    s.append(P('Entre el 26 de abril y el 15 de mayo de 2026 publicaste 21 landings en HTML, cada una en un \u00fanico archivo con v\u00eddeo de cabecera, desplegadas en Vercel. Se agrupan en cuatro familias de dise\u00f1o.'))
    s.append(table([
        ['Familia', 'Repositorios', 'Caracter\u00edsticas'],
        ['Est\u00e9tica y belleza (10)', 'vanity-face, jessica-montes, devons--beauty, blum-concept, belleza-lola, Loveliness, hair-beauty, infinity-beauty, ggbeauty, kaizen-estetica', 'Unas 1.800 l\u00edneas y 90 KB. V\u00eddeo de cabecera, tipograf\u00eda Playfair Display, siete secciones (inicio, nosotros, servicios, galer\u00eda, opiniones, equipo, contacto), formulario de reserva y aparici\u00f3n al hacer scroll.'],
        ['Cl\u00ednicas (4)', 'axularvet, pododent, euroklinik, poliklinik', 'Animaci\u00f3n con GSAP y ScrollTrigger, desplazamiento suave con Lenis. Tres de ellas con selector de espa\u00f1ol, ingl\u00e9s y alem\u00e1n.'],
        ['Inmobiliarias de Lanzarote (5)', 'artekasa, lanzarote7, casalanz, precio-perfecto, Timanfaya', 'Tipograf\u00eda Manrope, v\u00eddeo de cabecera, rejilla de propiedades, buscador en ventana modal y WhatsApp. Artekasa est\u00e1 en cinco idiomas.'],
        ['Restaurantes (2)', 'avenida55, el-rincon-carabobo', 'Carta con filtros por categor\u00eda, reservas y mapa. El Rinc\u00f3n de Carabobo a\u00f1ade part\u00edculas en three.js, GSAP y rejilla tipo bento.'],
    ], [20, 34, 46], first_bold=True))
    s.append(h3('Lo que demuestra ante un comprador'))
    s.append(P('Rapidez y oficio visual: una landing completa en un d\u00eda, adaptada a cuatro sectores. Es la base del gig 02.'))
    s.append(note([
        'Estas p\u00e1ginas llevan el nombre de negocios reales de Lanzarote y Madrid, con fotos de banco de im\u00e1genes. Por los repositorios no puedo saber si fueron encargos o propuestas que hiciste por tu cuenta.',
        'Si fueron encargos, pide permiso al cliente antes de usarlas en el portfolio. Si fueron propuestas, pres\u00e9ntalas como "dise\u00f1o conceptual" y cambia el nombre del negocio por uno inventado. Presentar como cliente a un negocio que no te contrat\u00f3 puede costarte la cuenta y un disgusto con ese negocio.'
    ], kind='warn', title='Antes de usarlas en el portfolio'))

    # P16
    s += h2('Repositorios sin contenido', tag='P16')
    s.append(table([
        ['Repositorio', 'Estado', 'Qu\u00e9 hacer'],
        ['ProEngineX', 'Solo un README con el t\u00edtulo. Descripci\u00f3n: "ENGINE SL".', 'Hacer privado hasta que tenga contenido.'],
        ['dise-o-web', 'Solo un README con el t\u00edtulo, aunque GitHub indica 37 MB de uso. Descripci\u00f3n: "Dise\u00f1o Web Venezuela".', 'Hacer privado o borrar.'],
        ['tumaquinaria', 'Vac\u00edo.', 'Borrar.'],
        ['reformat', 'Vac\u00edo.', 'Borrar.'],
        ['portafolio', 'Este repositorio.', 'Aqu\u00ed se guarda este dossier.'],
    ], [20, 48, 32], first_bold=True))
    return s
