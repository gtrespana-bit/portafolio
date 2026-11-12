# -*- coding: utf-8 -*-
from lib import *

GIGS = [
 dict(tag='G01', es='Marketplace o web de clasificados con Next.js y Supabase',
  en='I will build a classifieds marketplace web app with Next.js and Supabase',
  cat='Programming & Tech > Website Development > Custom Websites. Alternativa: Software Development > Web Applications',
  tags=['marketplace', 'nextjs', 'supabase', 'classifieds website', 'web application'],
  proof='P01, P02, P03, P04',
  desc="""I build classifieds and marketplace platforms that are ready for real users, not demos.

I have designed and launched four marketplaces myself: general classifieds, real estate, campervans and industrial machinery. You get the same architecture.

What I can build for you:
- Listings with photos, categories, filters and full text search
- Sign up, login and seller profiles
- Real time chat between buyers and sellers
- Favourites, saved searches and price alerts
- Reviews, reports and moderation tools
- Admin panel for users, listings and payments
- Featured listings, credits or subscription plans
- SEO pages by city and category, sitemap and structured data
- Mobile first design, installable as an app

Stack: Next.js, TypeScript, Tailwind, Supabase (Postgres, Auth, Storage, Realtime) and Vercel. The database is protected with row level security.

You receive the full source code in your own GitHub, the database migrations and a deployment on your own accounts.

Please message me before ordering so I can confirm scope and timing.""",
  packs=[('Starter', 'Listings, categories, search, sign up, seller profile, basic admin. Up to 6 page types.', '14 d\u00edas', '2', '450', '900'),
         ('Marketplace', 'Starter plus chat, favourites, reviews, moderation, full admin panel and SEO pages.', '25 d\u00edas', '3', '1.100', '2.200'),
         ('Complete', 'Marketplace plus payments or subscriptions, alerts, emails, two languages and PWA.', '40 d\u00edas', '4', '2.400', '4.500')],
  extras=['Segundo idioma: 150 $', 'Stripe o cobro con justificante: 300 $', 'Bot de Telegram para moderar: 120 $', 'Un mes de soporte tras la entrega: 200 $'],
  faq=[('Do I own the code?', 'Yes. The repository, the database and the hosting are created in your accounts. There is no licence fee.'),
       ('Can you adapt it to my niche and country?', 'Yes. Categories, filters, currency, language and legal pages are configured for your market. I have done this for four different sectors.'),
       ('What are the monthly costs?', 'Vercel and Supabase have free tiers that are enough to start. I explain the limits and the cost of the next tier before launch.'),
       ('Do you build mobile apps?', 'I build responsive web apps that can be installed on the phone as a PWA. I do not build native iOS or Android apps.')],
  reqs=['What is sold on your marketplace and in which country', 'Three reference sites you like', 'Categories and the main filters for each one', 'How you plan to make money: free, featured listings, subscriptions', 'Logo and brand colours, if you have them'],
  nota='Es tu gig de mayor valor. Im\u00e1genes: una composici\u00f3n con los cuatro marketplaces, una captura del panel de administraci\u00f3n y un v\u00eddeo de 60 segundos recorriendo la publicaci\u00f3n de un anuncio. Empieza cada pedido grande con una oferta personalizada por hitos.'),

 dict(tag='G02', es='Landing page premium para un negocio local',
  en='I will design and code a premium landing page for your local business',
  cat='Programming & Tech > Website Development > Landing Pages',
  tags=['landing page', 'business website', 'html css', 'responsive design', 'website design'],
  proof='P14, P15, P10',
  desc="""I design and code landing pages that look premium, load fast and bring you calls, bookings or leads.

I have built more than 20 landing pages for sectors such as beauty, clinics, real estate and restaurants, plus full websites for renovation companies.

What you get:
- A custom one page design, not a template
- Hero section with video or image
- Services, gallery, reviews, team and contact sections
- Contact or booking form and WhatsApp button
- Mobile first, responsive layout
- Smooth scroll animations
- Basic SEO: titles, descriptions, structured data and social preview image
- Deployment on your domain

Options: two to five languages, a simple panel to edit your own texts and prices, Google Maps, menu or price list.

I write clean HTML, CSS and JavaScript, or Astro and Next.js when the project needs it. No page builders and no monthly fees.

Send me your business name, what you offer and two or three websites you like, and I will tell you which package fits.""",
  packs=[('Essential', 'One page, 5 sections, contact form, WhatsApp button, responsive, deployed.', '3 d\u00edas', '2', '80', '150'),
         ('Premium', 'One page, 8 sections, video hero, animations, booking form, SEO basics, 2 languages.', '5 d\u00edas', '3', '180', '350'),
         ('Signature', 'Premium plus content editing panel, up to 4 languages, advanced animation or 3D.', '8 d\u00edas', '4', '350', '700')],
  extras=['Idioma adicional: 40 $', 'Entrega en 48 horas: 50 $', 'Textos escritos por ti: 60 $', 'Panel para editar contenidos: 120 $'],
  faq=[('Do you use templates or page builders?', 'No. Each page is coded by hand, which makes it faster and free of monthly plugin fees.'),
       ('Can I edit the content myself later?', 'Yes, with the Signature package or the content panel extra. Otherwise I send you clear instructions to change texts and images.'),
       ('Do you provide hosting and domain?', 'I deploy on Vercel, which is free for this kind of site, and connect your domain. You buy the domain in your own name.'),
       ('Do you write the texts?', 'You send the content, or you add the copywriting extra and I write it from a short questionnaire.')],
  reqs=['Business name, sector and city', 'Services or products with prices if you show them', 'Logo, photos and video, or permission to use stock images', 'Two or three websites you like', 'Contact details and opening hours'],
  nota='Gig de entrada: pedidos r\u00e1pidos que traen las primeras rese\u00f1as. Im\u00e1genes: tres composiciones, una por sector (est\u00e9tica, cl\u00ednica, inmobiliaria), con el m\u00f3vil y el escritorio. Usa solo dise\u00f1os con permiso o con nombre ficticio.'),

 dict(tag='G03', es='Web r\u00e1pida en Astro con SEO local para empresas de servicios',
  en='I will build a fast Astro website with local SEO pages for contractors',
  cat='Programming & Tech > Website Development > Business Websites',
  tags=['astro', 'local seo', 'contractor website', 'business website', 'static website'],
  proof='P07, P08, P09',
  desc="""Most local business websites are slow and have one generic page. I build fast static sites where every service and every area you cover has its own page, so Google can match you with local searches.

I ran renovation companies in Spain and I built the websites for my own remodeling businesses in three countries. One of them has more than 270 pages in two languages.

What you get:
- Astro website: static, secure and very fast
- Home, services, projects, about and contact pages
- Location pages for the towns or neighbourhoods you serve
- Before and after project galleries
- Local business structured data, sitemap and canonical tags
- Blog ready for articles, with RSS
- Contact form, click to call and WhatsApp
- Automatic checks that stop publishing if a link or a meta tag is broken
- Deployment on Vercel with your domain

Best for contractors, remodelers, plumbers, electricians, cleaners, clinics and any business that works by area.

I do not promise rankings. I deliver the technical base that makes ranking possible.""",
  packs=[('Local', '5 pages, 3 services, contact form, structured data, sitemap, deployed.', '7 d\u00edas', '2', '250', '450'),
         ('Local Pro', '15 pages: services, 8 location pages, 3 project cases, blog, SEO checks.', '12 d\u00edas', '3', '600', '1.100'),
         ('Regional', '40+ pages: services by location, bilingual, blog with 5 articles, PWA, IndexNow.', '20 d\u00edas', '4', '1.200', '2.400')],
  extras=['Cinco landings de zona adicionales: 100 $', 'Segundo idioma completo: 250 $', 'Tres art\u00edculos de blog: 120 $', 'Alta en Search Console y env\u00edo de sitemaps: 40 $'],
  faq=[('Why Astro and not WordPress?', 'Astro generates static pages: nothing to hack, nothing to update and top speed scores. One of my Astro sites scores 98 to 100 in Lighthouse performance.'),
       ('Will each location page have unique content?', 'Yes. Each page uses data about the area, its own projects and its own questions. I do not publish copies with only the city name changed.'),
       ('Can I add pages myself?', 'Yes. Pages and articles are simple files. I show you how, or you can order updates from me.'),
       ('Do you guarantee first page on Google?', 'No one can honestly guarantee that. I guarantee a technically correct, fast site with the right structure for local search.')],
  reqs=['Services you offer and the areas you cover', 'Photos of real projects, ideally before and after', 'Company details: name, address, phone, licence numbers', 'Your current website and Search Console access, if you have them', 'Three competitors in your area'],
  nota='Tu nicho m\u00e1s diferenciado: empresario del sector que adem\u00e1s programa. Im\u00e1genes: captura de remodelat.net, las puntuaciones Lighthouse de Houston y un esquema de la estructura "servicio por zona".'),

 dict(tag='G04', es='Base de datos Supabase con seguridad por filas, acceso y almacenamiento',
  en='I will design your Supabase database with RLS, auth and storage',
  cat='Programming & Tech > Software Development > Databases. Alternativa: APIs & Integrations',
  tags=['supabase', 'postgresql', 'database design', 'row level security', 'backend'],
  proof='P01 a P06',
  desc="""I design Supabase backends that are safe to put in front of real users.

I have built six production databases on Supabase and Postgres, from 15 to 61 tables, with hundreds of row level security policies, SQL functions and triggers.

What I can do for you:
- Database schema with relations, indexes and versioned migrations
- Row level security policies for every table, tested
- Auth: sign up, login, password reset and roles
- Storage: private buckets, signed URLs and upload rules
- SQL functions, triggers and RPC endpoints
- Full text search and JSONB filters
- Realtime subscriptions
- Rate limiting inside the database
- Review of an existing project: I find open tables, weak policies and exposed keys, and I fix them

You get SQL migration files you can run again, plus a short document explaining each table and policy.

Works with Next.js, React, Vue, Flutter or any other client. Message me with a short description of your app and I will tell you what you need.""",
  packs=[('Schema', 'Up to 8 tables with relations, indexes and RLS policies. Migration files.', '3 d\u00edas', '2', '90', '150'),
         ('Backend', 'Up to 20 tables, RLS, auth with roles, storage rules, 5 SQL functions.', '6 d\u00edas', '3', '250', '450'),
         ('Production', 'Up to 40 tables, full security review, triggers, search, tests and documentation.', '10 d\u00edas', '4', '600', '1.100')],
  extras=['Auditor\u00eda de seguridad de un proyecto existente: 150 $', 'Datos de ejemplo para desarrollo: 40 $', 'Videollamada de traspaso de 45 minutos: 50 $'],
  faq=[('Can you review a project that is already live?', 'Yes. I check every table, policy, bucket and key, and I send a list of findings with the fix for each one.'),
       ('Do you need my service role key?', 'For a review, read access to the SQL editor is enough. I never store your keys and I ask you to rotate them when the job ends.'),
       ('Do you also build the frontend?', 'Yes, with Next.js or React. That is a separate gig or a custom offer.')],
  reqs=['What your app does and who uses it', 'The main things you store and who can see or edit each one', 'Your current schema, if the project exists', 'The frontend framework you use'],
  nota='Poca competencia especializada y pedidos de tama\u00f1o medio. Im\u00e1genes: un diagrama de tablas y un ejemplo de pol\u00edtica RLS comentada. No pegues SQL real de tus productos.'),

 dict(tag='G05', es='Suscripciones y pagos con Stripe en tu app Next.js',
  en='I will integrate Stripe subscriptions and payments in your Next.js app',
  cat='Programming & Tech > Software Development > APIs & Integrations',
  tags=['stripe', 'payment integration', 'subscriptions', 'nextjs', 'saas'],
  proof='P03, P04',
  desc="""I connect Stripe to your Next.js or React app so you can charge customers without surprises.

In my own marketplace I built the full billing system: monthly and yearly plans, customer portal, webhooks, failed payment handling, coupons, free trials and tax IDs.

What I can set up:
- Stripe Checkout for one time payments
- Subscriptions with monthly and yearly prices
- Customer portal to change plan, update the card or cancel
- Webhooks that keep your database in sync, safe against retries
- Failed payments: grace period, reminders and downgrade
- Coupons, gift plans and free trials
- Plan limits: what each plan can and cannot do
- Test mode first, then live keys
- A document describing each payment flow

I work with Supabase or Postgres on the backend. If you use another database, ask me first.

I never ask for your Stripe password. You add me as a developer or share restricted keys.""",
  packs=[('Checkout', 'One time payment with Stripe Checkout, webhook and order record.', '3 d\u00edas', '2', '120', '200'),
         ('Subscriptions', 'Monthly and yearly plans, customer portal, webhooks, plan stored in your database.', '5 d\u00edas', '3', '300', '500'),
         ('Billing system', 'Subscriptions plus failed payments, coupons, trials, plan limits and documentation.', '9 d\u00edas', '4', '650', '1.200')],
  extras=['Facturas con datos fiscales del cliente: 100 $', 'Correos de aviso de cobro y de impago: 80 $', 'P\u00e1gina de precios dise\u00f1ada: 90 $'],
  faq=[('Is my app safe if a webhook arrives twice?', 'Yes. Each event is recorded and processed once, so retries from Stripe do not duplicate charges or plan changes.'),
       ('Can you add Stripe to an app that already has users?', 'Yes. I map existing users to Stripe customers and keep free users as they are.'),
       ('Do you handle taxes?', 'I configure Stripe Tax or tax inclusive prices and collect tax IDs. I am not a tax adviser, so your accountant decides the rates.')],
  reqs=['Your plans, prices and currency', 'Access to the repository and a Stripe account in test mode', 'How you store users today', 'What should happen when a payment fails or a plan is cancelled'],
  nota='Demanda constante y ticket medio alto. Imagen: un diagrama del ciclo de vida de una suscripci\u00f3n y una captura de la p\u00e1gina de planes de CamperOcasi\u00f3n.'),

 dict(tag='G06', es='Auditor\u00eda SEO t\u00e9cnica de webs Next.js o Astro, con correcci\u00f3n',
  en='I will audit the technical SEO of your Next.js or Astro site and fix it',
  cat='Digital Marketing > Search Engine Optimization (SEO) > Technical SEO',
  tags=['technical seo', 'seo audit', 'nextjs', 'core web vitals', 'schema markup'],
  proof='P01, P07, P08',
  desc="""I audit the technical SEO of your Next.js, Astro or static website and tell you exactly what is wrong, why it matters and how to fix it. Then I can fix it for you.

This is what I do on my own sites. One of my audits found more than 10,000 internal links pointing to redirects and three broken hreflang tags on a 273 page site.

What I check:
- Indexing: robots, sitemap, canonical, noindex and redirect chains
- Titles, descriptions and headings: missing, duplicated or too long
- Structured data: valid and useful
- International: hreflang and language versions
- Internal links and broken links
- Images: size, format, alt text and layout shift
- Speed: Core Web Vitals and Lighthouse
- Mobile and PWA basics

You receive a report ordered by impact, with the file or URL, the evidence and the fix for each issue. Not a generic tool export.

With the Standard and Premium packages I apply the fixes in your code and show before and after results.

I do not promise positions. I remove what is holding your site back.""",
  packs=[('Audit', 'Report for up to 50 pages, ordered by impact, with the fix for each issue.', '2 d\u00edas', '1', '60', '120'),
         ('Audit and fix', 'Report for up to 300 pages plus fixes for critical and high issues in your code.', '5 d\u00edas', '2', '180', '350'),
         ('Full technical SEO', 'Unlimited pages, all fixes, structured data, speed work and automatic build checks.', '8 d\u00edas', '3', '400', '800')],
  extras=['Datos estructurados para un tipo de p\u00e1gina: 50 $', 'Informe de velocidad antes y despu\u00e9s: 40 $', 'Alta en Search Console y env\u00edo de sitemaps: 40 $'],
  faq=[('Do you work with WordPress or Shopify?', 'My experience is with coded sites: Next.js, Astro and static HTML. For WordPress I can deliver the audit, but not the fixes.'),
       ('Do I need to give you access to the code?', 'For the audit only, no. For the fixes I need access to the repository and I work on a separate branch.'),
       ('How is this different from an automatic SEO tool?', 'A tool lists symptoms. I find the cause in the code, for example one wrong setting that creates thousands of redirects, and I fix it once.')],
  reqs=['Your website URL', 'The framework it is built with', 'Search Console access, if available', 'Repository access for packages that include fixes'],
  nota='Gig de entrada con alto valor percibido. Imagen: una p\u00e1gina real de tu informe de remodelat.net con los hallazgos numerados, y la tabla de puntuaciones Lighthouse.'),

 dict(tag='G07', es='Panel de administraci\u00f3n, CRM o ERP a medida',
  en='I will build a custom admin dashboard, CRM or ERP with React and Supabase',
  cat='Programming & Tech > Software Development > Web Applications',
  tags=['admin dashboard', 'crm', 'erp', 'react', 'internal tool'],
  proof='P05, P01, P06',
  desc="""I build internal tools that replace your spreadsheets: admin panels, CRMs and small ERPs made for the way your business works.

I built a complete ERP for a car import business: 16 modules covering stock, a ten step pipeline, CRM, accounting, invoicing, tax calculations, documents and reports, with four user roles. I also built an eleven section admin panel for a marketplace.

What I can build:
- Dashboard with your key numbers
- Tables with search, filters and export to CSV
- Customers, deals and follow ups
- Invoices, expenses and simple accounting
- Documents and photos attached to each record
- Roles and permissions
- Calculators and simulators for your prices or taxes
- PDF generation
- Works on mobile and can be installed as an app

Stack: React with Vite or Next.js, Tailwind and Supabase. Your data is protected with row level security and lives in your own account.

Tell me what you track today and where it hurts. I will propose the smallest tool that solves it.""",
  packs=[('Dashboard', 'Login, 1 dashboard, 3 data sections with search, filters and CSV export.', '8 d\u00edas', '2', '300', '500'),
         ('Business tool', 'Up to 7 modules, roles, PDF documents, charts and mobile layout.', '16 d\u00edas', '3', '800', '1.500'),
         ('Custom ERP', 'Up to 14 modules, accounting or invoicing, calculators, offline mode, user manual.', '30 d\u00edas', '4', '2.000', '4.000')],
  extras=['Importaci\u00f3n de tus datos desde Excel: 100 $', 'M\u00f3dulo adicional: 200 $', 'Manual de uso en PDF: 80 $', 'Un mes de soporte: 200 $'],
  faq=[('Can you import my current spreadsheets?', 'Yes. I map your columns to the new tables and load the data. Send me a sample file first.'),
       ('Where is my data stored?', 'In a Supabase project in your own account, in the region you choose. You can export everything at any time.'),
       ('Can several people use it with different permissions?', 'Yes. Roles such as owner, manager, sales and accountant are enforced in the database, not only in the screen.')],
  reqs=['A description of your business process, step by step', 'The spreadsheets or tools you use today', 'Who will use it and what each person may see or change', 'Reports or documents you need to produce'],
  nota='Ticket alto. Im\u00e1genes: capturas del ERP de KHC con datos de ejemplo. Graba un v\u00eddeo corto pasando por tres m\u00f3dulos.'),

 dict(tag='G08', es='Scraper en Python y seguimiento de precios',
  en='I will build a Python web scraper and price tracker for your market',
  cat='Data > Data Scraping. Alternativa: Programming & Tech > Software Development > Scripting',
  tags=['web scraping', 'python', 'data extraction', 'price tracking', 'data mining'],
  proof='P05',
  desc="""I write Python scrapers that collect the data you need and deliver it clean, in CSV, Excel, JSON or a database.

For my own car import business I built scrapers for three vehicle portals in Germany and Spain, collected market prices and fitted a pricing model on top (R squared 0.89).

What I can do:
- Extract listings, prices, product data or public directories
- Handle pagination, filters and detail pages
- Clean and normalize the data
- Remove duplicates
- Schedule it to run every day or every week
- Track price changes over time
- Simple analysis: averages, ranges and a price model

You get the script, instructions to run it and the data.

I only collect publicly available data and I respect each site's terms and robots rules. I do not bypass logins, paywalls or captchas, and I do not collect personal data.

Send me the website and the fields you need, and I will confirm if it is possible before you order.""",
  packs=[('One site', 'Scraper for 1 website, up to 8 fields, delivered as CSV with the script.', '2 d\u00edas', '1', '70', '120'),
         ('Multi site', 'Up to 3 websites, cleaning, duplicates removed, scheduled runs.', '5 d\u00edas', '2', '200', '350'),
         ('Price intelligence', 'Up to 5 sites, price history, comparison report and a simple price model.', '9 d\u00edas', '3', '500', '900')],
  extras=['Sitio adicional: 60 $', 'Carga en base de datos o Google Sheets: 50 $', 'Informe en PDF con gr\u00e1ficos: 80 $'],
  faq=[('Is web scraping legal?', 'It depends on the site, the data and your country. I work only with public, non personal data and within each site\u2019s terms. You are responsible for how you use the data.'),
       ('What if the website changes?', 'Scrapers can break when a site changes its layout. Fixes are free for 15 days after delivery; after that, a small update order.'),
       ('Can it run automatically?', 'Yes. I can schedule it on your computer, on a server or as a cloud job.')],
  reqs=['The website or websites', 'The exact fields you need, with an example', 'How many records you expect and how often', 'The output format you prefer'],
  nota='Categor\u00eda con mucha demanda y mucha competencia barata. Difer\u00e9nciate con el an\u00e1lisis: no solo los datos, tambi\u00e9n el modelo de precios. Mant\u00e9n siempre la frase sobre datos p\u00fablicos.'),

 dict(tag='G09', es='Plan de negocio con modelo financiero y PDF profesional',
  en='I will write your business plan with financial model and investor PDF',
  cat='Business > Business Plans',
  tags=['business plan', 'financial model', 'startup', 'investor', 'financial plan'],
  proof='P13, P05',
  desc="""I write business plans with numbers you can defend in front of a bank, an investor or a partner.

I have run my own companies and I build my plans the way I build software: every figure comes from a model, so when an assumption changes, the whole plan updates.

What you get:
- Executive summary
- Business model and services
- Market and competitors
- Operations and team
- Start up budget
- Five year profit and loss
- Cash flow and break even
- NPV, IRR and sensitivity analysis
- Risks and how to reduce them
- A designed PDF with charts, ready to present

My examples include a 49 page plan for a retail shop, a ten chapter plan for a renovation company and a plan for a car import business.

Strongest in: construction and renovation, local services, retail, vehicle trading and online marketplaces, in Spain and Latin America.

I need your idea, your location and the numbers you already know. Where data is missing, I research it and tell you the source.""",
  packs=[('Lean plan', '10 to 12 pages: model, market, start up budget and 3 year forecast. PDF.', '5 d\u00edas', '2', '150', '250'),
         ('Full plan', '25 to 30 pages: full plan, 5 year forecast, cash flow, break even. PDF and spreadsheet.', '9 d\u00edas', '3', '400', '700'),
         ('Investor plan', '40+ pages: full plan, NPV, IRR, sensitivity, scenarios and a summary deck.', '14 d\u00edas', '4', '900', '1.600')],
  extras=['Versi\u00f3n en segundo idioma: 120 $', 'Presentaci\u00f3n resumen de 10 diapositivas: 100 $', 'Estudio de locales o ubicaci\u00f3n: 100 $'],
  faq=[('Do you guarantee funding?', 'No. I deliver a solid, honest plan. The decision belongs to the bank or the investor.'),
       ('Where do the numbers come from?', 'From you, from public sources and from market research. Every assumption is listed with its source, so you can defend it.'),
       ('Can I change the numbers later?', 'Yes. You receive the spreadsheet or the model, and the results update when you change an assumption.'),
       ('In which languages do you write?', 'Spanish and English.')],
  reqs=['Your business idea and where it will operate', 'Investment available and financing you need', 'Prices, costs and sales you already know or expect', 'Who will read the plan: bank, investor, partner or grant'],
  nota='Fuera de programaci\u00f3n: te da una segunda v\u00eda de ingresos. Im\u00e1genes: tres p\u00e1ginas del PDF de 49 p\u00e1ginas con los datos anonimizados. Si tu ingl\u00e9s escrito no es fluido, ofrece este gig solo en espa\u00f1ol.'),

 dict(tag='G10', es='Funciones de inteligencia artificial para tu aplicaci\u00f3n',
  en='I will add AI features to your app with Gemini, Groq, OpenAI or Ollama',
  cat='Programming & Tech > AI Development > AI Integrations. Alternativa: AI Chatbots',
  tags=['ai integration', 'chatbot', 'llm', 'rag', 'ai agent'],
  proof='P12, P02, P06',
  desc="""I add AI features to your web app that are useful, controlled and not tied to one provider.

I built a local AI assistant that works with 11 model providers, runs tools with human approval and answers questions about your own code. I also added AI text improvement and receipt reading to my marketplaces.

What I can build:
- Chat assistant inside your app, with streaming answers
- Answers based on your documents or data (RAG)
- Buttons that write or improve text: product descriptions, listings, emails
- Agents that call your functions, with approval for sensitive actions
- Image and screenshot analysis
- OCR to read receipts or documents
- Fallback between models when one fails
- Private setup with local models through Ollama

Providers: Gemini, Groq, OpenAI compatible APIs, OpenRouter, Mistral and Ollama.
Backend: Next.js API routes or Python FastAPI.

You keep your own API keys. I show you the cost per request before going live.

Tell me what task you want the AI to do and I will suggest the simplest way.""",
  packs=[('AI button', 'One AI feature: generate or improve text from your data, with one provider.', '3 d\u00edas', '2', '120', '200'),
         ('AI assistant', 'Chat with streaming, your documents as knowledge, model fallback.', '7 d\u00edas', '3', '350', '600'),
         ('AI agent', 'Assistant that calls your functions with approval, memory and usage log.', '12 d\u00edas', '4', '800', '1.500')],
  extras=['Proveedor de modelos adicional: 50 $', 'Lectura de documentos con OCR: 120 $', 'Panel de consumo y costes: 100 $'],
  faq=[('Which model should I use?', 'It depends on the task, the language and the budget. I test two or three with your real examples and show you quality and cost.'),
       ('Can my data stay private?', 'Yes. With Ollama the model runs on your own machine or server and nothing is sent to third parties.'),
       ('Will the AI make mistakes?', 'Yes, all models do. I add limits, validation and human approval where a mistake would be costly.')],
  reqs=['The task you want to automate, with 3 real examples', 'Your app stack and repository access', 'An API key from the provider you prefer, or I recommend one', 'Any data that must not leave your systems'],
  nota='Categor\u00eda en crecimiento. Imagen: una captura de MiClaw con la tarjeta de aprobaci\u00f3n de una herramienta, y la lista de proveedores.'),

 dict(tag='G11', es='Correcci\u00f3n de errores y despliegue de apps Next.js en Vercel',
  en='I will fix bugs and deploy your Next.js app on Vercel',
  cat='Programming & Tech > Website Maintenance > Bug Fixes',
  tags=['nextjs', 'bug fix', 'vercel', 'react', 'deployment'],
  proof='P01 a P05',
  desc="""Your Next.js app has a bug, the build fails or the deployment does not work. I find the cause, fix it and explain what happened.

I maintain several Next.js applications in production, from version 14 to 16, with Supabase, Stripe and Vercel.

What I fix:
- Build and TypeScript errors
- Hydration and rendering errors
- API routes and server side code
- Supabase auth, queries and security policies
- Stripe webhooks
- Environment variables and Vercel configuration
- Domains, redirects and scheduled jobs
- Slow pages and heavy images
- Dependency upgrades

How it works: you give me access to the repository, I reproduce the problem, fix it on a branch and send you a pull request with a clear explanation.

If I cannot reproduce or fix the issue, I tell you quickly and we cancel the order.

Please message me first with the error message and a link to the site.""",
  packs=[('Quick fix', '1 bug or build error, fixed and explained.', '1 d\u00eda', '1', '30', '50'),
         ('Fix pack', 'Up to 4 issues or a full deployment with domain and environment variables.', '2 d\u00edas', '2', '80', '120'),
         ('Rescue', 'Up to 10 issues, version upgrade, speed review and a written report.', '4 d\u00edas', '2', '180', '300')],
  extras=['Entrega en 12 horas: 30 $', 'Error adicional: 25 $', 'Informe por escrito de causas y prevenci\u00f3n: 30 $'],
  faq=[('Do you need access to my production data?', 'Usually not. Repository access and a preview deployment are enough.'),
       ('What if the bug is bigger than expected?', 'I tell you before continuing and send a custom offer. No surprise charges.'),
       ('Do you fix other frameworks?', 'React with Vite and Astro, yes. For other frameworks, ask me first.')],
  reqs=['The error message or a description of what fails', 'Repository access (GitHub invitation)', 'A link to the site or the failing deployment', 'What changed just before it broke, if you know'],
  nota='Gig de volumen para conseguir rese\u00f1as r\u00e1pido. Responde en minutos: en esta subcategor\u00eda gana el primero que contesta con un diagn\u00f3stico.'),

 dict(tag='G12', es='Aplicaci\u00f3n de videovigilancia autoalojada para c\u00e1maras IP',
  en='I will build a self hosted IP camera surveillance app with Python',
  cat='Programming & Tech > Software Development > Desktop Applications',
  tags=['ip camera', 'opencv', 'python', 'rtsp', 'cctv'],
  proof='P11',
  desc="""I build self hosted video surveillance software for IP cameras: your video stays on your computer, with no cloud subscription.

I developed a complete surveillance app for Windows in Python: camera discovery, live view, recording, motion detection and alerts.

What I can build or adapt:
- Connection to RTSP and ONVIF cameras, including discovery on your network
- Live view in the browser
- Continuous or motion based recording
- Detection zones and privacy masks
- Optional object detection with YOLO
- Alerts by Telegram, email, Discord, ntfy, Pushover or webhook
- Web interface that works on mobile
- Windows installer

Stack: Python, FastAPI, OpenCV and ffmpeg.

Tell me your camera brand and model, how many cameras you have and what you want to be alerted about. Some cameras use closed protocols, so I confirm compatibility before you order.

This is for monitoring your own property. I do not build tools to access cameras you do not own.""",
  packs=[('Viewer', 'Live view for up to 4 RTSP cameras in a web page.', '4 d\u00edas', '2', '150', '250'),
         ('Recorder', 'Live view, recording, motion detection with zones and Telegram alerts.', '8 d\u00edas', '3', '400', '700'),
         ('Full system', 'Recorder plus object detection, several alert channels and Windows installer.', '14 d\u00edas', '4', '900', '1.500')],
  extras=['Canal de aviso adicional: 40 $', 'C\u00e1mara con control de movimiento: 80 $', 'Instalaci\u00f3n guiada por videollamada: 60 $'],
  faq=[('Which cameras are supported?', 'Any camera with an RTSP stream or ONVIF. Send me the model and I check before you order.'),
       ('Does it need the internet?', 'No. It runs on your local network. Internet is only needed for alerts.'),
       ('Can it detect people instead of any movement?', 'Yes, with the object detection option. It needs a reasonably modern computer.')],
  reqs=['Camera brands and models', 'Number of cameras and the computer that will run the software', 'What you want to record and when', 'How you want to receive alerts'],
  nota='Nicho con poca oferta. Publ\u00edcalo cuando ya tengas rese\u00f1as en otros gigs: los pedidos dependen del equipo del cliente y son menos previsibles.'),

 dict(tag='G13', es='Presupuesto de obra o reforma por partidas',
  en='I will prepare an itemized cost estimate for your renovation project',
  cat='Busca "construction cost estimate" en Fiverr y usa la subcategor\u00eda donde aparezcan esos gigs (Architecture & Building Design o Business > Consulting)',
  tags=['cost estimate', 'construction', 'quantity takeoff', 'renovation', 'bill of quantities'],
  proof='P06, P13',
  desc="""I prepare clear, itemized estimates for renovation and construction work, so you can send a professional quote or check one you received.

I have managed renovation companies in Spain and I built estimating software with a catalogue of more than 170,000 work items and price data for 18 countries.

What you get:
- Work items grouped by chapter: demolition, plumbing, electrical, tiling, carpentry and painting
- Quantities taken from your plans, measurements or photos
- Unit prices for labour and materials, with ranges
- Totals with tax and contingency
- An editable spreadsheet and a clean PDF

Typical jobs: bathroom, kitchen, full apartment renovation and small extensions.

Best coverage: Spain and Latin America. For other countries I use your local rates.

This is a budget estimate for planning and quoting. It is not a structural calculation or a legally certified document.

Send me plans or measurements, the location and the level of finish you want.""",
  packs=[('One room', 'Bathroom or kitchen: itemized estimate with quantities and unit prices. PDF.', '2 d\u00edas', '1', '60', '100'),
         ('Apartment', 'Full renovation up to 120 m2: chapters, quantities, prices, spreadsheet and PDF.', '4 d\u00edas', '2', '150', '280'),
         ('Project', 'Larger project or 3 finish levels compared, with schedule and payment plan.', '7 d\u00edas', '3', '350', '650')],
  extras=['Comparaci\u00f3n con un presupuesto recibido: 50 $', 'Cronograma de obra: 50 $', 'Plantilla con tu logotipo para reutilizar: 60 $'],
  faq=[('Are the prices valid for my city?', 'I use reference prices by country and adjust them with the local rates you give me. I show the source and the range of each price.'),
       ('Can contractors use this to quote their clients?', 'Yes. You receive an editable file with your logo, ready to send.'),
       ('Do you visit the site?', 'No. I work from plans, measurements, photos and video.')],
  reqs=['Plans or a sketch with measurements', 'Photos or video of the current state', 'City and country', 'Level of finish: basic, medium or high', 'What you want to keep and what you want to replace'],
  nota='Tu experiencia de a\u00f1os est\u00e1 aqu\u00ed, no en el c\u00f3digo. Imagen: un presupuesto de muestra de CotizaT con datos ficticios. Comprueba la categor\u00eda antes de publicar.'),
 dict(tag='G14', es='Producto SaaS mínimo viable con cuentas, cobro y panel',
  en='I will build your SaaS MVP with FastAPI or Next.js, Supabase and Stripe',
  cat='Programming & Tech > Software Development > Web Applications. Alternativa: Website Development > Custom Websites',
  tags=['saas', 'mvp', 'fastapi', 'web application', 'stripe'],
  proof='P06, P03',
  desc="""I build SaaS products that are ready to charge customers: accounts, teams, billing, admin panel and your core feature.

I designed, built and run my own SaaS for construction estimating. It has almost 100,000 lines of Python, more than 2,600 automated tests, Stripe billing, two languages, support for 23 countries and paying companies.

What I can build for you:
- Sign up, login and password reset
- Organizations with members and invitations, each one isolated in the database
- Your core feature: the screens and logic that make your product useful
- Plans, free trial and Stripe subscriptions
- Admin panel: users, payments, renewals and activity
- Transactional emails
- PDF or Excel export
- Public landing page with basic SEO
- Automated tests and a deployment pipeline

Stack: Python with FastAPI, or Next.js with TypeScript. Postgres on Supabase with row level security. Stripe. Deployed on Vercel in your own accounts.

You receive the source code, the database migrations and a short operations guide.

An MVP needs a clear scope. Message me first and we will define the one thing your product must do well.""",
  packs=[('Core', 'Login, one core feature with up to 5 screens, database with security rules, deployed.', '15 d\u00edas', '2', '600', '1.200'),
         ('SaaS', 'Core plus organizations, Stripe subscriptions, admin panel, emails and landing page.', '28 d\u00edas', '3', '1.400', '2.600'),
         ('Complete', 'SaaS plus free trial, PDF export, two languages, automated tests and operations guide.', '45 d\u00edas', '4', '2.800', '5.000')],
  extras=['Segundo idioma: 200 $', 'Asistente con IA dentro del producto: 350 $', 'Exportación a PDF con tu marca: 200 $', 'Un mes de soporte tras el lanzamiento: 250 $'],
  faq=[('Python or Next.js?', 'Both work. I recommend Python with FastAPI when the product has heavy calculations, documents or data, and Next.js when the interface is the product.'),
       ('Can you start from my existing code?', 'Yes, if it is FastAPI, Next.js or React. I review it first and tell you what I would keep and what I would rewrite.'),
       ('Who owns the product?', 'You do. Code, database, Stripe account and hosting are in your name from the first day.'),
       ('How do we avoid the scope growing?', 'We agree a written list of screens and features before the order. Anything new goes into a separate extra or a second phase.')],
  reqs=['The problem your product solves and who pays for it', 'The main workflow, step by step', 'Your plans and prices, or the ones you are considering', 'Two or three products you like', 'Your deadline and budget range'],
  nota='CotizaT es la prueba. La frase sobre empresas de pago sale de tu documento del 2 de noviembre: mantenla solo si sigue siendo cierta. Imágenes: el editor de presupuestos, la página de pago y el panel de operador, con datos de ejemplo. Publícalo en la tercera ola, con oferta personalizada por hitos.')
]


