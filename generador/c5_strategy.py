# -*- coding: utf-8 -*-
import json, os
from lib import *

M = lambda t: '<font name="Mono">%s</font>' % t


def build():
    # ---------------- 07
    s = section('07', 'Precios y plan de lanzamiento',
                'Un perfil nuevo sin rese\u00f1as no cobra lo mismo que uno con cincuenta. El plan es entrar con precios razonables en gigs r\u00e1pidos, juntar rese\u00f1as y subir.')
    s += h2('Cu\u00e1nto te queda de cada pedido', toc=False)
    s.append(P('La comisi\u00f3n de Fiverr que conozco es el 20 % de lo que paga el comprador por el pedido; compru\u00e9bala en sus condiciones actuales. El dinero queda retenido unos d\u00edas tras la entrega (lo habitual para vendedores nuevos son 14) antes de poder retirarlo.'))
    s.append(table([
        ['Precio del pedido', 'Comisi\u00f3n de Fiverr (20 %)', 'Recibes'],
        ['50 $', '10 $', '40 $'], ['150 $', '30 $', '120 $'], ['500 $', '100 $', '400 $'],
        ['1.200 $', '240 $', '960 $'], ['2.400 $', '480 $', '1.920 $'],
    ], [34, 33, 33], mono_cols=(0, 1, 2)))
    s.append(P('Calcula tus precios sobre lo que recibes, no sobre lo que paga el cliente. Y descuenta despu\u00e9s el coste de retirar el dinero y el cambio de moneda.', 'small'))
    s += h2('Regla de precios en tres escalones', toc=False)
    s.append(table([
        ['Etapa', 'Cu\u00e1ndo', 'Precio', 'Objetivo'],
        ['Lanzamiento', 'De 0 a 5 rese\u00f1as en el gig', 'Columna "lanzamiento" de la secci\u00f3n 06', 'Conseguir pedidos y rese\u00f1as de cinco estrellas'],
        ['Consolidaci\u00f3n', 'De 5 a 15 rese\u00f1as', 'Entre un 30 y un 50 % m\u00e1s', 'Filtrar clientes y ganar margen'],
        ['Objetivo', 'M\u00e1s de 15 rese\u00f1as', 'Columna "objetivo"', 'Trabajar menos pedidos y mejor pagados'],
    ], [16, 24, 32, 28], first_bold=True))
    s.append(P('No bajes de los precios de lanzamiento. Un precio demasiado bajo atrae pedidos conflictivos, y una mala rese\u00f1a al principio pesa mucho.'))
    s += h2('Orden de publicaci\u00f3n', toc=False)
    s.append(P('Fiverr limita el n\u00famero de gigs activos de los vendedores nuevos. Ese l\u00edmite ha cambiado con el tiempo (ha estado entre 4 y 7), as\u00ed que m\u00edralo en tu panel. El orden que propongo funciona con cualquiera de los dos.'))
    s.append(table([
        ['Ola', 'Gigs', 'Por qu\u00e9'],
        ['1. Primera semana', 'G02 landing, G06 auditor\u00eda SEO, G11 errores y despliegue, G04 Supabase', 'Encargos acotados, de pocos d\u00edas, con resultado f\u00e1cil de valorar. Traen las primeras rese\u00f1as.'],
        ['2. Con 3 a 5 rese\u00f1as', 'G03 web con SEO local, G05 Stripe, G10 inteligencia artificial, G08 scraper', 'Ticket medio. Ya tienes historial para que alguien se atreva con un pedido de varios cientos de d\u00f3lares.'],
        ['3. Con 10 o m\u00e1s rese\u00f1as', 'G01 marketplace, G07 ERP, G09 plan de negocio, G13 presupuestos, G14 SaaS, G12 videovigilancia', 'Proyectos largos. Aqu\u00ed est\u00e1 el dinero, pero nadie encarga 2.000 $ a un perfil vac\u00edo.'],
    ], [20, 40, 40], first_bold=True))
    s.append(note('Si el l\u00edmite es de cuatro gigs, la ola 1 los ocupa todos. Cuando un gig de la ola 1 ya tenga rese\u00f1as y quieras hueco, sustituye G11 por G03 o por G01: las rese\u00f1as cuentan para tu perfil entero.', title='Si solo puedes tener cuatro gigs'))
    s += h2('Tu disponibilidad real', toc=False)
    s.append(P('Seg\u00fan tus propios documentos, en diciembre de 2026 vuelves a A Coru\u00f1a para abrir RemodelaT Coru\u00f1a. Montar una empresa de reformas ocupa el d\u00eda entero. Tenlo en cuenta:'))
    s += bullets([
        'Pon plazos con margen. Los de la secci\u00f3n 06 suponen unas cuatro horas diarias de dedicaci\u00f3n.',
        'Limita los pedidos simult\u00e1neos en cada gig. Fiverr permite fijar un m\u00e1ximo de pedidos en cola.',
        'Usa el modo de ausencia cuando est\u00e9s en obra varios d\u00edas. Entregar tarde penaliza m\u00e1s que no estar disponible.',
        'Si vas a tener poco tiempo, prioriza los gigs de ticket alto con oferta personalizada frente a muchos pedidos peque\u00f1os.',
    ])
    s += h2('C\u00f3mo trabajar cada pedido', toc=False)
    s += bullets([
        '<b>Antes de aceptar:</b> pide que te escriban primero. En los gigs grandes, cierra el alcance por mensaje y env\u00eda una oferta personalizada.',
        '<b>Proyectos de m\u00e1s de 500 $:</b> div\u00eddelos en hitos con entregas parciales. Reduce el riesgo para los dos.',
        '<b>Durante el trabajo:</b> un mensaje de avance cada dos o tres d\u00edas, con una captura o un enlace de prueba.',
        '<b>Entrega:</b> el c\u00f3digo en el GitHub del cliente, un v\u00eddeo corto ense\u00f1ando el resultado y un documento de una p\u00e1gina con c\u00f3mo usarlo.',
        '<b>Todo dentro de Fiverr:</b> no des correo ni tel\u00e9fono ni cobres por fuera. Es motivo de cierre de cuenta.',
        '<b>Rese\u00f1as:</b> no las pidas a cambio de nada ni pidas una nota concreta. Entrega bien y recuerda al cliente, sin presi\u00f3n, que su valoraci\u00f3n te ayuda.',
        '<b>Tiempo de respuesta:</b> contesta el primer mensaje en menos de una hora cuando puedas. Es de lo que m\u00e1s influye en conseguir el pedido.',
    ])
    s += h2('Material que necesita cada gig', toc=False)
    s.append(P('Que yo sepa, Fiverr admite por gig hasta tres im\u00e1genes, un v\u00eddeo corto y dos PDF, y recomienda im\u00e1genes de 1280 por 769 p\u00edxeles. Confirma las medidas en el formulario.'))
    s.append(table([
        ['Material', 'Qu\u00e9 preparar'],
        ['Imagen principal', 'Una captura real del producto dentro de un marco de navegador o m\u00f3vil, con un t\u00edtulo de cuatro o cinco palabras. Sin fotos de banco ni iconos gen\u00e9ricos.'],
        ['Segunda imagen', 'Detalle de una funci\u00f3n: el panel de administraci\u00f3n, el mapa, la p\u00e1gina de planes o el informe.'],
        ['Tercera imagen', 'Las cifras: "4 marketplaces en producci\u00f3n", "273 p\u00e1ginas", "Lighthouse 100".'],
        ['V\u00eddeo (hasta 75 segundos)', 'Grabaci\u00f3n de pantalla recorriendo el producto, con tu voz o con r\u00f3tulos. Los gigs con v\u00eddeo reciben m\u00e1s pedidos.'],
        ['PDF', 'Un caso de estudio de dos p\u00e1ginas por gig: problema, soluci\u00f3n, cifras y capturas.'],
    ], [24, 76], first_bold=True))
    s.append(CondPageBreak(75 * mm))
    s.append(h3('Capturas que tienes que hacer t\u00fa'))
    s.append(P('No he podido abrir tus webs, as\u00ed que esta lista es lo que falta:'))
    s += bullets([
        'vendet.online: home, ficha de anuncio, asistente de publicaci\u00f3n, chat y tres secciones del panel de administraci\u00f3n.',
        'venezuela-inmuebles.online: mapa con resultados, ficha de inmueble, p\u00e1gina de planes y panel de agencia.',
        'camperocasion.online: home, filtros t\u00e9cnicos, p\u00e1gina de planes, valorador y calculadora de impuestos.',
        'maquinaria.click: home y comparador.',
        'app.khcimport.autos: panel, flota, simulador de importaci\u00f3n y CRM, con datos de ejemplo.',
        'cotizat.online: editor de presupuesto, cat\u00e1logo de partidas y un PDF generado.',
        'remodelat.net: home, una landing de zona, un caso con antes y despu\u00e9s; y el informe Lighthouse.',
        'Tres landings, una por sector, en m\u00f3vil y en escritorio.',
        'Vig\u00eda y MiClaw: la pantalla principal y una pantalla de configuraci\u00f3n.',
    ])

    # ---------------- 08
    s += section('08', 'Antes de publicar: GitHub y riesgos',
                 'Si vas a ense\u00f1ar tu GitHub a compradores, hay cosas que arreglar primero. Algunas son de imagen; otras, de privacidad y de seguridad.')
    s.append(note('El repositorio <font name="Mono">portafolio</font>, donde est\u00e1 guardado este dossier, es p\u00fablico. Esta secci\u00f3n dice d\u00f3nde hay informaci\u00f3n delicada en tus otros repositorios, y el documento incluye tus precios y tu estrategia. Hazlo privado antes de fusionar la rama, o guarda el PDF fuera de GitHub.', kind='warn', title='Este documento tambi\u00e9n es p\u00fablico'))
    s.append(table([
        ['N.\u00ba', 'Qu\u00e9 he encontrado', 'D\u00f3nde', 'Qu\u00e9 hacer'],
        ['1', '<b>CotizaT es ahora público.</b> Es tu producto comercial. Están a la vista el código, el catálogo de partidas con sus precios, tus planes de comercialización, el análisis del embudo con el nombre de dos empresas clientes, el plan de respuesta a incidentes y las auditorías. No tiene archivo de licencia.', 'generador-comercial', 'Volver a hacerlo privado ya. Para Fiverr bastan capturas, un vídeo y las cifras de la ficha P06.'],
        ['2', '<b>Informaci\u00f3n privada en repositorios p\u00fablicos.</b> Tu perfil de fundador, planes de negocio con cifras, estructura de costes, fichas de obras anteriores, una carpeta de documentos legales y el an\u00e1lisis de una nave.', 'RINCOCARABOBO, KHC-Auto-Import (carpeta plan-negocio), KHC-Tienda', 'Hacerlos privados. Si quieres ense\u00f1ar el ERP de KHC, separa el c\u00f3digo del plan de negocio en dos repositorios.'],
        ['3', '<b>Presupuesto de un cliente en PDF</b> en la ra\u00edz del repositorio.', 'reformat-venezuela', 'Borrarlo y limpiarlo tambi\u00e9n del historial: un archivo borrado sigue visible en los commits anteriores.'],
        ['4', '<b>C\u00f3digo de productos en producci\u00f3n abierto,</b> incluidos documentos de seguridad: listado de pol\u00edticas, auditor\u00edas con hallazgos y su correcci\u00f3n.', 'Marketplace-vzla, vendet-inmuebles, camperocasion, maquinaria-ocasion', 'Decide: o privados y ense\u00f1as capturas, o p\u00fablicos sin la documentaci\u00f3n de seguridad. Publicar las debilidades de una web que est\u00e1 en marcha facilita el trabajo a quien quiera atacarla.'],
        ['5', '<b>Perfil de GitHub vac\u00edo:</b> sin nombre, biograf\u00eda, ubicaci\u00f3n ni repositorios fijados.', 'Perfil', 'A\u00f1adir nombre, una l\u00ednea de presentaci\u00f3n, la web y fijar seis repositorios.'],
        ['6', '<b>Descripciones equivocadas o de prueba.</b> Vigia dice "Goofy Burger website"; MiClaw se llama "testing"; Majestic, "Masjestic"; rincon-carabobo, "pagina test".', 'Varios', 'Corregir nombre y descripci\u00f3n. Es lo primero que lee quien entra.'],
        ['7', '<b>README de plantilla o vac\u00edos.</b> Majestic y su variante conservan el texto de create-next-app; los de reformat-houston y reformat-venezuela solo tienen el t\u00edtulo y est\u00e1n mal codificados.', 'Varios', 'Escribir en cada uno: qu\u00e9 es, captura, tecnolog\u00eda, c\u00f3mo arrancarlo y enlace a la web.'],
        ['8', '<b>Landings con nombres de negocios reales</b> y fotos de banco de im\u00e1genes.', '21 repositorios', 'Si fueron propuestas sin encargo, hacerlos privados o cambiar el nombre del negocio. Ver la ficha P15.'],
        ['9', '<b>La web indicada en GitHub es la de Vercel,</b> no el dominio propio.', 'Marketplace-vzla, vendet-inmuebles, camperocasion, maquinaria-ocasion, reformat-venezuela', 'Poner vendet.online, venezuela-inmuebles.online, camperocasion.online, maquinaria.click y remodelat.net.'],
        ['10', '<b>Documento con la marca sustituida en bloque</b> y un dominio de relleno.', 'maquinaria-ocasion (docs)', 'Corregir o retirar.'],
        ['11', '<b>Repositorios vac\u00edos.</b>', 'tumaquinaria, reformat, ProEngineX, dise-o-web', 'Borrar o hacer privados.'],
        ['12', '<b>Archivos sueltos y bancos de precios de terceros.</b> Un archivo .patch, capturas de pantalla, tres Excel de ejemplo con formato de exportación de CYPE y dos bancos BC3 oficiales (22 MB) que el propio LEEME de la carpeta dice que no se versionan.', 'generador-comercial', 'Retirarlos. Comprueba la licencia de cada fuente antes de redistribuirla.'],
    ], [5, 43, 22, 30], mono_cols=(0,)))
    s.append(note([
        'He buscado en los archivos actuales de los 43 repositorios patrones de claves de Stripe, Google y GitHub, tokens de Telegram, claves privadas y tokens JWT, y archivos <font name="Mono">.env</font> subidos. No ha aparecido ninguno.',
        'La b\u00fasqueda no cubre el historial de commits, porque clon\u00e9 solo la \u00faltima versi\u00f3n de cada repositorio. Antes de dar por buena la limpieza, pasa una herramienta como gitleaks sobre el historial completo.'
    ], title='Claves y secretos'))
    s += h2('Qu\u00e9 fijar en el perfil de GitHub', toc=False)
    s.append(P('Seis repositorios que ense\u00f1an amplitud sin exponer nada delicado, una vez limpios:'))
    s.append(table([
        ['Repositorio', 'Qu\u00e9 ense\u00f1a', 'Antes de fijarlo'],
        ['camperocasion o Marketplace-vzla', 'Marketplace completo con pagos', 'Retirar la documentaci\u00f3n de seguridad'],
        ['KHC-Auto-Import', 'ERP y web en un mismo proyecto', 'Sacar la carpeta del plan de negocio'],
        ['reformat-venezuela', 'Web de 273 p\u00e1ginas con SEO local', 'Borrar el PDF del cliente y reescribir el README'],
        ['Vigia', 'Python, v\u00eddeo y aplicaci\u00f3n de escritorio', 'Corregir la descripci\u00f3n'],
        ['testing (MiClaw)', 'Asistente de IA con 11 proveedores', 'Renombrar a miclaw'],
        ['Majestic', 'Dise\u00f1o con animaci\u00f3n y 3D', 'Escribir el README'],
    ], [30, 36, 34], first_bold=True))
    s.append(P('CotizaT no lo fijes: es un producto que vendes, no una muestra de código.', 'small'))
    s += h2('Lo que puedes afirmar y lo que no', toc=False)
    s.append(table([
        ['Puedes decirlo', 'No lo digas'],
        ['"He dise\u00f1ado, programado y lanzado siete productos en 2026."', 'A\u00f1os de experiencia como programador que no puedas documentar.'],
        ['"Cuatro marketplaces en producci\u00f3n con el mismo motor."', 'Cifras de usuarios, tr\u00e1fico o ingresos que no hayas comprobado.'],
        ['"Más de 500.000 líneas de código y 3.300 commits en siete meses."', '"Clientes" para trabajos que fueron propuestas sin encargo.'],
        ['"He dirigido empresas de reformas en Espa\u00f1a."', 'Garant\u00edas de posicionamiento en Google o de financiaci\u00f3n.'],
        ['"Trabajo con herramientas de IA para entregar m\u00e1s r\u00e1pido."', 'Certificaciones o t\u00edtulos que no tengas.'],
        ['"He creado y mantengo un SaaS con empresas de pago." Solo mientras siga siendo cierto.', 'Nombres de tus clientes sin su permiso.'],
        ['Puntuaciones Lighthouse, con el informe a la vista.', 'Tecnolog\u00edas de la lista "no aparece en tus repositorios" de la secci\u00f3n 03.'],
    ], [50, 50]))

    # ---------------- 09
    s += section('09', 'Lo que solo t\u00fa puedes completar',
                 'Datos que no est\u00e1n en ning\u00fan repositorio y que el perfil necesita.')
    s.append(table([
        ['Dato', 'Para qu\u00e9', 'Estado'],
        ['Nombre completo y foto', 'Cabecera del perfil', 'Pendiente'],
        ['Titulaci\u00f3n exacta, centro y a\u00f1o', 'Secci\u00f3n de formaci\u00f3n y la palabra "engineer" de la descripci\u00f3n', 'Pendiente'],
        ['A\u00f1os al frente de empresas de reformas', 'Segunda ocupaci\u00f3n y gigs G03, G09 y G13', 'Pendiente'],
        ['Nivel real de ingl\u00e9s', 'Idiomas del perfil; decide si G09 va solo en espa\u00f1ol', 'Pendiente'],
        ['Qu\u00e9 landings fueron encargos y cu\u00e1les propuestas', 'Qu\u00e9 puedes ense\u00f1ar en el portfolio', 'Pendiente'],
        ['Permiso de los clientes para ense\u00f1ar su trabajo', 'Portfolio', 'Pendiente'],
        ['Horas semanales disponibles', 'Plazos y n\u00famero de pedidos en cola', 'Pendiente'],
        ['Pa\u00eds de residencia y forma de cobro', 'Los m\u00e9todos de retirada dependen del pa\u00eds. Compr\u00faebalo antes de publicar, sobre todo mientras sigas en Venezuela', 'Pendiente'],
        ['Situaci\u00f3n fiscal', 'Los ingresos de Fiverr se declaran. En Espa\u00f1a, una actividad habitual exige alta de aut\u00f3nomo; consulta con tu gestor', 'Pendiente'],
        ['Usuarios, anuncios o ingresos reales de tus productos', 'Si son buenos, son el mejor argumento de venta', 'Pendiente'],
        ['Cifras de CotizaT que quieras dar', 'Tu documento del 2 de noviembre cuenta 41 cuentas y 4 empresas de pago. Decide si lo dices y con qué cifra actual', 'Pendiente'],
    ], [32, 52, 16], first_bold=True))
    s += h2('Pasos siguientes, en orden', toc=False)
    for i, t in enumerate([
        'Limpia GitHub siguiendo la tabla de la secci\u00f3n 08, empezando por las filas 1 a 4.',
        'Completa los datos de la tabla anterior.',
        'Haz las capturas y graba un v\u00eddeo de 60 segundos de VendeT y otro de remodelat.net.',
        'Crea la cuenta de vendedor y pega el perfil de la secci\u00f3n 02.',
        'Publica los cuatro gigs de la ola 1 con sus precios de lanzamiento.',
        'Comprueba cada categor\u00eda y cada l\u00edmite de caracteres en el formulario real, y ajusta.',
        'Contesta todos los mensajes en menos de una hora durante las dos primeras semanas.',
        'Con tres rese\u00f1as, publica la ola 2. Con diez, la ola 3 y sube los precios de la ola 1.',
    ], 1):
        s.append(Paragraph('<font name="Mono-Md" color="#A06F12">%02d</font>&nbsp;&nbsp;%s' % (i, esc(t)), ST['bullet']))

    # ---------------- Anexo A
    s += section('A', 'Anexo: los 44 repositorios',
                 'Los 44 repositorios de la cuenta, con los datos de GitHub del 11 de noviembre de 2026.')
    data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'repos_full.json'), encoding='utf-8'))
    dom = {'generador-comercial': 'cotizat.online', 'Marketplace-vzla': 'vendet.online', 'vendet-inmuebles': 'venezuela-inmuebles.online',
           'camperocasion': 'camperocasion.online', 'maquinaria-ocasion': 'maquinaria.click',
           'KHC-Auto-Import': 'khcimport.autos', 'reformat-venezuela': 'remodelat.net'}
    kind = {}
    for n in ['Marketplace-vzla', 'vendet-inmuebles', 'camperocasion', 'maquinaria-ocasion']:
        kind[n] = 'Marketplace'
    for n in ['reformat-venezuela', 'reformat-houston', 'RemodelaT-Galicia']:
        kind[n] = 'Web Astro'
    for n in ['REFORMATNEW', 'Majestic', 'majesticweb-sandbox', 'rincon-carabobo']:
        kind[n] = 'Web Next.js'
    kind.update({'generador-comercial': 'SaaS', 'KHC-Auto-Import': 'ERP y web', 'Vigia': 'App Python', 'testing': 'App Python',
                 'KHC-Tienda': 'Plan de negocio', 'RINCOCARABOBO': 'Plan de negocio',
                 'ProEngineX': 'Sin contenido', 'dise-o-web': 'Sin contenido', 'tumaquinaria': 'Vac\u00edo',
                 'reformat': 'Vac\u00edo', 'portafolio': 'Este dossier'})
    order = ['SaaS', 'Marketplace', 'ERP y web', 'Web Astro', 'Web Next.js', 'App Python', 'Plan de negocio', 'Landing HTML',
             'Este dossier', 'Sin contenido', 'Vac\u00edo']
    rows = []
    for r in data:
        k = kind.get(r['name'], 'Landing HTML')
        web = dom.get(r['name']) or (r['homepageUrl'] or '').replace('https://', '') or '\u2013'
        rows.append((order.index(k), -r['commits'], [r['name'], k, str(r['commits']), r['createdAt'][:10], r['pushedAt'][:10], web]))
    rows.sort(key=lambda x: (x[0], x[1]))
    tbl = [['Repositorio', 'Tipo', 'Commits', 'Creado', 'Cambio', 'Web']]
    tbl += [r[2] for r in rows]
    s.append(table(tbl, [21, 13, 9, 12, 12, 33], mono_cols=(2, 3, 4, 5), first_bold=True))

    # ---------------- Anexo B
    s += section('B', 'Anexo: palabras clave por gig',
                 'T\u00e9rminos de b\u00fasqueda en ingl\u00e9s para repartir entre el t\u00edtulo, la descripci\u00f3n y las preguntas frecuentes, sin repetirlos de forma artificial.')
    s.append(table([
        ['Gig', 'T\u00e9rminos'],
        ['G01', 'marketplace website, classifieds website, listing website, multi vendor, buy and sell platform, OLX clone, Craigslist style, real estate portal, Next.js developer, Supabase developer'],
        ['G02', 'landing page design, one page website, small business website, salon website, clinic website, restaurant website, real estate landing page, responsive website, video hero'],
        ['G03', 'contractor website, remodeling website, construction website, local SEO website, service area pages, Astro developer, fast website, plumber website, electrician website'],
        ['G04', 'Supabase expert, Postgres database, database schema, RLS policies, Supabase auth, Supabase storage, SQL functions, backend developer, database security'],
        ['G05', 'Stripe integration, Stripe subscriptions, Stripe checkout, Stripe webhooks, SaaS billing, recurring payments, customer portal, payment gateway'],
        ['G06', 'technical SEO audit, website audit, Core Web Vitals, page speed, schema markup, hreflang, sitemap, canonical, indexing issues, Lighthouse'],
        ['G07', 'admin panel, dashboard, CRM development, custom ERP, internal tools, business software, inventory management, back office, React dashboard'],
        ['G08', 'web scraping, data scraping, Python scraper, data extraction, price monitoring, competitor prices, lead list, data collection'],
        ['G09', 'business plan writer, financial projections, startup business plan, bank loan business plan, pitch, feasibility study, financial forecast'],
        ['G10', 'AI integration, AI chatbot, custom chatbot, RAG chatbot, LLM integration, AI agent, Gemini API, Ollama, OpenAI API, AI assistant'],
        ['G11', 'fix Next.js bug, React bug fix, Vercel deployment, build error, hydration error, deploy website, website fix, TypeScript error'],
        ['G12', 'IP camera software, CCTV software, NVR, RTSP stream, ONVIF, motion detection, OpenCV, object detection, security camera app'],
        ['G13', 'construction cost estimate, renovation estimate, quantity takeoff, bill of quantities, BOQ, remodeling budget, material takeoff'],
        ['G14', 'SaaS development, SaaS MVP, startup MVP, FastAPI developer, Python web app, multi tenant, subscription app, Stripe billing, Supabase, web app development'],
    ], [8, 92], mono_cols=(0,)))

    # ---------------- Anexo C
    s += section('C', 'Anexo: plantillas de mensajes',
                 'Respuestas en ingl\u00e9s para las situaciones m\u00e1s frecuentes. C\u00e1mbialas con tus palabras: los mensajes id\u00e9nticos se notan.')
    msgs = [
        ('Primera respuesta a una consulta', "Hi, thanks for writing. I have read your message and this is something I can do.\n\nTo give you an exact price and delivery date I need three things:\n1. A short description of what the site or app must do\n2. One or two examples you like\n3. Your deadline\n\nI usually reply within a few hours."),
        ('Preguntas para cerrar el alcance', "Before I send you an offer, let me confirm the scope:\n- Pages or screens: \n- Main features: \n- Languages: \n- Payments: yes or no\n- Content: you provide it, or I write it\n- Hosting and domain: in your accounts\n\nIf this is right, I will send a custom offer with the price and the delivery date."),
        ('Texto de una oferta personalizada', "Custom offer: [project name]\n\nIncluded:\n- [item 1]\n- [item 2]\n- [item 3]\n\nNot included: [what is out of scope]\n\nDelivery: [n] days, in [n] milestones. You receive the source code in your own GitHub and a deployment on your accounts."),
        ('Falta informaci\u00f3n para empezar', "Thanks for your order. To start I still need: [list].\n\nThe delivery time starts when I have everything, so the sooner you send it, the sooner you get the result."),
        ('Mensaje de entrega', "Your project is ready.\n\n- Live preview: [link]\n- Source code: [repository]\n- Short video walkthrough: attached\n- One page guide: attached\n\nPlease check it and tell me if anything needs adjusting. Revisions are included as described in the package."),
        ('Rechazar un encargo que no encaja', "Thanks for thinking of me. This project is outside what I do well, so I prefer not to take it rather than deliver something average.\n\nWhat I can help with is [related service]. If that is useful, tell me and we can look at it."),
        ('El cliente pide algo fuera del alcance', "I can do that. It was not part of the original order, so I will send you an extra for it: [price], adding [n] days to the delivery. If you prefer to keep the original scope, we continue as planned."),
    ]
    for title, text in msgs:
        s += paste(title + ' (EN)', text)
    return s
