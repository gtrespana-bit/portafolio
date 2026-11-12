# -*- coding: utf-8 -*-
from reportlab.platypus import Paragraph, Spacer, PageBreak, NextPageTemplate
from reportlab.lib import colors
from lib import *
from c3_services import COUNT


def cover():
    w = colors.white
    soft = colors.HexColor('#B9C6D3')
    out = [Spacer(1, 30 * mm)]
    out.append(Paragraph('DOSSIER FIVERR  \u00b7  11 NOV 2026', ps('c0', fontName='Mono-Md', fontSize=9, leading=12, textColor=GOLD_L)))
    out.append(Spacer(1, 16 * mm))
    out.append(Paragraph('Todo lo que puedes<br/>vender en Fiverr', ps('c1', fontName='PlexC-Bd', fontSize=50, leading=52, textColor=w)))
    out.append(Spacer(1, 9 * mm))
    out.append(Paragraph(
        'Experiencia demostrable, cat\u00e1logo completo de servicios y gigs listos para publicar, '
        'a partir de la revisi\u00f3n de los 44 repositorios de <font name="Mono">gtrespana-bit</font>.',
        ps('c2', fontSize=13, leading=19, textColor=soft)))
    out.append(Spacer(1, 30 * mm))
    out.append(stats([
        ('44', 'repositorios revisados, con el código de todos leído'),
        ('3.328', 'commits entre abril y noviembre de 2026'),
        ('+500k', 'l\u00edneas de c\u00f3digo medidas en los proyectos principales'),
        ('7', 'productos con dominio propio en producci\u00f3n'),
        ('364', 'rutas de API en los cuatro marketplaces'),
        ('198', 'tablas Postgres entre los seis productos con base de datos'),
        (str(COUNT), 'servicios distintos que puedes ofrecer'),
        ('14', 'gigs redactados, con paquetes y precios'),
    ], cols=4, dark=True))
    out += [NextPageTemplate('main'), PageBreak()]
    return out