def gig(g):
    assert len(g['en']) <= 80, (g['tag'], len(g['en']))
    assert g['en'].startswith('I will ')
    assert len(g['tags']) == 5 and all(len(t) <= 20 for t in g['tags']), g['tag']
    for p in g['packs']:
        assert len(p[1]) <= 100, (g['tag'], p[0], len(p[1]))
    s = [PageBreak(), H2(g['es'], tag=g['tag'])]
    s.append(kv([
        ('Categor\u00eda', g['cat']),
        ('Etiquetas', '<font name="Mono">%s</font>' % '  \u00b7  '.join(x.replace(' ', '\u00a0') for x in g['tags'])),
        ('Prueba', 'Fichas %s de la secci\u00f3n 04' % g['proof']),
    ]))
    s += paste('T\u00edtulo del gig (EN)', g['en'], 80, title=True)
    s += paste('Descripci\u00f3n (EN)', g['desc'], 1200)
    s.append(h3('Paquetes'))
    pk = g['packs']
    s.append(table([
        ['', 'Basic', 'Standard', 'Premium'],
        ['Nombre', pk[0][0], pk[1][0], pk[2][0]],
        ['Descripci\u00f3n (EN)', pk[0][1], pk[1][1], pk[2][1]],
        ['Entrega', pk[0][2], pk[1][2], pk[2][2]],
        ['Revisiones', pk[0][3], pk[1][3], pk[2][3]],
        ['Precio de lanzamiento', pk[0][4] + ' $', pk[1][4] + ' $', pk[2][4] + ' $'],
        ['Precio objetivo', pk[0][5] + ' $', pk[1][5] + ' $', pk[2][5] + ' $'],
    ], [19, 27, 27, 27], first_bold=True, zebra=False))
    s.append(h3('Extras del gig'))
    s.append(P('  \u00b7  '.join(g['extras'])))
    s.append(h3('Preguntas frecuentes (EN)'))
    s.append(Paragraph('<br/><br/>'.join('<b>%s</b><br/>%s' % (esc(q), esc(a)) for q, a in g['faq']), ST['paste']))
    s.append(h3('Requisitos para el comprador (EN)'))
    s += bullets(g['reqs'])
    s.append(note(g['nota'], title='Nota'))
    return s


