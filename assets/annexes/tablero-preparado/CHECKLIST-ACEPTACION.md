# Criterios de aceptación y evidencia

La revisión de producto identifica versión, tarea, escenario, resultado esperado, resultado observado, evidencia, revisor y fecha. Este documento define criterios; las decisiones de revisión se registran en `registro-aceptacion-58.csv` o en las tarjetas correspondientes.

## Trazabilidad

- Versión y commit del frontend, API y landing.
- Task ID, User Story y escenarios asociados.
- Responsable, revisor y fecha de revisión.
- Evidencias de código, ejecución e integración.
- Decisión y estado de la tarea.

## Recorridos del producto

| Recorrido | Criterios |
| --- | --- |
| Programación | Datos válidos; rechazo de rangos, fechas, capacidad o reservas inválidas. |
| Estados | Inicio y entrega autorizados; restricciones de cancelación. |
| Cliente de Carga | Consulta de envíos asignados; rechazo de acceso cruzado y comandos de coordinador. |
| Acceso | Credenciales, restauración de sesión y revocación tras logout. |
| Alertas | Atención válida y distinción entre reconocimiento y recuperación térmica. |
| Historial y exportación | Fechas, unidades, periodos y procedencia de los datos. |
| Landing | Acceso por perfil e idioma, navegación y contacto. |
| Idiomas | Contenido y errores disponibles en español e inglés. |

## Colaboración entre productos

La evidencia relaciona trabajo propio y revisiones por integrante con los recorridos landing → SPA → API. El registro de revisión vincula tareas, versiones, observaciones y decisiones. El conteo de commits documenta actividad y se interpreta junto con la integración y la aceptación.

Las pruebas técnicas utilizan datos de demostración identificados. La existencia de una SPA y sus pruebas de autorización no acredita por sí sola ingesta de sensores físicos.