def build():
    s = []
    # ---------------- TOC
    s += [P('', 'h1num'), Paragraph('Contenido', ST['h1']), Rule(color=NAVY, thickness=1.2, space=10), toc()]

    # ---------------- 0
    s += section('00', 'C\u00f3mo leer este documento',
                 'Este dossier tiene dos usos: saber con precisi\u00f3n qu\u00e9 experiencia puedes demostrar, '
                 'y tener el texto ya escrito para montar el perfil y los gigs en Fiverr.')
    s += bullets([
        '<b>Secciones 01 a 03:</b> qui\u00e9n eres seg\u00fan tu c\u00f3digo, el perfil de Fiverr listo para pegar y el inventario de tecnolog\u00eda que has usado de verdad.',
        '<b>Secci\u00f3n 04:</b> cada proyecto, uno a uno, con sus cifras medidas en el repositorio y lo que demuestra ante un comprador.',
        '<b>Secci\u00f3n 05:</b> el cat\u00e1logo completo, %d servicios agrupados' % COUNT + '  por categor\u00eda, con la prueba que respalda cada uno, precio orientativo y plazo.',
        '<b>Secci\u00f3n 06:</b> 14 gigs redactados en ingl\u00e9s (t\u00edtulo, descripci\u00f3n, etiquetas, tres paquetes, preguntas frecuentes y requisitos).',
        '<b>Secciones 07 a 09:</b> precios y orden de lanzamiento, lo que conviene arreglar en GitHub antes de publicar y los datos que solo t\u00fa puedes rellenar.',
        '<b>Anexos:</b> tabla de los 44 repositorios, palabras clave y plantillas de mensajes para compradores.',
    ])
    s.append(h3('C\u00f3mo se ha hecho el an\u00e1lisis'))
    s += bullets([
        'He clonado los otros 43 repositorios de la cuenta y he le\u00eddo sus README, documentos de proyecto, dependencias, \u00e1rboles de rutas, librer\u00edas, componentes, migraciones SQL y tests. Las cifras de este documento (p\u00e1ginas, rutas, l\u00edneas, tablas, pol\u00edticas) est\u00e1n contadas sobre el c\u00f3digo, no copiadas de la documentaci\u00f3n.',
        'CotizaT (<font name="Mono">generador-comercial</font>) lo abriste el 11 de noviembre y lo he leído igual que el resto. Las cifras de su base de datos en producción (tablas, políticas, partidas cargadas) vienen de tu proyecto de Supabase.',
        'Los bloques con la marca <font name="Mono-Md" color="#A06F12">COPIAR</font> est\u00e1n escritos para pegarse tal cual. El contador indica los caracteres frente al l\u00edmite habitual de Fiverr.',
    ])
    s.append(note([
        'No he podido abrir tus webs en producci\u00f3n ni la p\u00e1gina de Fiverr: el entorno donde trabajo solo tiene acceso a GitHub. Por eso no hay capturas de pantalla, y los l\u00edmites y nombres de categor\u00eda de Fiverr son los que conozco, no una comprobaci\u00f3n de hoy. Verif\u00edcalos en tu panel al publicar.',
        'Los precios son una recomendaci\u00f3n m\u00eda, razonada en la secci\u00f3n 07. Antes de fijarlos, mira 5 o 10 gigs de tu misma subcategor\u00eda.',
    ], kind='warn', title='L\u00edmites de este an\u00e1lisis'))

    # ---------------- 1
    s += section('01', 'Resumen: qu\u00e9 puedes demostrar',
                 'En siete meses has publicado en GitHub el c\u00f3digo de siete productos en producci\u00f3n, '
                 'tres webs corporativas con SEO local, 26 webs y landings de negocio y dos aplicaciones de escritorio en Python.')
    s.append(stats([
        ('4', 'marketplaces completos: clasificados, inmuebles, campers y maquinaria'),
        ('209k', 'l\u00edneas TypeScript en esos cuatro marketplaces'),
        ('460', 'archivos de test: 221 en los marketplaces y 239 en CotizaT'),
        ('611', 'sentencias CREATE POLICY (seguridad por filas) en sus migraciones'),
        ('62k', 'l\u00edneas del ERP de KHC Auto Import, con 16 m\u00f3dulos'),
        ('177k', 'partidas de obra en el cat\u00e1logo de CotizaT, para 18 pa\u00edses'),
        ('273', 'p\u00e1ginas est\u00e1ticas en remodelat.net, en espa\u00f1ol e ingl\u00e9s'),
        ('100', 'puntuaci\u00f3n Lighthouse de rendimiento en la home de Reformat Houston'),
    ], cols=4))
    s += h2('Los siete activos más vendibles', toc=False)
    s.append(table([
        ['Activo', 'Por qu\u00e9 vende', 'D\u00f3nde est\u00e1 la prueba'],
        ['Motor de marketplace', 'Has lanzado cuatro verticales con el mismo motor y tienes un generador que clona un vertical nuevo. Pocos vendedores de Fiverr pueden ense\u00f1ar uno en producci\u00f3n; t\u00fa, cuatro.', 'Marketplace-vzla, vendet-inmuebles, camperocasion, maquinaria-ocasion'],
        ['Supabase con seguridad real', 'Pol\u00edticas RLS, funciones SQL, triggers, buckets privados con URL firmadas, l\u00edmites de peticiones at\u00f3micos y revisi\u00f3n de auditor\u00edas externas.', 'Migraciones de los cuatro marketplaces, KHC y CotizaT'],
        ['SEO t\u00e9cnico y program\u00e1tico', 'Landings generadas por ciudad y categor\u00eda, datos estructurados, hreflang, sitemaps, IndexNow y scripts que hacen fallar el build si hay errores SEO.', 'reformat-venezuela, RemodelaT-Galicia, reformat-houston, los marketplaces'],
        ['Pagos y suscripciones', 'Stripe con suscripci\u00f3n mensual y anual, portal de cliente, webhooks, impagos, cupones y prueba gratuita. Adem\u00e1s, cobro manual con justificante le\u00eddo por OCR.', 'camperocasion, maquinaria-ocasion, vendet-inmuebles'],
        ['Herramientas internas y ERP', 'Un ERP completo con CRM, contabilidad, motor fiscal espa\u00f1ol, facturaci\u00f3n, roles y modo sin conexi\u00f3n.', 'KHC-Auto-Import'],
        ['SaaS multiempresa en Python', 'CotizaT es tu proyecto más grande: 98.000 líneas de aplicación, 378 rutas, cobro con Stripe, 23 países, dos idiomas y 2.614 tests. Según tu documento del 2 de noviembre, ya tiene empresas que pagan.', 'generador-comercial'],
        ['Conocimiento del sector de la obra', 'Has dirigido empresas de reformas y has convertido ese oficio en software: presupuestos, partidas, mediciones y precios por pa\u00eds.', 'CotizaT, RINCOCARABOBO, las tres webs de reformas'],
    ], [20, 50, 30], first_bold=True))
    s += h2('Posicionamiento recomendado', toc=False)
    s.append(P('Tres frases posibles para presentarte. La primera es la que mejor encaja con lo que hay en tus repositorios.'))
    s.append(table([
        ['Opci\u00f3n', 'Frase', 'Cu\u00e1ndo usarla'],
        ['A. Constructor de productos', 'Dise\u00f1o, programo y lanzo plataformas web completas: marketplaces, SaaS y herramientas internas con Next.js y Supabase.', 'Perfil principal. Atrae pedidos grandes y encaja con los gigs 01, 04, 05, 07 y 14.'],
        ['B. Webs que posicionan para negocios locales', 'Webs r\u00e1pidas con SEO local para empresas de servicios, hechas por alguien que ha dirigido una.', 'Si quieres volumen de pedidos peque\u00f1os y medianos. Gigs 02, 03 y 06.'],
        ['C. Ingeniero de obra que programa', 'Software, presupuestos y planes de negocio para constructoras y empresas de reformas.', 'Nicho con poca competencia. Gigs 03, 09 y 13.'],
    ], [22, 46, 32], first_bold=True))
    s.append(note('Tu ventaja no es saber un framework, es haber llevado productos enteros hasta producci\u00f3n: base de datos, pagos, panel de administraci\u00f3n, SEO, correos, moderaci\u00f3n y documentaci\u00f3n. Dilo as\u00ed, con las cifras, y ense\u00f1a los enlaces.', title='La idea central'))

    # ---------------- 2
    s += section('02', 'Perfil de Fiverr, listo para pegar',
                 'Textos para la cabecera del perfil. Est\u00e1n en ingl\u00e9s porque es donde est\u00e1 la mayor\u00eda de la demanda; debajo va la versi\u00f3n en espa\u00f1ol por si abres el perfil tambi\u00e9n en ese idioma.')
    s += h2('Nombre y eslogan', toc=False)
    s.append(kv([
        ('Nombre visible', 'Tu nombre real, por ejemplo <b>Rub\u00e9n T.</b> Genera m\u00e1s confianza que una marca cuando a\u00fan no hay rese\u00f1as.'),
        ('Usuario', 'Corto y profesional. Ideas: <font name="Mono">rubenbuilds</font>, <font name="Mono">ruben_webdev</font>, <font name="Mono">majesticweb</font> (ya tienes esa marca de estudio en el repo Majestic). El usuario no se puede cambiar despu\u00e9s.'),
        ('Foto', 'Retrato real, fondo liso, buena luz. Sin logotipo.'),
    ]))
    s += paste('Eslogan (EN)', 'Full stack developer. I build and launch marketplaces, SaaS and fast websites.', 80, title=True)
    s += paste('Eslogan (ES)', 'Desarrollador full stack. Creo y lanzo marketplaces, SaaS y webs r\u00e1pidas.', 80, title=True)
    s += h2('Descripci\u00f3n del perfil', toc=False)
    s += paste('Descripci\u00f3n (EN)',
               "Hi, I'm Rub\u00e9n, an engineer and business owner who builds his own software.\n\n"
               "In 2026 I designed, coded and launched seven live products: four marketplaces (classifieds, real estate, campervans, machinery), "
               "a car import ERP, a construction estimating SaaS and a bilingual 270 page SEO site.\n\n"
               "I work with Next.js, TypeScript, Supabase, Stripe, Astro and Python. I handle the whole job: database, payments, admin panel, SEO and deployment.\n\n"
               "I ran renovation companies in Spain, so I understand deadlines, budgets and clients. Clear scope, honest timing, full source code.", 600)
    s += paste('Descripci\u00f3n (ES)',
               "Hola, soy Rub\u00e9n, ingeniero y empresario, y programo mi propio software.\n\n"
               "En 2026 he dise\u00f1ado, programado y lanzado siete productos en producci\u00f3n: cuatro marketplaces (clasificados, inmuebles, campers y maquinaria), "
               "un ERP de importaci\u00f3n de coches, un SaaS de presupuestos de obra y una web SEO biling\u00fce de 270 p\u00e1ginas.\n\n"
               "Trabajo con Next.js, TypeScript, Supabase, Stripe, Astro y Python, y me encargo de todo: base de datos, pagos, panel de administraci\u00f3n, SEO y despliegue.\n\n"
               "He dirigido empresas de reformas en Espa\u00f1a: s\u00e9 lo que son los plazos y los presupuestos.", 600)
    s.append(note('He escrito "engineer" porque as\u00ed te describes en tu perfil de fundador. Si tu titulaci\u00f3n es concreta (ingenier\u00eda civil, industrial, t\u00e9cnica), ponla. No a\u00f1adas a\u00f1os de experiencia como programador que no puedas respaldar: tu historial p\u00fablico empieza en abril de 2026, y siete productos en siete meses ya es un argumento fuerte por s\u00ed solo.', kind='warn', title='Ajusta antes de pegar'))
    s += h2('Habilidades para la secci\u00f3n Skills', toc=False)
    s.append(P('Fiverr permite una lista de habilidades. Estas son las que tu c\u00f3digo respalda, por orden de peso:'))
    s.append(table([
        ['Grupo', 'Habilidades (escr\u00edbelas en ingl\u00e9s)'],
        ['Frontend', 'Next.js, React, TypeScript, JavaScript, Tailwind CSS, Astro, HTML5, CSS3, Framer Motion, GSAP, Three.js, Progressive Web Apps'],
        ['Backend y datos', 'Supabase, PostgreSQL, SQL, Row Level Security, Node.js, REST API, FastAPI, Python, Vite'],
        ['Pagos e integraciones', 'Stripe, Webhooks, Cloudflare R2, Resend, Web Push, Telegram Bot API, Google Analytics 4, Sentry'],
        ['SEO', 'Technical SEO, Local SEO, Programmatic SEO, Schema Markup, Core Web Vitals, Google Search Console'],
        ['IA', 'LLM integration, Gemini API, Groq, Ollama, OpenAI compatible APIs, RAG, AI agents, OCR'],
        ['Python', 'Web scraping, OpenCV, ffmpeg, ReportLab, PDF generation, data analysis, PyInstaller'],
        ['Despliegue', 'Vercel, GitHub Actions, CI/CD, Git, cron jobs'],
        ['Negocio', 'Business planning, financial modeling, construction cost estimating, market research'],
    ], [20, 80], first_bold=True))
    s += h2('Resto de campos del perfil', toc=False)
    s.append(kv([
        ('Idiomas', 'Spanish: Native. English: indica tu nivel real (Basic, Conversational o Fluent). Tus webs est\u00e1n en dos idiomas, pero el comprador te escribir\u00e1 en ingl\u00e9s y tendr\u00e1s que contestar con soltura.'),
        ('Formaci\u00f3n', 'Tu titulaci\u00f3n de ingenier\u00eda, universidad y a\u00f1o. Dato que no est\u00e1 en los repositorios.'),
        ('Certificaciones', 'Solo si las tienes. No es un campo obligatorio.'),
        ('Ocupaci\u00f3n', 'Web Developer / Full Stack Developer, desde 2026. A\u00f1ade una segunda ocupaci\u00f3n: Construction & Renovation, con tus a\u00f1os reales al frente de empresas de reformas.'),
        ('Portfolio', 'Los proyectos de la secci\u00f3n 04 marcados como "Ense\u00f1ar". Fiverr deja subir im\u00e1genes, v\u00eddeo y PDF por gig y un portfolio en el perfil.'),
        ('Enlace a GitHub', 'Fiverr permite vincular cuentas. Antes, repasa la secci\u00f3n 08: hay repositorios p\u00fablicos que no deber\u00edan serlo.'),
    ]))
    return s
