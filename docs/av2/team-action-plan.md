# AV2: trabajo individual, trabajo del equipo y accesos

Fecha de revisión: 13/11/2026. Se consideran los cuatro integrantes activos registrados en el informe. El reparto siguiente es una **propuesta para acordar en el planning**, no un acta, una asignación aceptada ni evidencia de trabajo realizado.

El enunciado exige una nueva landing y Web App desplegadas, la primera versión de Web Services desplegada, Sprint 3, validación, videos y entregables. La API debe utilizar ASP.NET Core/C#, EF Core, REST, MySQL o PostgreSQL y OpenAPI vía Swagger. PostgreSQL es válido. Las guías Learning Center son ejemplos de implementación: no obligan por sí mismas a cambiar a MySQL, JWT, BCrypt, Controllers, CQRS o Scalar. La indicación `--private` del ejemplo no debe aplicarse: la observación del profesor exige repositorios públicos.

## Lo que debe hacer cada integrante

1. Participar en el planning, revisión y retrospectiva reales, y confirmar su capacidad, tareas y estados del tablero.
2. Realizar aportes verificables de propuestas, implementación, pruebas y despliegue en los productos correspondientes al sprint. Usar su propia cuenta y autor de Git; conservar commits, pruebas, revisiones y resultados que pueda explicar. No fijar un número artificial de commits ni usar cambios vacíos.
3. Preparar su testimonio ante cámara de aproximadamente un minuto para About-the-Team: nombre, actividad real, resultado comprobable y competencia desarrollada.
4. Participar ante cámara en la exposición del equipo, de máximo 30 minutos en total. Como reparto posible: seis minutos por persona y cuatro para introducción/cierre, 28 minutos.
5. Entregar al Team Leader el detalle de responsabilidades y contribuciones reales para el Performance Report. La calificación la determina el Team Leader con la escala del formato, no el conteo de commits.
6. Poder explicar un recorrido completo de su aporte y un caso de error: vista Vue → gateway HTTP → API → dominio → EF Core → PostgreSQL → respuesta. La SPA no accede directamente a la base.

### Reparto equilibrado de las entrevistas

El requisito es **3–5 entrevistas por segmento para todo el equipo**. Con Coordinador Logístico y Cliente de Carga son **6–10 entrevistas en total**; no son 6–10 por alumno. Reparto sugerido: cada integrante realiza una de cada segmento, con ocho participantes distintos en total (cuatro por segmento). Reclutar personas que correspondan a los perfiles; no sustituir validación por una actuación del equipo.

Para cada sesión: consentimiento, versión evaluada, tareas sobre landing y aplicación, grabación de interacción y comentarios espontáneos. Registrar nombres, apellidos, edad, distrito, segmento, fecha, screenshot, URL de Stream, inicio/duración y resumen descriptivo. Editar 3–5 minutos por entrevista para el video consolidado. El límite de 30 minutos de la exposición no se aplica al video consolidado de entrevistas.

## Propuesta por persona

Todos conservan las obligaciones anteriores. Los liderazgos propuestos no excluyen colaboración en los otros productos.

| Integrante | Responsabilidad principal propuesta | Material personal para entregar | Revisión técnica que debe poder mostrar |
| --- | --- | --- | --- |
| Alexander Sebastián Atauje Barreto | Coordinar base de datos, integración y publicación; custodiar la conexión del alojamiento si el equipo lo acuerda. | Una entrevista por segmento, testimonio, parte de exposición y evidencias de sus aportes. Iniciar sesión en Neon y Azure si será titular. | Configuración privada, migración, reservas/transacciones, API, Swagger y verificación después de publicar. |
| Rodrigo Andree Saavedra Flores | Coordinar recorridos de la SPA y el video de navegación Sprint 3. | Una entrevista por segmento, testimonio, parte de exposición y grabación del recorrido funcional. | Coordinador/cliente, sensores, estados, errores, sesiones, ES/EN y vistas móviles. |
| Joaquín Leonardo Daga Chávez | Coordinar reclutamiento, registro y consolidación del material de validación y del video de producto. | Una entrevista por segmento, testimonio, parte de exposición y fichas con datos/timing. | Tareas del protocolo, evidencia por entrevista y relación entre observaciones y mejoras reales. |
| Nayely Macarena Vera Solsol | Coordinar evaluación heurística, trazabilidad de tareas y consolidación de reporte/presentación. | Una entrevista por segmento, testimonio, parte de exposición y hallazgos/actualizaciones verificables. | Anexo D, severidad, historias/escenarios, estados del tablero, conclusiones y Student Outcome. |

