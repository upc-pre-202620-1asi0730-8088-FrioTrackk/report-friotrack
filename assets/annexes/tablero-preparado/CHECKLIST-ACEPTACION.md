# Checklist de aceptación y evidencia real

Usar esta lista en la revisión real del equipo. No está completada, no es un acta y no acredita aceptación de tareas.

## Antes de revisar

- [ ] Identificar la versión y commit realmente desplegados del frontend, API y landing.
- [ ] Confirmar responsables actuales y revisores; conservar la atribución histórica por separado.
- [ ] Relacionar cada tarjeta con su Task ID, User Story y escenarios del catálogo.
- [ ] Mantener cuatro listas de estado estándar y la etiqueta de cada sprint.
- [ ] Adjuntar los enlaces públicos que podrá abrir el docente, sin publicar credenciales.

## Para aceptar cada tarea

- [ ] El responsable demuestra el resultado sobre la versión identificada.
- [ ] Se ejecutan los escenarios aplicables, incluyendo el rechazo, límite o fallo previsto por la historia.
- [ ] Se documentan datos de entrada, resultado esperado, resultado observado y entorno.
- [ ] Se enlaza evidencia: commit/PR, CI, archivo de salida o ejecución real correspondiente al criterio.
- [ ] Se registra la decisión del revisor y su fecha real en la tarjeta o en `registro-aceptacion-58.csv`.
- [ ] Solo se mueve a Done si la aceptación se ha producido. Una tarea técnicamente implementada puede permanecer To Review.
- [ ] Si falla un criterio, se registra el fallo y trabajo pendiente, sin declarar cumplida la historia completa.

## Recorridos prioritarios del Sprint 2

- [ ] Coordinador: programar con datos válidos; rechazar rangos, fechas, capacidad o reservas inválidas.
- [ ] Estados: iniciar y entregar; rechazar cancelación de un envío en tránsito o entregado.
- [ ] Cliente de Carga: consultar únicamente sus envíos; rechazar acceso cruzado y comandos de coordinador.
- [ ] Acceso: credenciales correctas/incorrectas, restauración de sesión y revocación tras logout.
- [ ] Alertas: registrar acción válida, rechazar comentario vacío y distinguir atención de recuperación térmica.
- [ ] Historial y exportación: fechas/unidades correctas y periodos sin datos sin afirmar cumplimiento térmico inexistente.
- [ ] Landing: acceso por perfil e idioma, navegación móvil/escritorio y contacto sin confirmación falsa de recepción.
- [ ] Idiomas: contenido y errores disponibles en español e inglés sin claves expuestas.

Los datos simulados se deben identificar como tales. Las pruebas de autorización y el funcionamiento de una SPA no prueban la existencia de sensores físicos o PostgreSQL. Los pendientes de telemetría real y de receptor de contacto no pueden cerrarse solo porque el sitio se haya desplegado.

## Evidencia de colaboración entre productos

- [ ] Enlazar trabajo propio y revisiones reales de cada integrante en los repositorios que correspondan.
- [ ] Relacionar al menos un recorrido integrado landing → SPA → API con tarjetas y versiones verificables.
- [ ] Registrar quién implementó, quién revisó y qué observaciones se resolvieron. Equilibrar commits por sí solo no demuestra integración ni aceptación.
- [ ] Adjuntar un acta de la revisión que efectivamente se realice: fecha, asistentes, versión, demostraciones, decisiones y pendientes. No crear actas retrospectivas de reuniones que no estén registradas.
- [ ] Exportar el tablero actualizado y conservar enlaces de tarjetas y una captura real tomada por el equipo.
- [ ] Incorporar al reporte la fecha de corte y explicar qué se aceptó, qué queda To Review y qué sigue To Do.
