# Proyectos para LinkedIn

Textos listos para pegar en LinkedIn de los cinco proyectos: CotizaT, CamperOcasión, MaquinariaOcasión, Venezuela Inmuebles y KHC Auto Import. Cada uno va en español y en inglés.

Las cifras están contadas sobre el código de cada repositorio el 11 de noviembre de 2026.

## Cómo añadirlos

1. En tu perfil, pulsa **Añadir sección al perfil** y busca **Añadir proyecto** (suele estar dentro de «Recomendado»).
2. Pega el **nombre** y la **descripción** de cada bloque. Los bloques de texto tienen un botón de copiar arriba a la derecha.
3. En las fechas, pon el mes de inicio que indico y marca **«Actualmente trabajo en este proyecto»**.
4. Añade las **aptitudes** indicadas y, en **Contenido multimedia**, el enlace de la web y dos o tres capturas.
5. En **Asociado con**, elige el puesto de la sección «Experiencia» de más abajo, si lo creas.

Los límites y los nombres de los menús son los que conozco de LinkedIn y no los he podido comprobar desde aquí: 2.000 caracteres en la descripción y cinco aptitudes por proyecto. Si el formulario te deja añadir más aptitudes, usa las de la línea «Otras».

Para tener el perfil en los dos idiomas, LinkedIn permite crear un segundo perfil en inglés desde **Añadir perfil en otro idioma**. Si solo vas a tener uno, usa el español si buscas clientes en España y Latinoamérica, y el inglés si buscas trabajo en remoto.

## Orden recomendado

| N.º | Proyecto | Por qué en ese lugar |
|---|---|---|
| 1 | CotizaT | Es el más grande y tiene clientes de pago |
| 2 | CamperOcasión | Marketplace completo con suscripciones por Stripe |
| 3 | KHC Auto Import | Enseña otra cosa distinta: software de gestión interna |
| 4 | Venezuela Inmuebles | Mapa, inteligencia artificial y cobro adaptado al país |
| 5 | MaquinariaOcasión | Refuerza a CamperOcasión: el motor es reutilizable |

LinkedIn suele ordenar los proyectos por fecha, así que este orden sirve sobre todo para la sección **Destacado**: fija ahí los enlaces de CotizaT, CamperOcasión y KHC Auto Import.

---

## 1. CotizaT

| Campo | Valor |
|---|---|
| Fechas | ago. 2026 – actualidad (en inglés: Aug 2026 – Present) |
| Enlace | https://cotizat.online |
| Aptitudes | Python · FastAPI · PostgreSQL · Stripe · SaaS |
| Otras | SQLAlchemy, Supabase, Gestión de producto, SEO |
| Capturas | Editor de presupuestos, medición sobre plano, un PDF generado y la página de precios. |

**Nombre del proyecto (español)**

```text
CotizaT · SaaS de presupuestos de obra para construcción y reformas
```

**Descripción (español)** · 1570 de 2.000 caracteres

```text
CotizaT es un SaaS con el que constructoras y empresas de reformas preparan presupuestos de obra profesionales: capítulos, partidas, mediciones, costes, márgenes y un PDF con su marca. Está en producción en cotizat.online y ya tiene sus primeras empresas de pago.

Proyecto propio. Llevo el producto, el diseño, el desarrollo, el catálogo de precios y la operación.

Qué hace:
• Editor por capítulos y partidas con mediciones, costes internos, márgenes, versiones y plantillas.
• PDF profesional con portada, firma del cliente, anexos y la marca de cada empresa.
• Medición sobre planos: se calibra la escala y se miden longitudes, áreas y conteos, con exportación a DXF.
• Importación y exportación BC3 (FIEBDC-3) e importación de descompuestos desde Excel.
• Catálogo de partidas con su descompuesto y precios de referencia investigados para 18 países.
• Multiempresa: organizaciones, miembros e invitaciones, con los datos de cada empresa aislados.
• Suscripciones con Stripe, prueba gratuita y licencias, y cobro manual donde Stripe no opera.
• Asistente que revisa el presupuesto, calcula mediciones y avisa de lo que falta en el alcance.
• 23 países configurados con su moneda y sus impuestos, en español e inglés.
• Web pública con páginas de precios por país y comparador internacional.
• Panel de operación para ventas, cobros, renovaciones y soporte.

En cifras: 98.000 líneas de Python, 378 rutas, más de 2.600 tests automatizados y 69 migraciones de base de datos.

Tecnología: Python, FastAPI, SQLAlchemy, PostgreSQL en Supabase, Stripe, ReportLab y Vercel.
```