def build():
    s = section('06', 'Catorce gigs listos para publicar',
                'Cada ficha trae lo que pide el formulario de Fiverr: t\u00edtulo, categor\u00eda, etiquetas, descripci\u00f3n, tres paquetes, extras, preguntas frecuentes y requisitos.')
    s.append(P('Los textos que ve el comprador est\u00e1n en ingl\u00e9s. Los l\u00edmites que he aplicado son los habituales de Fiverr: 80 caracteres en el t\u00edtulo, 1.200 en la descripci\u00f3n, cinco etiquetas de hasta 20 caracteres y 100 caracteres en la descripci\u00f3n de cada paquete.'))
    s.append(P('Cada paquete tiene dos precios. El <b>de lanzamiento</b> es para conseguir las primeras rese\u00f1as; el <b>objetivo</b> es al que conviene llegar cuando el gig tenga unas 15. La l\u00f3gica est\u00e1 en la secci\u00f3n 07.'))
    s.append(table(
        [['Gig', 'Servicio', 'Tipo', 'Lanzamiento (USD)', 'Objetivo (USD)']] +
        [[g['tag'], g['es'],
          {'G01': 'Ticket alto', 'G07': 'Ticket alto', 'G14': 'Ticket alto', 'G09': 'Ticket medio', 'G03': 'Ticket medio', 'G05': 'Ticket medio',
           'G10': 'Ticket medio', 'G04': 'Ticket medio', 'G12': 'Nicho', 'G13': 'Nicho', 'G02': 'Entrada', 'G06': 'Entrada',
           'G11': 'Entrada', 'G08': 'Entrada'}[g['tag']],
          '%s a %s' % (g['packs'][0][4], g['packs'][2][4]), '%s a %s' % (g['packs'][0][5], g['packs'][2][5])] for g in GIGS],
        [7, 45, 14, 18, 16], mono_cols=(0,)))
    for g in GIGS:
        s += gig(g)
    return s