Elegir explícitamente quién será Team Leader. No se presume ese cargo por ser titular de GitHub o de la base.

## Videos del equipo

| Entregable | Cantidad y duración | Qué deben grabar ustedes | Publicación y documentación |
| --- | --- | --- | --- |
| Validación Sprint 3 | Un MP4 consolidado; 3–5 min editados por entrevista; propuesta de ocho sesiones: 24–40 min. | Participantes de ambos segmentos usando landing y aplicación. | Stream; registro individual, capturas, inicio/duración, resumen y evaluación heurística en 5.3. |
| About-the-Product | Un video de 1–3 min. | Modelo, funciones/beneficios, interacción real y al menos una opinión auténtica de cada segmento. Seleccionar testimonios del material real. | Stream y YouTube; captura/enlaces en 5.4 e incrustación en landing. |
| About-the-Team | Un video; pauta de unos cinco minutos de retrospectiva más un minuto por integrante (unos nueve minutos con cuatro miembros, ajustando transiciones). | Escenas de trabajo real, narración del proceso y los cuatro testimonios ante cámara. | Stream y YouTube; resumen, pauta con tiempos y captura/enlaces en conclusiones e incrustación en landing. |
| Navegación Sprint 3 | Un video que ilustre y explique las vistas y recorridos implementados; no se inventa un mínimo de minutos no indicado. | Recorrido en una versión identificada: coordinador y cliente, errores, ES/EN y móvil; usar datos de demostración. | Stream; introducción, captura/enlace en 5.2.3.5. |
| Exposición AV2 | Un video del equipo, máximo 30 min. | Todos ante cámara; explicación propia, demostración y resultados, siguiendo la presentación. | Stream y MP4 según los archivos de entrega; verificar acceso del docente. |

Los guiones están en [video-scripts.md](video-scripts.md). Usar el prefijo `upc-pre-202620-1asi0730-8088-blackstartup-` y los nombres finales indicados en [inputs-and-delivery.md](inputs-and-delivery.md). Los videos Product y Team pueden publicarse desde una cuenta acordada; cada integrante no necesita un canal independiente.

## Cuentas y decisiones necesarias para publicar

| Cuenta o decisión | Quién la realiza | Qué hace falta | Qué puede completarse después de conectar |
| --- | --- | --- | --- |
| GitHub | Cada integrante con su cuenta. | Membresía/permisos en la organización y nombre/correo Git correctos. | Trabajar en repositorios públicos, revisar aportes y publicar commits/releases. La cuenta de Alexander ya funciona para los cambios autorizados. |
| Neon Free, propuesta de alojamiento PostgreSQL | Un titular acordado por el equipo; los demás pueden colaborar según permisos. | Crear/iniciar sesión y vincular el complemento Neon. Confirmar plan Free y proyecto del equipo. No necesitan cuatro bases ni enviar contraseñas por chat. | Crear un proyecto PostgreSQL compatible, aplicar las 18 tablas mediante la migración EF y comprobar conectividad/persistencia. Aún no existe una base cloud confirmada. |
| Azure | Titular o miembro con acceso a los recursos existentes. | Iniciar sesión/autorizar la conexión para configurar y publicar. GitHub no concede permisos de Azure. | Configurar la conexión privada del servidor, publicar primero la API y después la SPA, comprobar permisos/Swagger y guardar recibos. |
| Datos iniciales | Decisión del equipo. | Acordar una base nueva de demostración o una migración revisada de datos/cuentas existentes. | Preparar cuentas y datos sin sustituir silenciosamente el almacén anterior. |
| Trello | Miembro con permiso de edición del tablero. | URL del tablero, conexión del complemento si se desea edición asistida, y confirmación de tareas/estados reales. | Actualizar tarjetas sin duplicar, obtener captura actual y reflejarla en la tabla del reporte. |
| Microsoft Stream / cuenta universitaria | Uno o más titulares de las grabaciones. | Subir videos y configurar enlaces que el docente pueda abrir. | Integrar URLs, capturas, tiempos y descripciones en el reporte. |
| YouTube | Un titular/canal acordado. | Publicar Product y Team con enlaces reproducibles e incrustación habilitada. | Configurar las dos URLs reales en la landing; los reproductores actuales permanecen ocultos sin ellas. |

