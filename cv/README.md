# CV

- **`CV - Ruben Romero - Hyb.pdf`**: el CV actualizado (noviembre de 2026), en inglés, dos páginas A4.
- **`cv.html`**: el mismo CV en una sola página web, con fuentes e imágenes dentro. Se abre en cualquier navegador.
- **`original/`**: el CV de junio de 2026, tal como estaba.
- **`src/`**: el generador. Reproduce el diseño del CV original y lo rellena con el contenido de `src/content.mjs`.

## Cambiar un texto

Todo el contenido está en `src/content.mjs`. Después de editarlo:

```bash
cd src
npm install        # solo la primera vez (ocupa unos 110 MB)
node build.mjs     # escribe ../CV - Ruben Romero - Hyb.pdf y ../cv.html
```

Hace falta Node 22.17 o posterior. En Windows y macOS el generador usa el Chrome o el Edge que ya tengas instalado; en Linux usa un Chromium que viene con `npm install`. Para usar otro navegador, pon la ruta de su ejecutable en la variable `CHROME_PATH`.

Este CV se generó en Linux. En Windows y macOS el generador no se ha probado: si allí alguna línea parte por otro sitio y algo deja de caber, el informe lo avisa.

Al terminar, `build.mjs` imprime un informe. Lo que hay que mirar:

- `mainFree` y `sidebarFree`: píxeles libres al final de cada página. Si alguno es negativo, el contenido no cabe y hay que acortar texto.
- `wraps`: títulos, fechas o etiquetas que se han partido en dos líneas. Debe estar vacío.

Las dos páginas están casi llenas: en la primera quedan unos 19 px y en la segunda unos 14 px, más o menos una línea de texto en cada una.

Dentro de un texto, `[[dominio.com]]` crea un enlace y `{{dos palabras}}` impide que la línea se parta entre ellas.

## Cómo está hecho

El CV original se imprimió desde una página web con Chrome. Aquí se hace lo mismo: `build.mjs` monta el HTML, lo abre en un Chromium sin interfaz y lo guarda como PDF.

- `src/cv.css` es el diseño. Las medidas salen de medir el PDF original.
- La tipografía es **Selawik**, la sustituta abierta que publica Microsoft para Segoe UI, que es la del original y no se puede redistribuir.
- `src/letter-spacing.json` ajusta el espaciado entre letras de cada tipo de texto para que las líneas ocupen lo mismo que con Segoe UI.
- Los iconos son los Fluent Emoji de Microsoft, los mismos dibujos que usaba el original. Para añadir uno, copia su SVG en `src/assets/emoji-svg/` y ejecuta `npm run emoji`.

Respecto al original hay tres cambios hechos a propósito: el segundo teléfono va alineado con el primero, el correo y las webs son enlaces, y el texto del PDF sale en orden de lectura para los filtros automáticos de CV.

## Comprobar que el diseño no se ha movido

`src/reference/content.original.mjs` contiene el texto exacto del CV de junio. Al generarlo con este diseño y compararlo con el PDF original, 237 de las 239 líneas de texto quedan a la misma altura exacta y las otras 2 a un píxel; la posición horizontal coincide en todas.

```bash
cd src
python3 -m venv /tmp/cvtools && /tmp/cvtools/bin/pip install -r tools/requirements.txt
node build.mjs --content reference/content.original.mjs --pdf /tmp/replica.pdf --html /tmp/replica.html
/tmp/cvtools/bin/python tools/compare.py "../original/CV - Ruben Romero- Hyb (original, jun 2026).pdf" /tmp/replica.pdf
```

`tools/inkcmp.py` compara iconos y viñetas, `tools/sidebyside.py` pone dos recortes uno al lado del otro y `tools/dump.py` vuelca las medidas de un PDF.

## Licencias

- Selawik: SIL Open Font License 1.1 (`src/fonts/LICENSE-Selawik.txt`).
- Fluent Emoji: MIT (`src/assets/emoji-svg/LICENSE-fluentui-emoji.txt`).