**Project name (English)**

```text
CotizaT · Construction and renovation estimating SaaS
```

**Description (English)** · 1533 de 2.000 caracteres

```text
CotizaT is a SaaS that lets builders and renovation companies prepare professional construction estimates: chapters, work items, measurements, costs, margins and a branded PDF. It is live at cotizat.online and already has its first paying companies.

My own product. I handle product, design, development, the price catalogue and operations.

What it does:
• Estimate editor by chapters and work items, with measurements, internal costs, margins, versions and templates.
• Professional PDF with cover, client signature, annexes and each company's branding.
• Takeoff on drawings: calibrate the scale and measure lengths, areas and counts, with DXF export.
• BC3 (FIEBDC-3) import and export, and import of cost breakdowns from Excel.
• Catalogue of work items with cost breakdowns and researched reference prices for 18 countries.
• Multi-tenant: organizations, members and invitations, with each company's data isolated.
• Stripe subscriptions, free trial and licences, plus manual payment where Stripe does not operate.
• Assistant that reviews the estimate, calculates measurements and flags missing scope.
• 23 countries configured with their currency and taxes, in Spanish and English.
• Public site with price pages by country and an international price comparison.
• Operations panel for sales, payments, renewals and support.

In numbers: 98,000 lines of Python, 378 routes, more than 2,600 automated tests and 69 database migrations.

Stack: Python, FastAPI, SQLAlchemy, PostgreSQL on Supabase, Stripe, ReportLab and Vercel.
```

---

## 2. CamperOcasión

| Campo | Valor |
|---|---|
| Fechas | sept. 2026 – actualidad (en inglés: Sep 2026 – Present) |
| Enlace | https://camperocasion.online |
| Aptitudes | Next.js · TypeScript · Supabase · Stripe · PostgreSQL |
| Otras | SEO, React, Tailwind CSS, Vercel |
| Capturas | Home, buscador con filtros técnicos, página de planes, valorador y calculadora de impuestos. |

**Nombre del proyecto (español)**

```text
CamperOcasión · Marketplace de campers y autocaravanas de ocasión en España
```

**Descripción (español)** · 1500 de 2.000 caracteres

```text
CamperOcasión es un marketplace de compraventa de campers y autocaravanas de segunda mano para el mercado español. Lo usan particulares y vendedores profesionales, que tienen tienda propia y suscripción. Está en producción en camperocasion.online.

Proyecto propio: producto, diseño, desarrollo y puesta en producción.

Qué hace:
• Publicación de anuncios con 16 filtros técnicos propios del sector y búsqueda avanzada.
• Tiendas de vendedores profesionales con URL propia, importación del stock por CSV y páginas por marca y modelo.
• Suscripción profesional con Stripe, mensual o anual: portal del cliente, gestión de impagos, cupones y prueba gratuita de 30 días.
• Chat entre comprador y vendedor, y créditos para destacar anuncios con pago por Bizum, transferencia o PayPal.
• Valorador «¿cuánto vale mi camper?» y calculadora del impuesto de transmisiones por comunidad autónoma.
• Contrato de compraventa generado, reservas, inspecciones y servicio de gestoría.
• Dossier de homologación de cada vehículo, guardado en almacenamiento privado.
• SEO programático: páginas por provincia y categoría con datos reales del mercado y datos estructurados.
• Analítica propia y panel de rendimiento para cada vendedor.
• Panel de administración y moderación de anuncios.

En cifras: 64.000 líneas de TypeScript, 112 rutas de API, 31 tablas, 216 políticas de seguridad a nivel de fila y 86 archivos de test.

Tecnología: Next.js, TypeScript, React, Tailwind CSS, PostgreSQL en Supabase, Stripe y Vercel.
```

