// Convierte los SVG de emoji (Fluent Emoji, de Microsoft) en PNG con fondo transparente.
// Uso: node raster-emoji.mjs assets/emoji-svg assets/emoji-png 160
// Los SVG usan filtros que no todos los visores de PDF dibujan bien; por eso el CV incrusta los PNG.
import fs from 'node:fs';
import path from 'node:path';
import { launch } from './browser.mjs';

const [src = 'assets/emoji-svg', dst = 'assets/emoji-png', size = '160'] = process.argv.slice(2);
const px = Number(size);
fs.mkdirSync(dst, { recursive: true });
const browser = await launch();
const page = await browser.newPage();
await page.setViewport({ width: px, height: px, deviceScaleFactor: 1 });
let n = 0;
for (const f of fs.readdirSync(src).filter((f) => f.endsWith('.svg')).sort()) {
  const svg = fs.readFileSync(path.join(src, f)).toString('base64');
  await page.setContent(`<html><body style="margin:0;background:transparent"><img src="data:image/svg+xml;base64,${svg}" style="display:block;width:${px}px;height:${px}px"></body></html>`);
  await page.evaluate(() => Promise.all([...document.images].map((i) => i.decode())));
  await page.screenshot({ path: path.join(dst, f.replace(/\.svg$/, '.png')), omitBackground: true, clip: { x: 0, y: 0, width: px, height: px } });
  n++;
}
await browser.close();
console.log(`${n} emoji -> ${dst} (${px}px)`);
