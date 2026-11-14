# Esquema relacional AV2

Este catálogo se deriva de la migración EF Core del repositorio canónico `friotrack-api`; identifica las fuentes y no acredita por sí solo despliegue cloud ni aceptación del sprint.

Migración: `20261113144845_InitialAv2Relational.cs`. SHA-256: `2872a561f81786cfdb92f68c1f6f15a63849d2869081e433319b2dff053a2a53`.

**18 tablas y 31 claves foráneas.** La tabla interna `__EFMigrationsHistory` registra EF Core y no es una entidad de negocio.

[Documento editable de seis páginas](FrioTrack-AV2-Database.drawio). Descargar y abrir en Archivo → Abrir de [diagrams.net](https://app.diagrams.net/). Las tablas y conectores son formas nativas; las relaciones se muestran como catálogo FK → PK para facilitar la lectura impresa.

| Vista | Imagen | Editable |
| --- | --- | --- |
| Relational schema overview | [SVG](00-erd-overview.svg) | [drawio](00-erd-overview.drawio) |
| Shipment Management | [SVG](01-erd-shipment.svg) | [drawio](01-erd-shipment.drawio) |
| Monitoring and Telemetry | [SVG](02-erd-monitoring.svg) | [drawio](02-erd-monitoring.drawio) |
| Fleet and Resources | [SVG](03-erd-fleet.svg) | [drawio](03-erd-fleet.drawio) |
| Alert and Reporting | [SVG](04-erd-alerts-reporting.svg) | [drawio](04-erd-alerts-reporting.drawio) |
| IAM | [SVG](05-erd-iam.svg) | [drawio](05-erd-iam.drawio) |

## Diferencias respecto al diseño TB1

- `auth_sessions` añade sesiones revocables persistentes. La clave primaria es el hash del token, no el token emitido.
- Los identificadores de entidad usan `varchar(100)`, compatibles con el contrato histórico. Los tipos de cada referencia constan en el catálogo; `thermal_reports.generated_by` usa `varchar(2000)`. No se convierten los identificadores históricos a UUID.
- El campo `version` del envío es un token de concurrencia. La reserva opera en una transacción y utiliza un bloqueo asesor por organización; las FK no impiden por sí solas el solapamiento.
- `thermal_reports.snapshot` utiliza `jsonb`: es la copia autorizada e inmutable del reporte al solicitarlo, no el almacén general de operaciones. La descarga implementada es JSON, además del CSV del frontend.
- Los roles y estados tienen restricciones CHECK. El aislamiento por empresa y por cliente se aplica también en el servicio de aplicación; una FK no sustituye autorización.
- La presencia de `password_reset_tokens` permite conservar el modelo previsto. No demuestra envío de correo ni un flujo de recuperación operativo.
- Las lecturas son de demostración y las evaluaciones de pérdida de señal se solicitan expresamente. No se afirma ingesta física ni evaluación automática en segundo plano.

## Catálogo de columnas

### Shipment Management

#### `shipments`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `organization_id` | `character varying(100)` | FK |
| `coordinator_id` | `character varying(100)` | FK |
| `customer_id` | `character varying(100)` | FK |
| `vehicle_id` | `character varying(100)` | FK |
| `driver_id` | `character varying(100)` | FK |
| `cargo` | `character varying(2000)` | NOT NULL |
| `weight` | `numeric(12,5)` | NOT NULL |
| `origin` | `character varying(2000)` | NOT NULL |
| `destination` | `character varying(2000)` | NOT NULL |
| `departure` | `timestamp with time zone` | NOT NULL |
| `arrival` | `timestamp with time zone` | NOT NULL |
| `status` | `character varying(2000)` | NOT NULL |
| `version` | `bigint` | NOT NULL |
| `min_temp` | `numeric(12,5)` | NOT NULL |
| `max_temp` | `numeric(12,5)` | NOT NULL |
| `min_humidity` | `numeric(12,5)` | NOT NULL |
| `max_humidity` | `numeric(12,5)` | NOT NULL |
| `tolerance_minutes` | `integer` | NOT NULL |

- CHECK `ck_shipment_dates`: `arrival > departure`.
- CHECK `ck_shipment_range`: `min_temp < max_temp AND min_humidity < max_humidity AND min_humidity >= 0 AND max_humidity <= 100 AND tolerance_minutes >= 0`.
- CHECK `ck_shipment_status`: `status IN ('scheduled','in-transit','delivered','cancelled')`.
- CHECK `ck_shipment_weight`: `weight > 0`.
- INDEX `IX_shipments_coordinator_id`: `coordinator_id`.
- INDEX `IX_shipments_customer_id`: `customer_id`.
- INDEX `IX_shipments_driver_id`: `driver_id`.
- INDEX `IX_shipments_organization_id_status`: `organization_id`, `status`.
- INDEX `IX_shipments_vehicle_id`: `vehicle_id`.

#### `shipment_history`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK |
| `actor_id` | `character varying(100)` | FK |
| `action` | `character varying(2000)` | NOT NULL |
| `note` | `character varying(2000)` | NOT NULL |
| `at` | `timestamp with time zone` | NOT NULL |

- INDEX `IX_shipment_history_actor_id`: `actor_id`.
- INDEX `IX_shipment_history_shipment_id`: `shipment_id`.

### Monitoring and Telemetry

#### `shipment_monitorings`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK, UK |
| `min_temp` | `numeric(12,5)` | NOT NULL |
| `max_temp` | `numeric(12,5)` | NOT NULL |
| `min_humidity` | `numeric(12,5)` | NOT NULL |
| `max_humidity` | `numeric(12,5)` | NOT NULL |
| `tolerance_minutes` | `integer` | NOT NULL |
| `max_silence_minutes` | `integer` | NOT NULL |
| `signal_status` | `character varying(2000)` | NOT NULL |
| `started_at` | `timestamp with time zone` | NOT NULL |
| `stopped_at` | `timestamp with time zone` | nullable |
| `last_reading_at` | `timestamp with time zone` | nullable |

- CHECK `ck_monitoring_range`: `min_temp < max_temp AND min_humidity < max_humidity AND min_humidity >= 0 AND max_humidity <= 100`.
- UNIQUE `IX_shipment_monitorings_shipment_id`: `shipment_id`.

#### `sensor_readings`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `monitoring_id` | `character varying(100)` | FK |
| `temperature` | `numeric(12,5)` | NOT NULL |
| `humidity` | `numeric(12,5)` | NOT NULL |
| `at` | `timestamp with time zone` | NOT NULL |
| `within_range` | `boolean` | NOT NULL |
| `is_demonstration` | `boolean` | NOT NULL |

- CHECK `ck_reading_values`: `humidity >= 0 AND humidity <= 100 AND temperature >= -50 AND temperature <= 50`.
- INDEX `IX_sensor_readings_monitoring_id_at`: `monitoring_id`, `at`.

#### `position_reports`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `monitoring_id` | `character varying(100)` | FK |
| `reading_id` | `character varying(100)` | FK, UK |
| `latitude` | `numeric(12,5)` | NOT NULL |
| `longitude` | `numeric(12,5)` | NOT NULL |
| `at` | `timestamp with time zone` | NOT NULL |

- CHECK `ck_position_coordinates`: `latitude >= -90 AND latitude <= 90 AND longitude >= -180 AND longitude <= 180`.
- INDEX `IX_position_reports_monitoring_id`: `monitoring_id`.
- UNIQUE `IX_position_reports_reading_id`: `reading_id`.

### Fleet and Resources

#### `vehicles`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `organization_id` | `character varying(100)` | FK |
| `plate` | `character varying(2000)` | UK |
| `capacity` | `numeric(12,5)` | NOT NULL |
| `enabled` | `boolean` | NOT NULL |

- CHECK `ck_vehicle_capacity`: `capacity > 0 AND capacity <= 100`.
- INDEX `IX_vehicles_organization_id`: `organization_id`.
- UNIQUE `IX_vehicles_plate`: `plate`.

#### `drivers`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `organization_id` | `character varying(100)` | FK |
| `name` | `character varying(2000)` | NOT NULL |
| `license` | `character varying(2000)` | UK |
| `enabled` | `boolean` | NOT NULL |

- UNIQUE `IX_drivers_license`: `license`.
- INDEX `IX_drivers_organization_id`: `organization_id`.

#### `sensors`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `organization_id` | `character varying(100)` | FK |
| `serial_code` | `character varying(2000)` | UK |
| `vehicle_id` | `character varying(100)` | FK, UK, nullable |
| `enabled` | `boolean` | NOT NULL |

- INDEX `IX_sensors_organization_id`: `organization_id`.
- UNIQUE `IX_sensors_serial_code`: `serial_code`.
- UNIQUE `IX_sensors_vehicle_id`: `vehicle_id`.

#### `fleet_allocations`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK, UK |
| `vehicle_id` | `character varying(100)` | FK |
| `driver_id` | `character varying(100)` | FK |
| `from` | `timestamp with time zone` | NOT NULL |
| `until` | `timestamp with time zone` | NOT NULL |
| `status` | `character varying(2000)` | NOT NULL |
| `released_at` | `timestamp with time zone` | nullable |

- CHECK `ck_allocation_interval`: `until > "from"`.
- INDEX `IX_fleet_allocations_driver_id_from_until`: `driver_id`, `from`, `until`.
- UNIQUE `IX_fleet_allocations_shipment_id`: `shipment_id`.
- INDEX `IX_fleet_allocations_vehicle_id_from_until`: `vehicle_id`, `from`, `until`.

### Alert and Reporting

#### `alerts`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK |
| `type` | `character varying(2000)` | NOT NULL |
| `reading` | `numeric(12,5)` | nullable |
| `trigger_reading_id` | `character varying(100)` | FK, nullable |
| `at` | `timestamp with time zone` | NOT NULL |
| `last_deviation_at` | `timestamp with time zone` | NOT NULL |
| `severity` | `character varying(2000)` | NOT NULL |
| `status` | `character varying(2000)` | NOT NULL |
| `resolved_at` | `timestamp with time zone` | nullable |
| `recovery_reading_id` | `character varying(100)` | nullable |

- CHECK `ck_alert_status`: `status IN ('active','acknowledged','resolved')`.
- INDEX `IX_alerts_shipment_id_status`: `shipment_id`, `status`.
- INDEX `IX_alerts_trigger_reading_id`: `trigger_reading_id`.

#### `corrective_actions`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `alert_id` | `character varying(100)` | FK |
| `actor_id` | `character varying(100)` | FK |
| `note` | `character varying(2000)` | NOT NULL |
| `notify_client` | `boolean` | NOT NULL |
| `at` | `timestamp with time zone` | NOT NULL |

- INDEX `IX_corrective_actions_actor_id`: `actor_id`.
- INDEX `IX_corrective_actions_alert_id`: `alert_id`.

#### `notifications`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK |
| `recipient_id` | `character varying(100)` | FK |
| `type` | `character varying(2000)` | NOT NULL |
| `at` | `timestamp with time zone` | NOT NULL |
| `read_at` | `timestamp with time zone` | nullable |

- INDEX `IX_notifications_recipient_id_read_at`: `recipient_id`, `read_at`.
- INDEX `IX_notifications_shipment_id`: `shipment_id`.

#### `incidents`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK |
| `actor_id` | `character varying(100)` | FK |
| `note` | `character varying(2000)` | NOT NULL |
| `at` | `timestamp with time zone` | NOT NULL |

- INDEX `IX_incidents_actor_id`: `actor_id`.
- INDEX `IX_incidents_shipment_id`: `shipment_id`.

#### `thermal_reports`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `shipment_id` | `character varying(100)` | FK |
| `generated_by` | `character varying(2000)` | FK |
| `at` | `timestamp with time zone` | NOT NULL |
| `snapshot` | `jsonb` | NOT NULL |

- INDEX `IX_thermal_reports_generated_by`: `generated_by`.
- INDEX `IX_thermal_reports_shipment_id`: `shipment_id`.

### IAM

#### `organizations`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `name` | `character varying(2000)` | NOT NULL |


#### `users`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `organization_id` | `character varying(100)` | FK |
| `name` | `character varying(2000)` | NOT NULL |
| `email` | `character varying(2000)` | UK |
| `company_name` | `character varying(2000)` | NOT NULL |
| `role` | `character varying(2000)` | NOT NULL |
| `language` | `character varying(2000)` | NOT NULL |
| `password_hash` | `character varying(2000)` | NOT NULL |
| `password_salt` | `character varying(2000)` | NOT NULL |
| `enabled` | `boolean` | NOT NULL |

- CHECK `ck_user_role`: `role IN ('coordinator','cargo-client')`.
- UNIQUE `IX_users_email`: `email`.
- INDEX `IX_users_organization_id`: `organization_id`.

#### `auth_sessions`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `token_hash` | `character varying(100)` | PK |
| `user_id` | `character varying(100)` | FK |
| `expires_at` | `timestamp with time zone` | NOT NULL |

- INDEX `IX_auth_sessions_expires_at`: `expires_at`.
- INDEX `IX_auth_sessions_user_id`: `user_id`.

#### `password_reset_tokens`

| Columna | Tipo PostgreSQL | Restricciones |
| --- | --- | --- |
| `id` | `character varying(100)` | PK |
| `user_id` | `character varying(100)` | FK |
| `token_hash` | `character varying(100)` | UK |
| `expires_at` | `timestamp with time zone` | NOT NULL |
| `used_at` | `timestamp with time zone` | nullable |

- UNIQUE `IX_password_reset_tokens_token_hash`: `token_hash`.
- INDEX `IX_password_reset_tokens_user_id`: `user_id`.

## Referencias de integridad

| Hija | FK | Padre | PK | Eliminación |
| --- | --- | --- | --- | --- |
| `shipments` | `driver_id` | `drivers` | `id` | Restrict |
| `shipments` | `organization_id` | `organizations` | `id` | Restrict |
| `shipments` | `coordinator_id` | `users` | `id` | Restrict |
| `shipments` | `customer_id` | `users` | `id` | Restrict |
| `shipments` | `vehicle_id` | `vehicles` | `id` | Restrict |
| `shipment_history` | `shipment_id` | `shipments` | `id` | Cascade |
| `shipment_history` | `actor_id` | `users` | `id` | Restrict |
| `shipment_monitorings` | `shipment_id` | `shipments` | `id` | Cascade |
| `sensor_readings` | `monitoring_id` | `shipment_monitorings` | `id` | Cascade |
| `position_reports` | `reading_id` | `sensor_readings` | `id` | Cascade |
| `position_reports` | `monitoring_id` | `shipment_monitorings` | `id` | Cascade |
| `vehicles` | `organization_id` | `organizations` | `id` | Restrict |
| `drivers` | `organization_id` | `organizations` | `id` | Restrict |
| `sensors` | `organization_id` | `organizations` | `id` | Restrict |
| `sensors` | `vehicle_id` | `vehicles` | `id` | Restrict |
| `fleet_allocations` | `driver_id` | `drivers` | `id` | Restrict |
| `fleet_allocations` | `shipment_id` | `shipments` | `id` | Cascade |
| `fleet_allocations` | `vehicle_id` | `vehicles` | `id` | Restrict |
| `alerts` | `trigger_reading_id` | `sensor_readings` | `id` | Restrict |
| `alerts` | `shipment_id` | `shipments` | `id` | Cascade |
| `corrective_actions` | `alert_id` | `alerts` | `id` | Cascade |
| `corrective_actions` | `actor_id` | `users` | `id` | Restrict |
| `notifications` | `shipment_id` | `shipments` | `id` | Cascade |
| `notifications` | `recipient_id` | `users` | `id` | Restrict |
| `incidents` | `shipment_id` | `shipments` | `id` | Cascade |
| `incidents` | `actor_id` | `users` | `id` | Restrict |
| `thermal_reports` | `shipment_id` | `shipments` | `id` | Cascade |
| `thermal_reports` | `generated_by` | `users` | `id` | Restrict |
| `users` | `organization_id` | `organizations` | `id` | Restrict |
| `auth_sessions` | `user_id` | `users` | `id` | Cascade |
| `password_reset_tokens` | `user_id` | `users` | `id` | Cascade |

## Reproducción

Con ambos repositorios en directorios hermanos, ejecutar `python scripts/build-av2-schema.py`. Puede indicarse otra ruta con `--migration`. El script solo lee la migración y escribe documentación; no inicia servicios, crea bases de datos ni accede a credenciales.
