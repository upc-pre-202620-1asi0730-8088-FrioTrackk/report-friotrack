# 5.3.1. Diseño de entrevistas de validación

## Propósito y participantes

Validar si las personas de los segmentos objetivo comprenden la propuesta de FríoTrack y completan los recorridos disponibles de la versión AV2. El enunciado pide **3–5 entrevistas por segmento**; con Coordinador Logístico y Cliente de Carga se preparan **6–10 entrevistas**. Se recomienda reclutar participantes distintos por segmento y comprobar que su experiencia corresponde a transporte refrigerado o gestión/contratación de carga.

Estas sesiones requieren interacción con landing y aplicación. Las entrevistas anteriores de investigación sobre problemas no se presentan como validación del producto. Si una persona participó antes, su nueva sesión debe registrar las nuevas tareas y la versión evaluada.

## Antes de la sesión

1. Identificar commit/versiones de landing, SPA y API y el entorno que se evaluará. Usar una versión estable y cuentas de prueba con datos ficticios.
2. Obtener autorización para grabar y para utilizar fragmentos identificados en el reporte y videos del proyecto. Acordar qué información podrá publicarse y evitar contraseñas, datos de clientes reales o información comercial privada en pantalla.
3. Registrar nombres, apellidos, edad, distrito, segmento y fecha. Usar un ID de sesión en los archivos de trabajo y respetar las condiciones de publicación acordadas.
4. Comprobar audio, cámara y captura de la aplicación. No grabar un escritorio personal con información ajena a la sesión.
5. Explicar que se evalúa el producto, no la capacidad de la persona. No dirigirla hacia respuestas positivas ni completar las tareas por ella.

## Introducción sugerida del moderador

“Gracias por participar. Queremos observar cómo utilizarías FríoTrack para tu trabajo. Te pediré realizar algunas tareas y comentar qué esperas que ocurra y qué encuentras. Si algo resulta confuso, ese comentario nos ayuda a mejorar. Los datos y operaciones que usaremos son de demostración.”

## Tareas del Coordinador Logístico

| ID | Instrucción para el participante | Qué observar | Criterio de referencia |
| --- | --- | --- | --- |
| C1 | Revisa la landing y explica con tus palabras qué ofrece FríoTrack y para quién. | Comprensión de propuesta, límites y acceso. | Identifica transporte refrigerado y el perfil que necesita. |
| C2 | Accede con la cuenta de prueba y localiza un envío indicado. | Terminología, búsqueda, orientación y fecha de datos. | Encuentra el envío y distingue lecturas de demostración/antiguas. |
| C3 | Programa un envío con el cliente, carga, ruta, fechas, rangos y recursos entregados en la ficha de prueba. | Comprensión de campos, validación y confirmación. | Registro completo y recursos reservados sin cambios parciales. |
| C4 | Intenta una reserva que se solape con la anterior y explica el resultado. | Claridad del rechazo y recuperación del error. | Se informa indisponibilidad y no se duplica la reserva. |
| C5 | Consulta una alerta y registra una acción correctiva sobre el envío de demostración. | Diferencia entre atención y resolución, visibilidad del historial. | Atención registrada sin cerrar falsamente la excursión. |
| C6 | Consulta historial/reporte disponible y explica qué evidencia contiene; luego cierra sesión. | Fechas, unidades, procedencia y salida segura. | Reconoce la evidencia disponible y la sesión queda revocada. |

## Tareas del Cliente de Carga

| ID | Instrucción para el participante | Qué observar | Criterio de referencia |
| --- | --- | --- | --- |
| L1 | Revisa la landing y localiza el acceso que utilizarías como cliente. | Comprensión del perfil y continuidad entre productos. | Llega al acceso de cliente conservando idioma. |
| L2 | Inicia sesión con la cuenta de prueba y encuentra el envío indicado. | Orientación y comprensión del listado. | Consulta únicamente envíos asignados. |
| L3 | Revisa la condición ambiental y ubicación disponible de tu envío. | Fecha de lectura, unidades y comprensión de los datos. | Distingue medición disponible de dato ausente o simulado. |
| L4 | Localiza una notificación, explica qué significa y márcala como leída si esa función está implementada. | Contenido, visibilidad y cambio de estado. | El destinatario comprende el aviso y registra lectura explícita. |
| L5 | Consulta o descarga el historial/reporte habilitado y cierra sesión. | Utilidad percibida, comprensión y permisos. | Obtiene evidencia permitida y termina su sesión. |

Confirmar las tareas contra la versión final del incremento antes de entrevistar. No pedir funciones no implementadas como si estuvieran disponibles; una limitación se registra y se decide si queda fuera del alcance o constituye un defecto del compromiso AV2.

## Preguntas de cierre

- ¿Qué fue más fácil y qué resultó más confuso?
- ¿Hubo algún término, mensaje o dato que no comprendiste?
- ¿Qué información necesitabas y no pudiste encontrar?
- ¿Qué haría falta para utilizarlo en tu trabajo? ¿Por qué?
- ¿Qué beneficio observaste, si alguno? ¿Autorizarías utilizar un fragmento de esta opinión en el video del producto?

Las opiniones deben conservar su sentido, incluidas las críticas. About-the-Product necesita una opinión de cada segmento y al menos un testimonio positivo auténtico de validación; no se solicita a una persona que invente una valoración.

## Registro y análisis

Completar [validation-records.csv](validation-records.csv) con datos reales. Por tarea registrar resultado observado, errores, ayuda necesaria y comentarios; tiempo y cantidad de intentos son métricas recomendadas, no resultados presupuestos. Relacionar los hallazgos con [heuristics-template.md](heuristics-template.md), priorizar y comprobar las correcciones.

Consolidar las entrevistas en un MP4 con títulos de participante, segmento y fecha; el Anexo C orienta edición de 3–5 minutos por entrevista. Publicar en Stream privado con permiso para el docente. Incorporar por entrevista un cuadro representativo, enlace, inicio y duración y resumen descriptivo. No confundir duración editada con tiempo total de la sesión.
