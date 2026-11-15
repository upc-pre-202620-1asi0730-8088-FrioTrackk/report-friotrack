# Documentación AV2 — FríoTrack

Referencia: enunciado UPC 1ASI0730, periodo 202620, AV2 semana 12, páginas 32–33; validación página 27; videos Anexo C página 39; evaluación heurística Anexo D páginas 40–41.

| Documento | Contenido |
| --- | --- |
| [Sprint 3](sprint-3.md) | Planificación, contratos y evidencias del incremento. |
| [Backlog propuesto](sprint3-backlog-proposal.csv) | Descomposición de tareas y estimaciones de revisión de 4–8 horas. |
| [Protocolo de validación](validation-protocol.md) | Método, tareas y preguntas por segmento. |
| [Registro de entrevistas](validation-records.csv) | Sesiones AV2-C01, AV2-L01 y AV2-L02; la ficha AV2-L03 se consulta en el informe principal. |
| [Evaluación heurística](heuristics-template.md) | Formato de Anexo D y escala de severidad 1–4. |
| [Especificaciones de videos](video-scripts.md) | Estructura y duración de Product, Team, navegación y exposición. |
| [Estructura de presentación](keynote-outline.md) | Organización temática de la presentación AV2. |
| [Entrega AV2](inputs-and-delivery.md) | Formatos y nomenclatura de los entregables. |

## Incremento técnico

El [informe principal](../../README.md#523-sprint-3--av2) registra la implementación y sus comprobaciones. El [esquema AV2](../../assets/architecture/av2/README.md) deriva de la migración inicial: 18 tablas, 31 FK e identificadores compatibles con el contrato histórico.

La landing está publicada en GitHub Pages y Azure. La SPA y la API ASP.NET Core están publicadas en Azure con PostgreSQL 17 en Neon desde el 14/11/2026. Los [registros técnicos](../../assets/evidence/av2/technical-verification.json), [recibos de publicación](../../assets/evidence/av2/redeployment-api.json) y [recorridos públicos](../../assets/evidence/av2/public-interview-verification.json) identifican fuentes, entornos y resultados. Las sesiones AV2-C01, AV2-L01, AV2-L02 y AV2-L03 se documentan en [5.3.2](../../README.md#532-registro-de-entrevistas).

La versión incluye acceso y permisos, recursos independientes, programación y reservas, lecturas autorizadas, alertas, atención e historial. El reporte persistido es JSON; la exportación CSV de la SPA es una función distinta. La telemetría corresponde a datos de demostración. Sensores físicos, envío externo de correo y pagos están fuera del alcance acreditado de esta versión.
