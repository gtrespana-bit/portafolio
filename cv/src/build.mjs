// Genera el CV en PDF (y un HTML autocontenido) a partir de content.mjs.
//
//   node build.mjs                      -> ../CV - Ruben Romero - Hyb.pdf  y  ../cv.html
//   node build.mjs --content otro.mjs --pdf salida.pdf --html salida.html --ls espaciado.json
//
// Al terminar imprime un informe en JSON: fuentes cargadas, espacio libre en cada página
// (mainFree y sidebarFree, en px; si alguno es negativo, el contenido no cabe), número de
// líneas de cada bloque y los textos de una sola línea que se han partido en dos (wraps).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { launch } from './browser.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const arg = (name, def) => {
  const i = process.argv.indexOf('--' + name);
  return i > -1 && process.argv[i + 1] ? path.resolve(process.argv[i + 1]) : def;
};
const contentPath = arg('content', path.join(HERE, 'content.mjs'));
const pdfPath = arg('pdf', path.join(HERE, '..', 'CV - Ruben Romero - Hyb.pdf'));
const htmlPath = arg('html', path.join(HERE, '..', 'cv.html'));
const lsPath = arg('ls', path.join(HERE, 'letter-spacing.json'));

const cv = (await import(pathToFileURL(contentPath).href)).default;

// ---------- utilidades ----------
const b64 = (file) => fs.readFileSync(path.join(HERE, file)).toString('base64');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
// [[dominio.com]] -> enlace a https://dominio.com · [[a@b.com]] -> mailto · [[texto|https://url]]
// {{dos palabras}} -> no se separan al partir la línea (evita que una palabra quede sola en la línea siguiente)
const rich = (s) =>
  esc(s)
    .replace(/\[\[(.+?)\]\]/g, (_, inner) => {
      const [text, url] = inner.split('|');
      const href = url ?? (text.includes('@') ? 'mailto:' + text : 'https://' + text);
      return `<a href="${href}">${text}</a>`;
    })
    .replace(/\{\{(.+?)\}\}/g, '<span class="nw">$1</span>');

const font = (file, weight) => `@font-face {
  font-family: 'CV Sans';
  font-weight: ${weight};
  font-style: normal;
  src: url(data:font/ttf;base64,${b64('fonts/' + file)}) format('truetype');
}`;

const emojiCache = new Map();
const emoji = (name) => {
  if (!emojiCache.has(name)) {
    const p = path.join(HERE, 'assets/emoji-png', name + '.png');
    if (!fs.existsSync(p)) throw new Error(`Falta el emoji "${name}" en assets/emoji-png (añade el SVG a assets/emoji-svg y ejecuta: npm run emoji)`);
    emojiCache.set(name, fs.readFileSync(p).toString('base64'));
  }
  return `<img class="emo" alt="" src="data:image/png;base64,${emojiCache.get(name)}">`;
};

// Espaciado entre letras por tipo de texto: compensa las pequeñas diferencias de anchura entre
// Selawik y la Segoe UI del original, para que las líneas partan por el mismo sitio.
const LS_SELECTORS = {
  's-name': '.s-name', 's-text': '.s-titles, .c-item, .lang', 's-h': '.s-h', 'sk-label': '.sk-label', 'sk-tag': '.sk-tag',
  h2: 'h2', profile: '.profile-t', 'exp-role': '.exp-role', 'exp-co': '.exp-co', 'exp-date': '.exp-date', bullet: '.exp li',
  tag: '.tag', 'proj-t': '.proj-t', 'proj-d': '.proj-d', 'ach-t': '.ach-t', 'ach-d': '.ach-d', 'edu-t': '.edu-t', 'edu-d': '.edu-d',
};
const spacing = fs.existsSync(lsPath) ? JSON.parse(fs.readFileSync(lsPath, 'utf8')) : {};
const spacingCss = Object.entries(spacing)
  .filter(([k]) => LS_SELECTORS[k])
  .map(([k, v]) => `${LS_SELECTORS[k]} { letter-spacing: ${v}px; }`)
  .join('\n');

// ---------- plantillas ----------
const tags = (list) => (list?.length ? `<div class="tags">${list.map((t) => `<span class="tag">${esc(t)}</span>`).join('')}</div>` : '');

