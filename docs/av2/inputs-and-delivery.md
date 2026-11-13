# Entradas necesarias y checklist de entrega AV2

## Decisiones y accesos

| Entrada | Para qué se necesita | Qué se puede adelantar |
| --- | --- | --- |
| Fecha/hora de AV2 y rúbrica específica del aula, si existe | Confirmar el cierre de semana 12 | Estructura, código y protocolo. El statement indica hasta 24 horas después del inicio de la sesión regular correspondiente; con dos sesiones semanales se considera la segunda. |
| Integrantes activos, líderes, colaboradores y capacidad | Completar planning, LACX y responsables del tablero | Propuesta de tareas, sin inventar acuerdos o aceptación. |
| Motor y destino BD; presupuesto y política de datos existentes | Publicar persistencia relacional sin perder cuentas o información | PostgreSQL local y migraciones de desarrollo coherentes con el diseño actual. |
| Autenticación Azure y acceso a recursos | Publicar API, BD, SPA y landing y obtener recibos reales | Builds, pruebas, configuración y herramientas de publicación. |
| Conexión Trello con permiso de edición | Leer y actualizar el tablero real sin duplicar tarjetas | CSV y descripciones preparadas. GitHub no concede acceso a Trello. |
| Participantes de ambos segmentos y autorización de grabación | Ejecutar validación real | Guion, tareas, fichas y agenda propuesta. |
| Grabaciones y opiniones auténticas | Registros, análisis, About-the-Product y entrevistas consolidadas | Pautas de montaje y diseño de títulos. |
| Sesiones de trabajo y testimonios de cada integrante | About-the-Team y Student Outcome | Guion y lista de escenas necesarias. |
| Cuentas Stream/YouTube y enlaces finales | Publicar videos y habilitar reproductores en landing | Código de integración con URLs opcionales. Si no existe conexión directa, el equipo sube los MP4 y entrega los enlaces. |
| Responsabilidades y calificaciones del Team Leader | Performance Report AV2 | Formato Word/PDF; no inventar evaluación individual. |

No enviar contraseñas ni tokens por el chat o Git. Usar conexiones autorizadas y variables privadas cuando corresponda. La autenticación Microsoft mediante código tiene vigencia limitada: iniciar un flujo nuevo al momento de publicar, sin reutilizar códigos antiguos.

## Secuencia de trabajo

1. Acordar incremento y capacidad del Sprint 3 y confirmar los segmentos.
2. Implementar backend relacional, REST/OpenAPI, integración SPA y pruebas; actualizar el diseño según el código real.
3. Publicar y verificar una versión estable, con límites de demostración explícitos.
4. Ejecutar validación de ambos segmentos, registrar resultados y priorizar hallazgos.
5. Corregir y comprobar mejoras seleccionadas; registrar aceptación auténtica.
6. Consolidar videos, reporte, presentación, participación y ZIP; revisar enlaces como los abrirá el docente.

El reclutamiento y la grabación de sesiones reales de trabajo del equipo pueden avanzar en paralelo al desarrollo. La validación del producto debe realizarse sobre una versión identificada y funcional, no sobre promesas de funciones futuras.

## Entregables y comprobación final

- [ ] Reporte acumulativo en Markdown en repositorio público, con carátula del formato aprobado, versiones, colaboración, índice y Student Outcome actualizados.
- [ ] Correcciones de capítulos anteriores y diseño consistentes con backend y base implementados.
- [ ] Ocho subsecciones de Sprint 3 completas con datos reales y tablas editables.
- [ ] 5.3: protocolo, registro de 3–5 entrevistas por segmento y evaluación heurística en formato Anexo D.
- [ ] About-the-Product y About-the-Team publicados en Stream y YouTube e incrustados en landing.
- [ ] Nuevas versiones de landing y Web App publicadas; primera versión Web Services publicada con PostgreSQL/EF Core y documentación Swagger.
- [ ] API con pruebas unitarias y de integración/aceptación en su repositorio canónico.
- [ ] Productos y documentación con inglés por defecto y soporte ES/EN; revisión de accesibilidad e integración del servicio externo declarado.
- [ ] Tablero actual, actas y aceptación verificables; contribuciones/revisiones reales por producto.
- [ ] Videos de navegación y exposición accesibles; exposición de todos los miembros ante cámara de no más de 30 minutos.
- [ ] Conclusiones contrastadas con validación, bibliografía APA y anexos con páginas diferenciadas al exportar.
- [ ] PPTX/PDF con presentación del equipo, fotos, nombres, apellidos y carrera.
- [ ] Performance Word/PDF elaborado por Team Leader, con responsabilidades y calificaciones reales de las alternativas 20, 16, 13, 07 o 00.
- [ ] ZIP con código/artefactos aplicables; excluir credenciales, bases pobladas y cachés privados.
- [ ] URLs del docente comprobadas, releases correctas y PDF sin enlaces a rutas privadas de la computadora.

## Nombres de archivos

| Archivo | Nombre |
| --- | --- |
| Reporte | `upc-pre-202620-1asi0730-8088-blackstartup-report-av2.pdf` |
| Presentación | `upc-pre-202620-1asi0730-8088-blackstartup-keynote-av2.pptx` y `.pdf` |
| Participación | `upc-pre-202620-1asi0730-8088-blackstartup-performance-av2.docx` y `.pdf` |
| Exposición | `upc-pre-202620-1asi0730-8088-blackstartup-expo-av2.mp4` |
| Validación | `upc-pre-202620-1asi0730-8088-blackstartup-validation-sprint-3.mp4` |
| Producto | `upc-pre-202620-1asi0730-8088-blackstartup-about-the-product-sprint-3.mp4` |
| Equipo | `upc-pre-202620-1asi0730-8088-blackstartup-about-the-team-sprint-3.mp4` |
| Navegación | `upc-pre-202620-1asi0730-8088-blackstartup-productnavigation-sprint-3.mp4` |

La lista de preparación no se marca completada por la existencia del archivo plantilla. Cada entrega debe tener material propio, resultados y enlaces comprobables.
