# portafolio

Material para presentar los proyectos de `gtrespana-bit`: un dossier para montar el perfil de Fiverr, los textos de los proyectos para LinkedIn y el CV.

- **`dossier-fiverr.pdf`**: el documento (68 páginas, en español; los textos para pegar en Fiverr van en inglés).
- **`linkedin-proyectos.md`**: textos para la sección de proyectos de LinkedIn (CotizaT, CamperOcasión, MaquinariaOcasión, Venezuela Inmuebles y KHC Auto Import), en español y en inglés.
- **`generador/`**: el código que lo produce, por si quieres cambiar un texto o un precio y volver a generarlo.
- **`cv/`**: el CV actualizado con los proyectos nuevos (`CV - Ruben Romero - Hyb.pdf`), con el mismo diseño que el anterior, y su generador. Ver `cv/README.md`.

## Contenido del PDF

| Sección | Qué trae |
|---|---|
| 00 a 03 | Cómo leerlo, resumen de lo demostrable, perfil de Fiverr listo para pegar y tecnología usada |
| 04 | 16 fichas de proyecto con cifras medidas sobre el código |
| 05 | Catálogo de 120 servicios con prueba, precio orientativo y plazo |
| 06 | 14 gigs: título, categoría, etiquetas, descripción, paquetes, extras, preguntas frecuentes y requisitos |
| 07 a 09 | Precios y orden de lanzamiento, qué arreglar en GitHub antes de publicar y datos pendientes |
| Anexos | Tabla de los 44 repositorios, palabras clave por gig y plantillas de mensajes |

## Regenerar el PDF

```bash
cd generador
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python build.py            # escribe ../dossier-fiverr.pdf
```

Los textos están en `c1_intro.py` (perfil), `c2_projects.py` (proyectos), `c3_services.py` (tecnología y catálogo),
`c4_gigs.py` (gigs) y `c5_strategy.py` (precios, GitHub, pendientes y anexos). Si un título o una descripción
supera el límite de caracteres de Fiverr, el script se detiene y lo indica.

Las tipografías de `generador/fonts/` son IBM Plex (licencia SIL Open Font License 1.1).

## Aviso

Este repositorio es público y el dossier incluye precios, estrategia y una lista de cosas que conviene
retirar de otros repositorios. La carpeta `cv/` lleva además tu correo y tus teléfonos. Conviene hacerlo privado.