const sidebar = (s) => `<aside class="side">
  <div class="s-head">
    <div class="photo"><img src="data:image/jpeg;base64,${b64('assets/photo.jpg')}" alt="${esc(s.name)}"></div>
    <div class="s-name">${esc(s.name)}</div>
    <div class="s-titles">${s.titles.map((t) => `<div>${esc(t)}</div>`).join('')}</div>
  </div>
  <div class="s-h">${esc(s.labels.contact)}</div>
  <div class="contact">
    ${s.contact.map((c) => `<div class="c-item" data-lines="${c.lines.length}">${emoji(c.icon)}${c.lines.map(rich).join('<br>')}</div>`).join('\n    ')}
  </div>
  <div class="s-h s-skills">${esc(s.labels.skills)}</div>
  <div class="skills">
    ${s.skills.map((g) => `<div class="sk-group"><div class="sk-label">${esc(g.label)}</div><div class="sk-tags">${g.tags.map((t) => `<span class="sk-tag">${esc(t)}</span>`).join('')}</div></div>`).join('\n    ')}
  </div>
  <div class="s-h s-langs">${esc(s.labels.languages)}</div>
  <div class="langs">
    ${s.languages.map(([name, level]) => `<div class="lang"><span>${esc(name)}</span><span class="dots" title="${level}/5">${[1, 2, 3, 4, 5].map((i) => `<i${i <= level ? ' class="on"' : ''}></i>`).join('')}</span></div>`).join('\n    ')}
  </div>
</aside>`;

const sections = {
  profile: (s) => `<p class="profile-t">${rich(s.text)}</p>`,
  experience: (s) =>
    s.items
      .map(
        (e) => `<div class="exp">
      <div class="exp-role">${esc(e.role)}</div>
      <div class="exp-co">${rich(e.company)}</div>
      <div class="exp-date">${esc(e.date)}</div>
      <ul>${e.bullets.map((b) => `<li>${rich(b)}</li>`).join('')}</ul>
      ${tags(e.tags)}
    </div>`,
      )
      .join('\n    '),
  projects: (s) =>
    s.items
      .map(
        (p) => `<div class="proj">
      <div class="proj-t">${emoji(p.icon)}${rich(p.title)}</div>
      <div class="proj-d">${rich(p.text)}</div>
      ${tags(p.tags)}
    </div>`,
      )
      .join('\n    '),
  achievements: (s) => `<div class="achs">${s.items.map((a) => `
      <div class="ach">${emoji(a.icon)}<div class="ach-t">${esc(a.title)}</div><div class="ach-d">${rich(a.text)}</div></div>`).join('')}
    </div>`,
  education: (s) =>
    s.items
      .map((e) => `<div class="edu"><div class="edu-t">${esc(e.title)}</div>${(e.lines ?? [e.text]).map((l) => `<div class="edu-d">${rich(l)}</div>`).join('')}</div>`)
      .join('\n    '),
};

const page = (blocks) => `<div class="page">
${sidebar(cv.sidebar)}
<main class="main">
  ${blocks
    .map((s) => {
      if (!sections[s.type]) throw new Error(`Tipo de sección desconocido: ${s.type}`);
      return `<section class="sec sec-${s.type}">
    <h2>${esc(s.title)}</h2>
    ${sections[s.type](s)}
  </section>`;
    })
    .join('\n  ')}
</main>
</div>`;

const html = `<!doctype html>
<html lang="${esc(cv.meta.lang)}">
<head>
<meta charset="utf-8">
<title>${esc(cv.meta.title)}</title>
<meta name="author" content="${esc(cv.sidebar.name)}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
${font('selawk.ttf', 400)}
${font('selawksb.ttf', 600)}
${font('selawkb.ttf', 700)}
${fs.readFileSync(path.join(HERE, 'cv.css'), 'utf8')}
${spacingCss}
@media screen { body { background: #525659; } .page { margin: 16px auto; background: #fff; box-shadow: 0 2px 12px rgba(0, 0, 0, .4); } }
</style>
</head>
<body>
${cv.pages.map(page).join('\n')}
</body>
</html>
`;
fs.mkdirSync(path.dirname(htmlPath), { recursive: true });
fs.writeFileSync(htmlPath, html);

