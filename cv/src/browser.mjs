// Arranca un Chromium sin interfaz. Qué navegador se usa:
//
//   1. El de la variable CHROME_PATH, si está definida (Chrome, Edge o Chromium).
//   2. En Windows y macOS, el Chrome o el Edge que ya esté instalado.
//   3. En Linux, el del paquete @sparticuz/chromium, que trae el navegador y sus bibliotecas
//      dentro de node_modules: no hace falta tener Chrome instalado. Ese paquete solo sirve en Linux.
import fs from 'node:fs';
import path from 'node:path';
import puppeteer from 'puppeteer-core';

export function installedBrowser() {
  const fromEnv = process.env.CHROME_PATH;
  if (fromEnv) {
    if (!fs.existsSync(fromEnv)) throw new Error(`CHROME_PATH apunta a un archivo que no existe: ${fromEnv}`);
    return fromEnv;
  }
  const candidates = [];
  if (process.platform === 'win32') {
    const bases = [process.env.PROGRAMFILES, process.env['PROGRAMFILES(X86)'], process.env.LOCALAPPDATA].filter(Boolean);
    for (const b of bases) candidates.push(path.join(b, 'Google', 'Chrome', 'Application', 'chrome.exe'));
    for (const b of bases) candidates.push(path.join(b, 'Microsoft', 'Edge', 'Application', 'msedge.exe'));
  } else if (process.platform === 'darwin') {
    candidates.push(
      '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
      '/Applications/Chromium.app/Contents/MacOS/Chromium',
    );
  }
  return candidates.find((p) => fs.existsSync(p));
}

export async function launch() {
  const exe = installedBrowser();
  if (exe) return puppeteer.launch({ executablePath: exe, headless: true, args: ['--font-render-hinting=none'] });
  if (process.platform !== 'linux') {
    throw new Error('No encuentro Chrome ni Edge. Instala Chrome o define la variable CHROME_PATH con la ruta de su ejecutable.');
  }
  process.env.AWS_LAMBDA_JS_RUNTIME ??= 'nodejs22.x'; // así el paquete desempaqueta también sus bibliotecas
  const { default: chromium } = await import('@sparticuz/chromium');
  chromium.setGraphicsMode = false;
  return puppeteer.launch({ executablePath: await chromium.executablePath(), args: chromium.args, headless: 'shell' });
}
