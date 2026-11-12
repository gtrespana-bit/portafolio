// Contenido del CV de Rubén Romero (versión «Hyb»: Full-Stack + SEO). Actualizado en noviembre de 2026.
//
// Para cambiar el CV se edita solo este archivo y se ejecuta `node build.mjs`.
//   · [[dominio.com]] crea un enlace a https://dominio.com; [[texto|https://url]] enlaza otro destino.
//   · {{dos palabras}} impide que la línea se parta entre ellas (para que no quede una palabra suelta).
//   · Los iconos son los nombres de los archivos de assets/emoji-png (sin .png).
//   · build.mjs avisa si algo se sale de la página o si un título se parte en dos líneas.

const sidebar = {
  name: 'Rubén Romero',
  titles: ['Full-Stack Web Developer', 'SEO Specialist & Performance Expert'],
  labels: { contact: 'Contact', skills: 'Skills', languages: 'Languages' },
  contact: [
    { icon: 'e-mail', lines: ['[[lanzareformas@icloud.com]]'] },
    { icon: 'mobile_phone', lines: ['+58 422 799 7043 (VE)', '+34 651 658 995 (ES)'] },
    { icon: 'round_pushpin', lines: ['Caracas / Madrid'] },
    { icon: 'octopus', lines: ['[[github.com/gtrespana-bit]]'] },
  ],
  skills: [
    { label: 'Frontend', tags: ['HTML5', 'CSS3', 'JavaScript', 'TypeScript', 'Astro', 'React', 'Next.js', 'Tailwind'] },
    { label: 'Backend & BaaS', tags: ['Supabase', 'PostgreSQL', 'Node.js', 'Python', 'FastAPI', 'Stripe', 'REST APIs', 'Edge Functions'] },
    { label: 'SEO & Content', tags: ['Technical SEO', 'Local SEO', 'On-Page SEO', 'Programmatic SEO', 'Content Writing', 'Keyword Research', 'Schema.org', 'Ahrefs', 'SEMrush', 'GA4', 'Search Console'] },
    { label: 'Performance', tags: ['Core Web Vitals', 'Lighthouse', 'PageSpeed', 'Screaming Frog'] },
    { label: '3D & Animations', tags: ['Three.js', 'Spline', 'GSAP', 'WebGL', 'Canvas API'] },
    { label: 'DevOps & Tools', tags: ['Git', 'Vercel', 'Sentry', 'Docker', 'CI/CD', 'GitHub Actions', 'Automated Testing'] },
    { label: 'AI & Automation', tags: ['OpenAI API', 'Claude API', 'Gemini API', 'Content Automation', 'OCR'] },
  ],
  languages: [['Spanish', 5], ['English', 4], ['German', 2]],
};

