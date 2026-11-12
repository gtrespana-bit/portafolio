// Contenido EXACTO del CV original (junio de 2026), en el formato del generador.
// No es el CV actual: sirve para comprobar que el generador reproduce el diseño original.
//   node build.mjs --content reference/content.original.mjs --pdf /tmp/replica.pdf --html /tmp/replica.html
//   python tools/compare.py "../original/CV - Ruben Romero- Hyb (original, jun 2026).pdf" /tmp/replica.pdf

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
    { label: 'Backend & BaaS', tags: ['Supabase', 'PostgreSQL', 'Node.js', 'REST APIs', 'Edge Functions'] },
    { label: 'SEO & Content', tags: ['Technical SEO', 'Local SEO', 'On-Page SEO', 'Content Writing', 'Keyword Research', 'Schema.org', 'Ahrefs', 'SEMrush', 'GA4', 'Search Console'] },
    { label: 'Performance', tags: ['Core Web Vitals', 'Lighthouse', 'PageSpeed', 'Screaming Frog'] },
    { label: '3D & Animations', tags: ['Three.js', 'Spline', 'GSAP', 'WebGL', 'Canvas API'] },
    { label: 'DevOps & Tools', tags: ['Git', 'Vercel', 'Sentry', 'Docker', 'CI/CD'] },
    { label: 'AI & Automation', tags: ['OpenAI API', 'Claude API', 'Content Automation'] },
  ],
  languages: [['Spanish', 5], ['English', 4], ['German', 2]],
};

export default {
  meta: { lang: 'en', title: 'CV - Rubén Romero - Full-Stack & SEO Specialist' },
  sidebar,
  pages: [
    [
      {
        type: 'profile',
        title: 'Professional Profile',
        text: "Full-Stack Web Developer with a Doctorate in Engineering (UPM) and deep expertise in Technical SEO, Performance Optimization, and Content Strategy. I combine solid engineering skills (Supabase, React, Next.js, Astro) with proven SEO execution—achieving first-page rankings, 99/100 PageSpeed scores, and 40%+ organic traffic growth. Experienced in writing SEO-optimized long-form content, implementing Schema.org markup, and building multilingual platforms (ES/EN/DE). I've also worked with Three.js, GSAP, and Canvas API for immersive experiences. Dual residency in Caracas and Madrid, available for remote work.",
      },
      {
        type: 'experience',
        title: 'Professional Experience',
        items: [
          {
            role: 'Full-Stack Developer & Product Architect',
            company: 'vendet.online - AI-Powered Marketplace',
            date: '2024 - Present',
            bullets: [
              'Complete architecture with Supabase (PostgreSQL), Row Level Security (RLS), and Edge Functions for serverless logic.',
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
              'Complete local SEO strategy achieving first-page rankings for 20+ high-intent keywords across Caracas, Valencia, and other major cities.',
              'Authored 15+ long-form SEO blog articles (2,500+ words each) targeting transactional keywords, driving 40%+ organic traffic growth.',
              'Implemented LocalBusiness and Service schema markup, earning rich snippets and improving CTR from search results.',
              'Site built with Astro (SSG): 99/100 Desktop, 94+/100 Mobile PageSpeed. LCP reduced from 4.1s to 1.8s (56% improvement).',
              'Location-specific landing pages with city-targeted content and optimized meta tags for local search dominance.',
            ],
            tags: ['Technical SEO', 'Local SEO', 'Astro', 'Schema.org', 'Content Strategy'],
          },
          {
            role: 'Creative Web Developer & Multilingual Specialist',
            company: 'Immersive Projects & Healthcare/Beauty Sector',
            date: '2023 - Present',
            bullets: [
              'Web experiences with Three.js, Spline, GSAP, and Canvas API, including interactive 3D globe with GLSL shaders and animated data flows.',
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
    [
      {
        type: 'projects',
        title: 'Featured Projects',
        items: [
          {
            icon: 'chart_increasing',
            title: 'ReformaT - Local SEO Dominance',
            text: 'Complete local SEO strategy for multi-city remodeling company. First-page rankings for "remodelación Caracas", "reformas Valencia" and 20+ high-intent keywords. Built location-specific landing pages, implemented LocalBusiness schema, and authored 15+ long-form articles. Results: 99/100 PageSpeed, 56% LCP reduction, 40%+ organic traffic growth.',
            tags: ['Local SEO', 'Content Strategy', 'Astro', 'Schema.org'],
          },
          {
            icon: 'money_bag',
            title: 'vendet.online - AI Marketplace',
            text: 'Classifieds platform with Supabase architecture (PostgreSQL + RLS), hybrid AI system for SEO content generation and moderation, virtual credit economy, and 5,000+ active listings optimized for search visibility.',
            tags: ['Supabase', 'OpenAI API', 'SEO at Scale', 'Sentry'],
          },
          {
            icon: 'globe_showing_europe-africa',
            title: 'MajesticWeb - Interactive 3D Globe',
            text: 'Platform with interactive 3D globe (Three.js + GLSL shaders), mouse rotation, animated data flows between cities, and scroll-driven synchronization with GSAP ScrollTrigger. Optimized for 60fps with devicePixelRatio management.',
            tags: ['Three.js', 'GLSL', 'GSAP', 'React'],
          },
          {
            icon: 'hospital',
            title: 'Multilingual SEO Platforms',
            text: 'Premium healthcare websites with i18n systems (ES/EN/DE), medical terminology, LocalBusiness schema, optimized Google Business Profiles, and FAQ sections targeting "People Also Ask" queries for featured snippets.',
            tags: ['i18n SEO', 'Medical Content', 'Local SEO'],
          },
        ],
      },
      {
        type: 'achievements',
        title: 'Quantifiable Achievements',
        items: [
          { icon: 'rocket', title: 'Performance', text: '99/100 Desktop, 94+/100 Mobile. LCP reduced from 4.1s to 1.8s (56% improvement).' },
          { icon: 'bar_chart', title: 'Organic Growth', text: '40%+ organic traffic increase through strategic content and technical SEO.' },
          { icon: 'bullseye', title: 'Local Rankings', text: 'First-page rankings for 20+ high-intent local keywords across multiple cities.' },
          { icon: 'writing_hand', title: 'Content Production', text: '15+ long-form SEO articles (2,500+ words) establishing topical authority.' },
          { icon: 'robot', title: 'AI Automation', text: '70% reduction in content moderation time through AI workflows.' },
          { icon: 'globe_showing_europe-africa', title: 'Multilingual SEO', text: 'ES/EN/DE content strategies for international healthcare clients.' },
        ],
      },
      {
        type: 'education',
        title: 'Education & Certifications',
        items: [
          { title: 'Doctorate in Electrical Engineering', text: 'Universidad Politécnica de Madrid (UPM) - Spain' },
          { title: 'SEO & Content Marketing Training', text: 'Self-directed learning through Ahrefs Academy, SEMrush Academy, Moz Learning, and hands-on implementation across 10+ client projects.' },
          { title: 'Technical Certifications', text: 'Google Analytics 4, Google Search Console, Schema.org, Core Web Vitals, Technical SEO Audits, Local SEO Strategy, Three.js Journey, GSAP Certified.' },
          { title: 'Live Projects', lines: ['• ReformaT Venezuela: First-page local rankings', '• vendet.online: AI-powered marketplace', '• MajesticWeb: Immersive 3D experience', '• Healthcare platforms: Multilingual SEO success'] },
        ],
      },
    ],
  ],
};
