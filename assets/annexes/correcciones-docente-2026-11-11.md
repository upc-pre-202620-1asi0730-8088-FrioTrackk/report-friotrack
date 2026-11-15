# Seguimiento de observaciones del docente

Corte documental: 11/11/2026. Actualización técnica AV2: 14/11/2026. Las evidencias de implementación, publicación y aceptación se identifican por separado.

| Observación | Corrección y evidencia | Estado / límite |
| --- | --- | --- |
| Formato de carátula | Carátula original centrada conservada en README. | Excluida de esta revisión por solicitud del autor; no se acredita conformidad del 100% con el ejemplo. |
| Gráficos de colaboración | Project Report Collaboration Insights: gráfico histórico y [corte reproducible de 43 commits](../evidence/report-collaboration-2026-11-11.json). | Corregido el artefacto; el gráfico no crea contribuciones. |
| Varios escenarios por historia | Catálogo de 43 historias con 86 escenarios Given/When/Then; verificador de reporte. | Corregido en la documentación. |
| Contextos genéricos al final | Epics, historias y diagramas presentan IAM después del dominio core y de apoyo. | Corregido. |
| Web Application y SPA distintas | C4 de 4.6.3: servidor estático y programa Vue separados. | Corregido; cuatro contenedores. |
| Mejorar C4 | Contexto, contenedores y componentes actual/objetivo en 4.6.2–4.6.4. | Corregido; alcance y tecnologías explícitos. |
| Clases alineadas con DDD | Cinco diagramas en 4.7.1: raíces, entidades, VO, repositorios y referencias por ID. Sensor independiente; recuperación térmica y señal distintas. | Diseño DDD documentado; incremento AV2 implementado con EF Core y PostgreSQL. |
| Sprint Goal con plantilla | Ambos objetivos usan Our focus is on / We believe it delivers / This will be confirmed when. | Corregido; no equivale a goal aceptado. |
| Estados de tareas | Backlogs descompuestos en 8 y 50 tareas, estimaciones de revisión de 4–8 h, estados estándar y notas de evidencia. | Estados y estimaciones documentados; aceptación del equipo no registrada en este corte. |
| Repositorios públicos faltantes | Cuatro productos enlazados en 5.1.2: reporte, landing, frontend y API independiente. | Repositorios publicados; evidencia en sus releases y fuentes del 10/11. |
| Releases correctas | Versiones y commits identificados en 5.1.2; PDF del reporte actualizado en v2.0.4. | Corregido el versionado; una release no equivale a despliegue Azure. |
| Estructura de código | 5.1.3 y 4.7.1.6 documentan contextos del frontend, puerto/adaptador y API separada. | Fuentes organizadas por contextos; persistencia EF Core/PostgreSQL publicada en AV2. |
| Participación y número de commits | Se conservan autorías e historial real, sin reasignar trabajo. | Actividad atribuida a sus autores según el historial de cada repositorio. |
| Evidencia de sprint y colaboración | Date/Time/Location separados; matrices por aspecto; cortes de pruebas fechados. | Actas y asignaciones no registradas en el corte documental. |

Los recibos históricos conservan su fecha y entorno. La publicación AV2 del 14/11/2026 está documentada en los recibos de [API](../evidence/av2/redeployment-api.json), [SPA](../evidence/av2/redeployment-frontend.json) y [landing](../evidence/av2/redeployment-landing.json). La ingesta física de sensores está fuera del alcance de esta versión.