// ---------- PDF + comprobaciones ----------
const browser = await launch();
const tab = await browser.newPage();
await tab.setViewport({ width: 794, height: 1123 });
await tab.emulateMediaType('print');
await tab.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
await tab.evaluate(() => document.fonts.ready);
await tab.evaluate(() => Promise.all([...document.images].map((i) => i.decode().catch(() => {}))));

const report = await tab.evaluate(() => {
  const out = { fonts: [...document.fonts].map((f) => `${f.family} ${f.weight} ${f.status}`), pages: [], wraps: [] };
  const lines = (el) => {
    const r = document.createRange();
    r.selectNodeContents(el);
    const tops = [];
    for (const rc of r.getClientRects()) if (rc.width > 0.5 && !tops.some((t) => Math.abs(t - rc.top) < 3)) tops.push(rc.top);
    return tops.length;
  };
  const px = (v) => Math.round(v * 10) / 10;
  document.querySelectorAll('.page').forEach((pg, i) => {
    const box = pg.getBoundingClientRect();
    const side = pg.querySelector('.side');
    const main = pg.querySelector('.main');
    const bottomOf = (el) => Math.max(...[...el.querySelectorAll('*')].map((e) => e.getBoundingClientRect().bottom));
    const limit = (el) => box.bottom - parseFloat(getComputedStyle(el).paddingBottom);
    const count = (sel) => [...pg.querySelectorAll(sel)].map(lines);
    out.pages.push({
      page: i + 1,
      pageHeight: px(box.height),
      mainBottom: px(bottomOf(main) - box.top),
      mainFree: px(limit(main) - bottomOf(main)),
      sidebarBottom: px(bottomOf(side) - box.top),
      sidebarFree: px(limit(side) - bottomOf(side)),
      lineCounts: {
        profile: count('.profile-t'),
        bullets: [...pg.querySelectorAll('.exp')].map((e) => [...e.querySelectorAll('li')].map(lines)),
        projects: count('.proj-d'),
        achievements: count('.ach-d'),
        education: [...pg.querySelectorAll('.edu')].map((e) => [...e.querySelectorAll('.edu-d')].reduce((n, d) => n + lines(d), 0)),
      },
    });
    const single = '.s-name, .s-titles div, .s-h, .sk-label, .sk-tag, .lang span:first-child, h2, .exp-role, .exp-co, .exp-date, .proj-t, .ach-t, .edu-t, .tag';
    pg.querySelectorAll(single).forEach((el) => {
      if (lines(el) > 1) out.wraps.push(`p${i + 1} ${el.className || el.tagName}: ${el.textContent.trim().slice(0, 60)}`);
    });
    pg.querySelectorAll('.c-item').forEach((el) => {
      if (lines(el) > Number(el.dataset.lines)) out.wraps.push(`p${i + 1} contacto: ${el.textContent.trim().slice(0, 60)}`);
    });
    pg.querySelectorAll('.main .tags').forEach((el) => {
      const tops = new Set([...el.children].map((c) => Math.round(c.getBoundingClientRect().top)));
      if (tops.size > 1) out.wraps.push(`p${i + 1} etiquetas en ${tops.size} filas: ${el.textContent.trim().slice(0, 60)}`);
    });
  });
  return out;
});

await tab.pdf({ path: pdfPath, width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
await browser.close();

report.pdf = pdfPath;
report.pdfBytes = fs.statSync(pdfPath).size;
console.log(JSON.stringify(report, null, 1));

const problems = [];
for (const p of report.pages) {
  if (p.mainFree < 0) problems.push(`Página ${p.page}: el contenido principal se sale ${-p.mainFree} px por abajo.`);
  if (p.sidebarFree < 0) problems.push(`Página ${p.page}: la barra lateral se sale ${-p.sidebarFree} px por abajo.`);
}
if (report.fonts.some((f) => !f.endsWith('loaded'))) problems.push('Alguna fuente no se ha cargado.');
for (const w of report.wraps) problems.push(`Texto partido en dos líneas: ${w}`);
if (problems.length) {
  console.error('\nATENCIÓN:\n- ' + problems.join('\n- '));
  process.exitCode = 1;
}