**Project name (English)**

```text
CamperOcasión · Marketplace for used campervans and motorhomes in Spain
```

**Description (English)** · 1360 de 2.000 caracteres

```text
CamperOcasión is a marketplace for buying and selling used campervans and motorhomes in Spain. It serves private sellers and professional dealers, who get their own storefront and a subscription. It is live at camperocasion.online.

My own product: product, design, development and launch.

What it does:
• Listings with 16 technical filters specific to the sector and advanced search.
• Dealer storefronts with their own URL, stock import by CSV and pages by make and model.
• Professional subscription with Stripe, monthly or yearly: customer portal, failed payment handling, coupons and a 30 day free trial.
• Chat between buyer and seller, and credits to feature listings paid by Bizum, bank transfer or PayPal.
• "What is my camper worth?" valuation tool and a transfer tax calculator for each Spanish region.
• Generated sales contract, reservations, inspections and paperwork service.
• Homologation file for each vehicle, kept in private storage.
• Programmatic SEO: pages by province and category with real market data and structured data.
• In-house analytics and a performance panel for each seller.
• Admin panel and listing moderation.

In numbers: 64,000 lines of TypeScript, 112 API routes, 31 tables, 216 row level security policies and 86 test files.

Stack: Next.js, TypeScript, React, Tailwind CSS, PostgreSQL on Supabase, Stripe and Vercel.
```

---

## 3. KHC Auto Import

| Campo | Valor |
|---|---|
| Fechas | may. 2026 – actualidad (en inglés: May 2026 – Present) |
| Enlace | https://khcimport.autos |
| Aptitudes | React · Supabase · Python · ERP · Next.js |
| Otras | PostgreSQL, Web scraping, Análisis de datos, Fiscalidad |
| Capturas | Cuadro de mando, tablero de la flota, simulador de importación y la web pública. Con datos de ejemplo. |

**Nombre del proyecto (español)**

```text
KHC Auto Import · ERP a medida y web para un negocio de importación de vehículos
```

**Descripción (español)** · 1583 de 2.000 caracteres

```text
KHC Auto Import es un negocio de importación de vehículos desde Alemania a Galicia. Diseñé y desarrollé todo su software: un ERP interno que cubre la operación completa y la web pública, que se alimenta del ERP.

El ERP, con 16 módulos:
• Cuadro de mando: caja, capital inmovilizado en stock, beneficio, impuestos pendientes y previsión de cobros y pagos a 90 días.
• Flota: cada vehículo recorre un flujo de 10 estados, de la prospección a la entrega, con su coste real, su documentación y su margen neto.
• Simulador de importación: calcula si una operación es rentable antes de comprar.
• Motor fiscal español: impuesto de matriculación (modelo 576), ITP (modelo 620), IVTM, régimen de bienes usados y calendario de obligaciones.
• Catálogo de 1.104 variantes de 37 marcas, con fiabilidad del motor y precios estimados de compra y de venta.
• CRM, oportunidades y contactos que llegan desde la web.
• Contabilidad, facturación, documentos, informes y exportación a CSV.
• Lista de inspección precompra y calculadora de viajes con mapa.
• Cuatro roles de usuario (propietario, gestor, comercial y gestoría), con permisos aplicados en la base de datos.

La web pública: el stock se publica desde el ERP en un clic, sin exponer costes ni datos internos.

Datos de mercado: programas en Python que recogen precios de tres portales de Alemania y España, y un modelo de regresión que estima el precio de venta (R² de 0,89).

En cifras: 62.000 líneas de código en el ERP y 13.000 líneas de Python.

Tecnología: React, Vite, Next.js, Tailwind CSS, PostgreSQL en Supabase, Python y Vercel.
```

