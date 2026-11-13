# Validación y exportación del informe

El informe editable y la carátula se mantienen en `README.md`. El PDF es una exportación; no se reconstruye la carátula desde Word ni desde una imagen de página completa.

## Comprobación estructural

```shell
python scripts/check-report.py
```

El verificador comprueba referencias y anclas locales, escenarios completos, estimaciones y estados de tareas, orden de contextos genéricos, campos de planificación y las 22 vistas históricas con sus fuentes nativas y hashes. Para AV2 verifica además claves e índices del catálogo relacional, seis vistas del esquema, fuentes editables, enlaces de los documentos de preparación y estimaciones de la propuesta de Sprint 3. La comprobación no acredita aceptación de tareas, trabajo del equipo ni un despliegue nuevo.

## Catálogo relacional AV2

Con `friotrack-api` y este repositorio en directorios hermanos:

```shell
python scripts/build-av2-schema.py
```

El script lee la migración inicial EF Core y genera el catálogo JSON/Markdown, seis vistas SVG y formas nativas diagrams.net en `assets/architecture/av2/`. `--migration` admite una ruta distinta. No requiere base de datos ni credenciales. `schema-manifest.json` conserva los hashes de las vistas; los C4 mantienen un manifiesto separado. Si cambia el esquema, revisar el mapa de contextos, regenerar y comprobar las imágenes antes de exportar el informe.

## Exportación a PDF

Requiere Pandoc, Node.js con Playwright y Chromium, y Python con `pypdf` y `reportlab`. `CHROME_PATH` permite elegir una instalación de Chrome para el proceso de exportación sin interfaz; no utiliza un perfil personal ni controla ventanas abiertas.

Desde la raíz del repositorio:

```shell
pandoc README.md -f gfm -t html5 --standalone --metadata title="FríoTrack Informe TB1" --css scripts/report.css -o report.html
node scripts/render-report.cjs
python scripts/assemble-report.py
```

Para el corte de preparación AV2, utilizar el mismo proceso y ejecutar `python scripts/assemble-report.py --stage av2`. El resultado usa el sufijo `report-av2.pdf` y conserva el PDF histórico TB1. La carátula procede del Markdown original; las entrevistas, grabaciones, planificación y nueva publicación de SPA/API conservan su estado real pendiente.

El renderizador verifica que todas las imágenes carguen. Para las vistas de arquitectura utiliza sus originales SVG y hojas horizontales. Los enlaces a archivos locales se convierten en enlaces públicos al repositorio para que funcionen al descargar el PDF. La composición conserva la carátula Markdown y añade numeración desde la segunda página. El resultado se guarda en `deliverables/upc-pre-202620-1asi0730-8088-blackstartup-report-tb1.pdf`.

Antes de publicar, renderizar el PDF a imágenes con Poppler y revisar figuras, tablas, pies, saltos de página y la carátula. Registrar la nueva revisión por separado de los recibos históricos de octubre.
