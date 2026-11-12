# Preparación del tablero de FríoTrack

Este paquete prepara la regularización de 58 tareas del reporte: 8 de Sprint 1 y 50 de Sprint 2. **No es evidencia de que Trello se haya actualizado.** No se pudo consultar el tablero con las herramientas de lectura disponibles; eso no permite concluir que sea privado ni conocer su estado actual.

Tablero referenciado: <https://trello.com/b/6qrvOukt/blackstartup-fr%C3%ADotrack>.

## Qué está preparado

- `tarjetas-preparadas-58.csv` y `.json`: nombres, descripciones, listas propuestas, IDs, horas y atribución histórica para una carga mediante API o revisión manual.
- `to-do-titulos.txt`: 24 títulos para la lista To Do.
- `to-review-titulos.txt`: 34 títulos para la lista To Review.
- `in-process-titulos.txt` y `done-titulos.txt`: vacíos porque no hay evidencia registrada que permita asignar esos estados a estas tareas de corrección.
- `descripciones-tarjetas.md`: contenido completo para las tarjetas.
- `registro-aceptacion-58.csv`: registro por tarea con campos sin completar para resultados reales.
- `CHECKLIST-ACEPTACION.md`: pasos para documentar la revisión real y preparar las evidencias del reporte.

Las horas son **estimaciones posteriores de revisión**, no tiempos históricos. Los nombres históricos se conservan como atribución, sin convertirlos en responsables actuales. No se asigna trabajo pendiente a Benjamin, que consta retirado. El equipo debe confirmar las asignaciones actuales.

## Actualización manual sin control de pantalla

1. Un integrante con permiso de edición abre el tablero y exporta el JSON actual como respaldo. No borrar las tarjetas históricas ni su actividad.
2. Comprobar si ya existen los Task ID `S1-T01A` a `S1-T04B` y `S2-T01A` a `S2-T19B`. Actualizar por ID; no duplicar tareas existentes. Las tareas antiguas sin sufijo A/B mantienen su referencia de origen en las descripciones.
3. Usar las listas **To Do**, **In Process**, **To Review** y **Done**. Mantener la identificación de sprint mediante etiqueta o campo.
4. Cuando falten tarjetas, pegar en la lista correspondiente el contenido del archivo de títulos. Trello puede separar las líneas en tarjetas. Después completar cada descripción desde `descripciones-tarjetas.md`, etiquetas y responsable confirmado.
5. Revisar estados con el equipo: To Do es pendiente; In Process exige trabajo realmente iniciado; To Review tiene un resultado comprobable pendiente de aceptación; Done requiere aceptación registrada. Los estados preparados son una propuesta basada en el reporte, no una orden de sobrescribir el tablero real.
6. Adjuntar enlaces al producto y resultados reales. Mantener la fecha actual de la revisión; no inventar movimientos, reuniones ni aceptaciones de octubre.
7. Conservar el nuevo export JSON, enlaces a tarjetas y una captura tomada por el equipo que muestre el tablero real. Se puede entregar esa evidencia para integrarla al reporte sin conceder acceso a la pantalla.

## Actualización mediante API

Trello no ofrece importación genérica directa de CSV/JSON. Estos archivos sirven como fuente para automatización por API o para revisión manual. Una integración autenticada debe primero leer el tablero, relacionar listas y miembros, detectar duplicados por Task ID y mostrar un resumen de cambios antes de aplicarlos. No se requiere una base de datos propia para el tablero.

Nunca enviar contraseñas o tokens por el chat. Si se habilita una conexión autorizada de Trello, los cambios pueden realizarse sin Computer Use. Una sesión iniciada en GitHub no concede permisos de Trello.

Fuentes oficiales consultadas:

- [Importar datos en Trello](https://support.atlassian.com/trello/docs/importing-data-into-trello/): pegado de títulos y API; no hay importador genérico.
- [Exportar datos de Trello](https://support.atlassian.com/trello/docs/exporting-data-from-trello/): export JSON disponible para miembros del tablero; CSV depende del plan.