**Project name (English)**

```text
KHC Auto Import · Custom ERP and website for a vehicle import business
```

**Description (English)** · 1542 de 2.000 caracteres

```text
KHC Auto Import is a business that imports vehicles from Germany to Galicia, Spain. I designed and built all of its software: an internal ERP that covers the whole operation and the public website, which is fed from the ERP.

The ERP, with 16 modules:
• Dashboard: cash, capital tied up in stock, profit, pending taxes and a 90 day forecast of payments in and out.
• Fleet: each vehicle moves through a 10 stage workflow, from prospecting to delivery, with its real cost, paperwork and net margin.
• Import simulator: works out whether a deal is profitable before buying.
• Spanish tax engine: registration tax (form 576), transfer tax (form 620), road tax, the used goods VAT scheme and a calendar of filings.
• Catalogue of 1,104 variants from 37 makes, with engine reliability and estimated purchase and sale prices.
• CRM, opportunities and leads coming in from the website.
• Accounting, invoicing, documents, reports and CSV export.
• Pre-purchase inspection checklist and a trip calculator with map.
• Four user roles (owner, manager, sales and external accountant), with permissions enforced in the database.

The public website: stock is published from the ERP in one click, without exposing costs or internal data.

Market data: Python programs that collect prices from three portals in Germany and Spain, and a regression model that estimates the sale price (R² of 0.89).

In numbers: 62,000 lines of code in the ERP and 13,000 lines of Python.

Stack: React, Vite, Next.js, Tailwind CSS, PostgreSQL on Supabase, Python and Vercel.
```

---

## 4. Venezuela Inmuebles

| Campo | Valor |
|---|---|
| Fechas | jul. 2026 – actualidad (en inglés: Jul 2026 – Present) |
| Enlace | https://venezuela-inmuebles.online |
| Aptitudes | Next.js · TypeScript · Supabase · PostgreSQL · Inteligencia artificial |
| Otras | Leaflet, OCR, Google Gemini, SEO |
| Capturas | Mapa con resultados, ficha de un inmueble, página de planes y panel de agencia. |

**Nombre del proyecto (español)**

```text
Venezuela Inmuebles · Portal inmobiliario con mapa, planes para agencias e IA
```

**Descripción (español)** · 1293 de 2.000 caracteres

```text
Venezuela Inmuebles es un portal de venta y alquiler de inmuebles para el mercado venezolano, con planes de pago para profesionales y agencias. Está en producción en venezuela-inmuebles.online.

Proyecto propio: producto, diseño, desarrollo y puesta en producción.

Qué hace:
• Búsqueda sobre mapa interactivo, con agrupación de resultados y filtro por zona.
• Planes Gratuito, Profesional y Agencia. Las agencias gestionan su equipo, sus invitaciones y su cartera de inmuebles.
• Cobro adaptado al país: el usuario sube el justificante de Pago Móvil o Binance y el sistema lo lee con OCR, lo valida y bloquea su reutilización.
• Mejora de la descripción del anuncio con inteligencia artificial (Gemini), con modelos de reserva si el primero falla.
• Agenda de visitas, comparador de inmuebles y estimador financiero en dólares y bolívares.
• Búsquedas guardadas con alertas y resúmenes por correo.
• Escaparate propio para cada vendedor.
• SEO: páginas por operación, estado y ciudad.
• Monitor interno de errores y analítica del embudo de conversión.

En cifras: 54.000 líneas de TypeScript, 72 rutas de API, 36 tablas, 96 políticas de seguridad a nivel de fila y 70 funciones SQL.

Tecnología: Next.js, TypeScript, React, PostgreSQL en Supabase, Leaflet, Gemini, OCR con Tesseract y Vercel.
```

**Project name (English)**

```text
Venezuela Inmuebles · Real estate portal with map search, agency plans and AI
```