La base se aloja en internet; no exige mantener encendida la PC. Neon Free puede suspender cómputo por inactividad y reactivarlo con consultas; también aplica límites de uso. La API tiene su propio alojamiento y condiciones. Confirmar el plan antes de la exposición y comprobar el recorrido completo, sin confundir código publicado con aplicación desplegada.

Propuesta de proveedor revisada el 13/11/2026: [Neon Free](https://neon.com/pricing), [Npgsql/.NET](https://neon.com/docs/guides/dotnet-npgsql), [suspensión por inactividad](https://neon.com/docs/introduction/scale-to-zero). No se ha contratado un plan de pago.

## Reparto de lo que puede prepararse y lo que requiere al equipo

| Actividad | Preparación técnica/documental posible | Intervención humana necesaria |
| --- | --- | --- |
| Backend, SPA, landing y pruebas | Implementar, revisar y corregir código; ejecutar pruebas; publicar commits/releases con la identidad autorizada. | Comprender el código, aportar/revisar en la propia cuenta y demostrar competencias. |
| Base y despliegue | Configurar proyecto conectado, tablas, migración, conexión, artefactos y verificación pública. | Crear/vincular cuentas, confirmar destino/plan y decidir tratamiento de datos existentes. |
| Reporte y diagramas | Mantener Markdown, C4/DDD/ERD, evidencias técnicas, tablas, exportación y enlaces. | Proporcionar actas, capacidad, responsables, aceptación, datos de entrevistas y decisiones reales. |
| Validación y heurísticas | Preparar protocolo, fichas y formato; analizar grabaciones y problemas observados. | Reclutar personas, obtener consentimiento, realizar y grabar sesiones auténticas. |
| Videos | Preparar guiones; ayudar a ordenar/editar material recibido e integrar enlaces. | Grabar voces, cámara, opiniones de usuarios y trabajo real; iniciar sesión para subir/publicar cuando corresponda. |
| Presentación y performance | Preparar una base editable y plantilla de evaluación. | Completar resultados, fotos autorizadas, exposición propia y evaluación del Team Leader. |

## Orden de ejecución

1. Acordar integrantes/Team Leader, reparto, capacidad, fechas y Sprint Goal; actualizar el tablero real.
2. Vincular Neon y Azure; decidir datos iniciales; preparar PostgreSQL y publicar API/Swagger antes que la SPA.
3. Comprobar una versión estable de landing, SPA y API, identificar sus commits y guardar evidencias.
4. Realizar las ocho entrevistas propuestas (o 6–10 cumpliendo 3–5 por segmento). Evaluar heurísticas y priorizar mejoras.
5. Corregir los hallazgos seleccionados, probar de nuevo y registrar aceptación del equipo.
6. Grabar/consolidar Product, Team, navegación y exposición; publicar los enlaces y completar el reporte.
7. Terminar PPTX/PDF y Performance Word/PDF; revisar archivos complementarios ZIP, enlaces y acceso del docente.

## Cierre del reporte y entrega

- Registro de versiones, Collaboration Insights y Student Outcome actualizados con aportes reales.
- Sprint 3 con sus ocho subsecciones: planning; LACX; backlog con screenshot/URL público y tabla; commits; ejecución/video; documentación de endpoints/Swagger y capturas; despliegue; colaboración por producto.
- Tareas de 4–8 horas, responsables y estados To Do / In Process / To Review / Done conforme al tablero real; varias situaciones Given/When/Then por historia.
- 5.3 con diseño, registro y heurísticas del Anexo D; 5.4 y conclusiones con los dos videos y su pauta/enlaces.
- Repositorios públicos, releases trazables y nuevas versiones realmente desplegadas; inglés por defecto, ES/EN y revisión de accesibilidad.
- Reporte Markdown/PDF, keynote PPTX/PDF, performance DOCX/PDF elaborado por Team Leader y ZIP con complementos según corresponda, sin credenciales ni bases privadas.
- Carátula revisada por el equipo en el formato de entrega y todos los enlaces comprobados como los abrirá el docente.

La base de código 0.2.0 y sus pruebas ya están publicadas. La landing 0.2.0 está en GitHub Pages; API/SPA AV2 cloud, cuenta PostgreSQL conectada, tablero, sesiones de validación y grabaciones siguen pendientes. Consultar el [registro técnico](../../assets/evidence/av2/technical-verification.json) y el [informe](../../README.md#523-sprint-3--preparación-av2) para distinguir evidencia existente de preparación.
