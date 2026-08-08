# ADR 5.4: Selección de la Estrategia de Migración de Base de Datos

* **Contexto:** La base de datos requiere evolucionar su esquema para soportar nuevas funcionalidades de la API sin perder los datos de producción generados en el Módulo 4.
* **Alternativas:** 
  1. Recreación destructiva de tablas (`db.drop_all()` / `db.create_all()`).
  2. Scripts SQL manuales ejecutados en el servidor de base de datos.
  3. Control de versiones de esquema automatizado con Alembic / Flask-Migrate.
* **Criterio de Selección:** Garantizar la trazabilidad, reversibilidad (rollbacks) e integridad de datos en el proceso de actualización del esquema.
* **Evidencia Empírica:** La simulación de evolución de esquema (`src/tests/test_spike_5_4.py`) confirmó la preservación del 100% de los registros existentes al aplicar modificaciones de columnas con valores predeterminados de fábrica.
* **Decisión:** Integrar Flask-Migrate (Alembic) para gestionar la evolución del esquema relacional mediante scripts de migración versionados.
* **Consecuencias Positivas:** Capacidad de desplegar cambios estructurales de forma automatizada y segura en cualquier entorno, manteniendo el historial de versiones en Git.
* **Consecuencias Negativas / Riesgos:** Requiere disciplina para generar revisiones antes de cada cambio en los modelos y atención especial en migraciones destructivas de tipo `DROP COLUMN`.