**Description (English)** · 1166 de 2.000 caracteres

```text
Venezuela Inmuebles is a property portal for sales and rentals in Venezuela, with paid plans for professionals and agencies. It is live at venezuela-inmuebles.online.

My own product: product, design, development and launch.

What it does:
• Search on an interactive map, with result clustering and filtering by area.
• Free, Professional and Agency plans. Agencies manage their team, invitations and property portfolio.
• Payments adapted to the country: the user uploads a Pago Móvil or Binance receipt and the system reads it with OCR, validates it and blocks reuse.
• AI improvement of listing descriptions (Gemini), with fallback models if the first one fails.
• Viewing schedule, property comparison and a financial estimator in dollars and bolívares.
• Saved searches with alerts and email digests.
• A storefront for each seller.
• SEO: pages by operation, state and city.
• Internal error monitor and conversion funnel analytics.

In numbers: 54,000 lines of TypeScript, 72 API routes, 36 tables, 96 row level security policies and 70 SQL functions.

Stack: Next.js, TypeScript, React, PostgreSQL on Supabase, Leaflet, Gemini, OCR with Tesseract and Vercel.
```

---

## 5. MaquinariaOcasión

| Campo | Valor |
|---|---|
| Fechas | oct. 2026 – actualidad (en inglés: Oct 2026 – Present) |
| Enlace | https://maquinaria.click |
| Aptitudes | Next.js · TypeScript · Supabase · PostgreSQL · SEO |
| Otras | Arquitectura de software, React, Stripe, Vercel |
| Capturas | Home, comparador de máquinas, tasador y una página de marca. |

**Nombre del proyecto (español)**

```text
MaquinariaOcasión · Marketplace B2B de maquinaria de ocasión
```

**Descripción (español)** · 1281 de 2.000 caracteres

```text
MaquinariaOcasión es un marketplace de compraventa de maquinaria de ocasión entre empresas. Está en producción en maquinaria.click.

Lo construí sobre el motor de marketplace que desarrollé para CamperOcasión. Para ello creé una herramienta que clona un vertical completo a partir de un único archivo de marca: nombre, dominio, textos y categorías. Con ella, el nuevo marketplace salió en cuatro días.

Proyecto propio: arquitectura, desarrollo y puesta en producción.

Qué hace:
• Publicación y búsqueda de maquinaria con categorías y filtros propios del sector.
• Tiendas de vendedores profesionales, planes de suscripción y chat con el comprador.
• Comparador de máquinas y tasador.
• Páginas por marca, foro y vídeos incrustados en los anuncios.
• SEO técnico: 384 páginas generadas en la compilación, sitemaps, datos estructurados y aviso automático a los buscadores con IndexNow.
• Panel de administración y moderación.

Qué demuestra: que el marketplace es un motor reutilizable. La identidad de la marca vive en un solo módulo, así que lanzar un sector nuevo es cuestión de días y no de meses.

En cifras: 59.000 líneas de TypeScript, 107 rutas de API, 34 tablas y 72 archivos de test.

Tecnología: Next.js, TypeScript, React, Tailwind CSS, PostgreSQL en Supabase y Vercel.
```

**Project name (English)**

```text
MaquinariaOcasión · B2B marketplace for used machinery
```

**Description (English)** · 1151 de 2.000 caracteres

```text
MaquinariaOcasión is a B2B marketplace for buying and selling used machinery. It is live at maquinaria.click.

I built it on the marketplace engine I developed for CamperOcasión. To do that I wrote a tool that clones a complete vertical from a single brand file: name, domain, copy and categories. With it, the new marketplace was launched in four days.

My own product: architecture, development and launch.

What it does:
• Machinery listings and search with categories and filters specific to the sector.
• Dealer storefronts, subscription plans and chat with buyers.
• Machine comparison and valuation tools.
• Pages by brand, a forum and embedded videos in listings.
• Technical SEO: 384 pages generated at build time, sitemaps, structured data and automatic search engine notification with IndexNow.
• Admin panel and moderation.

What it shows: the marketplace is a reusable engine. Brand identity lives in a single module, so launching a new sector takes days, not months.

In numbers: 59,000 lines of TypeScript, 107 API routes, 34 tables and 72 test files.

Stack: Next.js, TypeScript, React, Tailwind CSS, PostgreSQL on Supabase and Vercel.
```

