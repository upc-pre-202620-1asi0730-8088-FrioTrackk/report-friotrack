# Fuentes de evidencia — FríoTrack TB1

- Informe y contribuciones: historial del repositorio actual, rama `develop`, 07–08/10/2026; metadatos en `current-commits.json`.
- Implementación: frontend integrado en `main`, revisión `dc49d7e28e13c8d0f78fa913dd5353ea162012c6`.
- Ejecución publicada: registros Azure y capturas de 08/10/2026, horario de Lima.
- Diseño y material local anterior: artefactos del Capítulo IV y archivo de evidencias fechado en `archive/2026-10-07/`.
- Requisitos de entrega: enunciado UPC 1ASI0730, periodo 202620, sección TB1 y estructura de Sprint 2.

## Revisión del código fuente y del informe de noviembre

- La [revisión del 10/11/2026](review-corrections-2026-11-10.json) documenta las correcciones de código y del informe: 18 pruebas frontend, compilación de producción y 26 comprobaciones locales del servicio independiente. No registra un nuevo despliegue en Azure.
- El recibo [repository-verification.json](repository-verification.json) conserva el corte histórico de octubre: 15 pruebas de dominio frontend, 222 módulos compilados y 26 comprobaciones locales de la API. Los recibos Azure y sus 12 comprobaciones HTTPS pertenecen a ese despliegue anterior; no validan la revisión de noviembre en producción.
- El [corte de colaboración del 11/11/2026](report-collaboration-2026-11-11.json) cuenta los 43 commits sin merges alcanzables desde `02022660eb5954dd0ead0ef5f33d39c1db45b02e`, agrupados por el nombre de autor registrado en Git. El [gráfico de autores y fechas](../images/chapter-05/report-collaboration-2026-11-11.png) conserva este corte reproducible; no incluye los commits de la corrección posterior ni sustituye la captura histórica del equipo.

Las fechas de autor del gráfico se conservan tal como aparecen en los metadatos Git. Los conteos no acreditan por sí solos identidad, horas invertidas, revisión de tareas o una contribución equilibrada, y no se suman con los de otros productos.

Las imágenes de datos operativos utilizan registros de prueba. Los recibos técnicos no sustituyen actas, exposición ni evaluación individual del equipo.

## Cierre técnico del 11/11/2026

- [Integración local](local-integrated-acceptance.json): 157 comprobaciones aprobadas con API real aislada y bundle de producción, ES/EN, 390/1440 px. No acredita Azure ni captura del escritorio.
- [API local](local-api-verification-2026-11-11.json): 26 comprobaciones de autenticación, persistencia, comandos y permisos.
- [Consulta pública previa](public-predeployment-2026-11-11.json): frontend, landing y API disponibles; los HTML todavía difieren de las fuentes corregidas en ese corte.
- [Preparación del tablero](../annexes/tablero-preparado/estado-preparacion.json): 58 tareas propuestas, sin actualización externa ni aceptación inventada.
- [Guía de cierre](../annexes/cierre-evidencias-tb1.md): acceso Trello/Azure requerido y revisión auténtica del equipo.
