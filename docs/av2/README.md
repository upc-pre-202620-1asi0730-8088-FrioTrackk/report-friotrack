# Preparación de AV2 — FríoTrack

Estos documentos preparan el Sprint 3 y las secciones nuevas de AV2. No certifican entrevistas, reuniones, videos, publicación en cloud ni aceptación que todavía no se hayan realizado. La carátula y las entregas anteriores se conservan en el informe principal.

Referencia: enunciado UPC 1ASI0730, periodo 202620, AV2 semana 12, páginas 32–33; validación página 27; videos Anexo C página 39; heurísticas Anexo D páginas 40–41. El PDF adjuntado nuevamente por el equipo tiene el mismo contenido que la copia anterior.

| Documento | Uso |
| --- | --- |
| [Sprint 3](sprint-3.md) | Ocho secciones requeridas y propuesta de planificación, con datos reales pendientes identificados. |
| [Backlog propuesto](sprint3-backlog-proposal.csv) | Tareas de 4–8 horas para discutir con el equipo; no constituyen capacidad ni compromiso aceptados. |
| [Protocolo de validación](validation-protocol.md) | Tareas y preguntas por segmento para ejecutar sobre una versión estable. |
| [Registro vacío de entrevistas](validation-records.csv) | Una fila por entrevista real, con evidencias y resultados. |
| [Evaluación heurística](heuristics-template.md) | Estructura de Anexo D, severidad 1–4 y detalle de hallazgos observados. |
| [Guiones de videos](video-scripts.md) | Product, Team, navegación y exposición; grabaciones auténticas aún necesarias. |
| [Esquema de presentación](keynote-outline.md) | Estructura para preparar la presentación AV2 con evidencias verificadas. |
| [Entradas y entrega](inputs-and-delivery.md) | Lo que debe proporcionar el equipo, dependencias y nombres de archivos. |
| [Plan por integrante](team-action-plan.md) | Reparto propuesto, videos/entrevistas, cuentas y orden de trabajo para completar AV2. |

El repositorio Markdown continúa siendo la fuente editable. Los documentos de preparación deben integrarse al informe con sus resultados reales y exportarse a PDF antes de entregar. No reemplazar las tablas de historias o backlog por screenshots de Trello.

## Incremento técnico en preparación

Las fuentes del incremento incorporan PostgreSQL con EF Core, recursos REST y OpenAPI/Swagger, integrados con la SPA. El [informe principal](../../README.md#523-sprint-3--preparación-av2) registra el corte de implementación y separa sus pruebas de la aceptación y publicación pendientes. El [esquema AV2](../../assets/architecture/av2/README.md) se deriva de la migración inicial: 18 tablas, 31 FK e identificadores compatibles con el contrato histórico.

Los [registros técnicos](../../assets/evidence/av2/technical-verification.json) identifican los commits y pruebas ejecutadas. La landing está publicada en GitHub Pages; el despliegue de la nueva SPA/API y su base cloud sigue pendiente.

Se priorizan acceso y permisos, recursos independientes, programación/reserva consistente, lecturas autorizadas, alertas, atención e historial. La descarga del reporte persistido es JSON y el CSV de la SPA es una exportación distinta. Los datos son de demostración; no se afirma recepción física de sensores, correo verificado, pagos o funcionalidades fuera del incremento implementado.

El equipo debe acordar alcance, líderes, colaboradores, capacidad y criterios de aceptación en una planificación real. La estructura DDD y una base de datos vacía no acreditan por sí solas el cumplimiento de las historias.