---

## Puesto para la sección «Experiencia»

Los proyectos lucen más si cuelgan de un puesto. Como son productos tuyos, crea uno así y asocia a él los cinco proyectos.

| Campo | Valor |
|---|---|
| Cargo | Fundador y desarrollador de producto (en inglés: Founder & Product Developer) |
| Tipo de empleo | Autónomo |
| Empresa | Proyectos propios, o el nombre comercial que uses |
| Fechas | abr. 2026 – actualidad |

**Descripción (español)** · 868 de 2.000 caracteres

```text
Diseño, desarrollo y lanzo productos de software propios, de la idea a la producción: marketplaces, SaaS y herramientas internas de gestión.

En 2026 he puesto en producción:
• CotizaT, un SaaS de presupuestos de obra para constructoras y empresas de reformas.
• Cuatro marketplaces sobre un mismo motor: clasificados, inmuebles, campers y maquinaria.
• Un ERP completo para un negocio de importación de vehículos.
• Webs de empresas de reformas con SEO local para Venezuela y Estados Unidos.

Me ocupo de todo el ciclo: producto, base de datos, pagos, panel de administración, SEO, pruebas automatizadas y despliegue. Trabajo con Next.js, TypeScript, Python, FastAPI, PostgreSQL en Supabase y Stripe.

Antes de programar dirigí empresas de reformas, y eso se nota en lo que construyo: software pensado para negocios reales, con sus costes, sus impuestos y sus plazos.
```

**Description (English)** · 797 de 2.000 caracteres

```text
I design, build and launch my own software products, from idea to production: marketplaces, SaaS and internal business tools.

In 2026 I shipped:
• CotizaT, a construction estimating SaaS for builders and renovation companies.
• Four marketplaces on one shared engine: classifieds, real estate, campervans and machinery.
• A complete ERP for a vehicle import business.
• Renovation company websites with local SEO for Venezuela and the United States.

I cover the whole cycle: product, database, payments, admin panel, SEO, automated tests and deployment. I work with Next.js, TypeScript, Python, FastAPI, PostgreSQL on Supabase and Stripe.

Before writing software I ran renovation companies, and it shows in what I build: software made for real businesses, with their costs, taxes and deadlines.
```

---

## Antes de publicar

- **CotizaT, «primeras empresas de pago».** Sale de tu documento del 2 de noviembre, que cuenta 4 empresas de pago. Deja la frase solo mientras sea cierta y no nombres a los clientes sin su permiso.
- **KHC Auto Import.** Lo describo como un negocio de importación porque así aparece en tus documentos. Si todavía no ha empezado a operar, cambia la primera frase por «KHC Auto Import es un proyecto de negocio de importación de vehículos…».
- **Puesto de «Experiencia».** La fecha de abril de 2026 es la del primer repositorio. La frase sobre las empresas de reformas viene de tu perfil de fundador; ajusta el texto a tu trayectoria real y añade esas empresas como puestos anteriores.
- **«Proyecto propio».** Así lo has indicado tú. Si en alguno participó otra persona, añádela en el campo de colaboradores.
- **Capturas.** No he podido abrir las webs, así que no hay imágenes. Un proyecto con dos o tres capturas recibe mucha más atención que uno con solo texto. En KHC usa datos de ejemplo.
- **Repositorios.** No enlaces el código de CotizaT ni el de los marketplaces: enlaza las webs. En LinkedIn interesa el producto, no el repositorio.
- **Webs en marcha.** Comprueba que los cinco dominios cargan bien antes de enlazarlos.