export default {
  meta: { lang: 'en', title: 'CV - Rubén Romero - Full-Stack & SEO Specialist' },
  sidebar,
  pages: [
    // ------------------------------------------------------------------ página 1
    [
      {
        type: 'profile',
        title: 'Professional Profile',
        text: 'Full-Stack Web Developer with a Doctorate in Engineering (UPM) and deep expertise in Technical SEO, Performance Optimization, and Content Strategy. I design, build, and launch my own products end to end: CotizaT, a construction-estimating SaaS with its first paying companies; four live marketplaces on one reusable engine; and a custom ERP for a vehicle-import business. I combine solid engineering skills (Next.js, TypeScript, Python, Supabase, Stripe) with proven SEO execution—achieving first-page rankings, 99/100 PageSpeed scores, and 40%+ organic traffic growth. Dual residency in Caracas and Madrid, available for remote work.',
      },
      {
        type: 'experience',
        title: 'Professional Experience',
        items: [
          {
            role: 'Founder & Full-Stack Product Developer',
            company: 'Own Software Products - SaaS, Marketplaces & ERP',
            date: '2026 - Present',
            bullets: [
              'Designed, built, and launched a construction-estimating SaaS (CotizaT), three new marketplaces, and a custom ERP, covering product, database, payments, SEO, testing, and deployment end to end.',
              'CotizaT: multi-tenant Python/FastAPI application on PostgreSQL (Supabase) with Row Level Security, Stripe subscriptions, and 23 countries configured—98,000 lines of Python, 378 routes, and 2,600+ automated tests.',
              'Reusable marketplace engine in Next.js, TypeScript, and Supabase: CamperOcasión, with dealer storefronts and Stripe subscriptions, and MaquinariaOcasión, a new B2B vertical launched in four days.',
              'Payments adapted to each market: Stripe subscriptions end to end in Spain; Pago Móvil and Binance receipts read by OCR and validated in Venezuela Inmuebles.',
              'Programmatic SEO across products: landing pages by country, province, city, and category with structured data, hreflang, sitemaps, and IndexNow.',
            ],
            tags: ['Next.js', 'TypeScript', 'Python', 'FastAPI', 'Stripe', 'Programmatic SEO'],
          },
          {
            role: 'Full-Stack Developer & Product Architect',
            company: 'vendet.online - AI-Powered Marketplace',
            date: '2024 - Present',
            bullets: [
              'Complete architecture with Supabase (PostgreSQL), Row Level Security (RLS), and Edge Functions for {{serverless logic.}}',
              'Hybrid AI integration (OpenAI, Claude, OpenClaw) for SEO-optimized description generation and content moderation, reducing manual review time by 70%.',
              'Comprehensive on-page SEO across 5,000+ active listings with optimized meta tags, structured data, and internal linking.',
              'Virtual credit-based economy system with monetization (Boost, 24h/48h Featured listings).',
              'Sentry monitoring reducing MTTR by 60%. Response times <200ms.',
            ],
            tags: ['Supabase', 'PostgreSQL', 'Edge Functions', 'OpenAI API', 'SEO at Scale'],
          },
          {
            role: 'SEO Strategist & Performance Engineer',
            company: 'ReformaT Venezuela - Construction & Remodeling',
            date: '2024 - Present',
            bullets: [
              'Complete local SEO strategy with location-specific landing pages, achieving first-page rankings for "remodelación Caracas", "reformas Valencia", and 20+ high-intent keywords.',
              'Authored 15+ long-form SEO blog articles (2,500+ words each) targeting transactional keywords, driving 40%+ organic traffic growth.',
              'Implemented LocalBusiness and Service schema markup, earning rich snippets and improving CTR from search results.',
              'Site built with Astro (SSG): 99/100 Desktop, 94+/100 Mobile PageSpeed. LCP reduced from 4.1s to 1.8s (56% improvement).',
            ],
            tags: ['Technical SEO', 'Local SEO', 'Astro', 'Schema.org', 'Content Strategy'],
          },
          {
            role: 'Creative Web Developer & Multilingual Specialist',
            company: 'Immersive Projects & Healthcare/Beauty Sector',
            date: '2023 - Present',
            bullets: [
              "Web experiences with Three.js, Spline, GSAP, and Canvas API, including MajesticWeb's interactive 3D globe with GLSL shaders and animated data flows.",
              'Multilingual SEO content (ES/EN/DE) for healthcare clinics with proper medical terminology and cultural localization.',
              'Premium interfaces with glassmorphism, microinteractions, custom cursors, and scroll-driven animations.',
              'FAQ sections and "People Also Ask" content to capture featured snippets and voice search queries.',
              'Google Business Profile optimization and local citations for multi-location healthcare providers.',
            ],
            tags: ['Three.js', 'GSAP', 'i18n', 'Medical SEO', 'WebGL'],
          },
        ],
      },
    ],
    // ------------------------------------------------------------------ página 2
    [
      {
        type: 'projects',
        title: 'Featured Projects',
        items: [
          {
            icon: 'building_construction',
            title: 'CotizaT - Construction Estimating SaaS',
            text: 'Multi-tenant SaaS for builders and renovation companies, live at [[cotizat.online]] with its first paying companies. Estimate editor with branded PDF output, takeoff on drawings with DXF export, BC3 import/export, reference prices for 18 countries, Stripe subscriptions, and an assistant that reviews estimates and flags missing scope.',
            tags: ['Python', 'FastAPI', 'PostgreSQL', 'Stripe', 'SaaS'],
          },
          {
            icon: 'minibus',
            title: 'CamperOcasión - Campervan Marketplace (Spain)',
            text: 'Marketplace for used campervans and motorhomes, live at [[camperocasion.online]]. Dealer storefronts with CSV stock import, Stripe subscriptions end to end (customer portal, failed payments, coupons, 30-day trial), a valuation tool, and programmatic SEO by province. 112 API routes and 216 Row Level Security policies.',
            tags: ['Next.js', 'TypeScript', 'Supabase', 'Stripe'],
          },
          {
            icon: 'tractor',
            title: 'MaquinariaOcasión - B2B Marketplace Launched in 4 Days',
            text: 'Used-machinery marketplace live at [[maquinaria.click]], built on the CamperOcasión engine with my own tool that clones a complete vertical from a single brand file. 384 build-time pages with structured data and IndexNow.',
            tags: ['Next.js', 'Supabase', 'Reusable Engine', 'Technical SEO'],
          },
          {
            icon: 'house',
            title: 'Venezuela Inmuebles - Real Estate Portal with Map & AI',
            text: 'Sales and rentals portal live at [[venezuela-inmuebles.online]], with interactive map search and paid plans for agencies. Payments adapted to the country: Pago Móvil and Binance receipts are read by OCR, validated, and blocked from reuse. Listing descriptions improved with Gemini.',
            tags: ['Next.js', 'Supabase', 'Leaflet', 'OCR', 'Gemini API'],
          },
          {
            icon: 'automobile',
            title: 'KHC Auto Import - Custom ERP & Website',
            text: 'ERP with 16 modules for a business importing vehicles from Germany to Spain: fleet workflow, import simulator, Spanish tax engine, CRM, and invoicing, with the public website ([[khcimport.autos]]) fed from the ERP. Python scrapers collect market prices for a regression model (R² 0.89).',
            tags: ['React', 'Supabase', 'Python', 'ERP', 'Data Analysis'],
          },
        ],
      },
      {
        type: 'achievements',
        title: 'Quantifiable Achievements',
        items: [
          { icon: 'package', title: 'Products in Production', text: '7 products live on their own domains: a SaaS, four marketplaces, an ERP, and a local SEO site.' },
          { icon: 'rocket', title: 'Performance', text: '99/100 Desktop, 94+/100 Mobile. LCP reduced from 4.1s to 1.8s (56% improvement).' },
          { icon: 'bar_chart', title: 'Organic Growth', text: '40%+ organic traffic increase through strategic content and technical SEO.' },
          { icon: 'bullseye', title: 'Local Rankings', text: 'First-page rankings for 20+ high-intent local keywords across multiple cities.' },
          { icon: 'test_tube', title: 'Code Quality', text: '2,600+ automated tests in CotizaT and 600+ Row Level Security policies across four marketplaces.' },
          { icon: 'stopwatch', title: 'Time to Market', text: 'New marketplace vertical launched in four days on a reusable engine.' },
        ],
      },
      {
        type: 'education',
        title: 'Education & Certifications',
        items: [
          { title: 'Doctorate in Electrical Engineering', text: 'Universidad Politécnica de Madrid (UPM) - Spain' },
          { title: 'SEO & Content Marketing Training', text: 'Self-directed learning through Ahrefs Academy, SEMrush Academy, Moz Learning, and hands-on implementation across 10+ client projects.' },
          { title: 'Technical Certifications', text: 'Google Analytics 4, Google Search Console, Schema.org, Core Web Vitals, Technical SEO Audits, Local SEO Strategy, Three.js Journey, GSAP Certified.' },
          {
            title: 'Live Projects',
            lines: [
              '• [[cotizat.online]] · [[camperocasion.online]] · [[maquinaria.click]] · [[venezuela-inmuebles.online]]',
              '• [[vendet.online]] · [[khcimport.autos]] · [[remodelat.net]] (ReformaT Venezuela)',
            ],
          },
        ],
      },
    ],
  ],
};
