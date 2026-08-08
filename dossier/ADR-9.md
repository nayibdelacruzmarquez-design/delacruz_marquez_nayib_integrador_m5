# ADR 9: Decisiones Finales de Integración, Despliegue y Mantenimiento

* **Contexto:** Tras investigar las 8 decisiones por separado (del 5.1 al 5.8), se requirió integrar todos los componentes en una sola API REST contenerizada para validar si surgían fricciones o incompatibilidades al ejecutarse en conjunto.
* **Alternativas:** 
  1. Reestructurar la arquitectura cambiando el servidor síncrono a asíncrono (ASGI) tras detectar bloqueos en Docker.
  2. Mantener la arquitectura monolítica modular síncrona alineando los límites de los módulos de forma estricta.
* **Criterio de Selección:** Priorizar la cohesión del sistema y la facilidad de mantenimiento sin introducir sobreingeniería tras verificar la compatibilidad entre el ORM, la inyección de dependencias y el contenedor.
* **Evidencia Empírica:** Durante el Spike 5.8 y las pruebas de integración, las 8 decisiones encajaron sin fricción severa debido a que desde el Spike 5.1 se optó por un WSGI síncrono compatible con SQLAlchemy, la serialización JSON pura (5.2 y 5.3) no requirió dependencias pesadas en Docker, y las migraciones de SQLite/Alembic (5.4) se ejecutaron sin bloqueos al usar el patrón Application Factory (5.6).
* **Decisión:** Mantener las 8 decisiones arquitectónicas previas y empaquetar la solución integral mediante Docker apoyado en Flask-Migrate y Pytest.
* **Consecuencias Positivas:** Integración limpia, 0% de conflictos de compatibilidad entre librerías, y portabilidad absoluta del servicio.
* **Consecuencias Negativas / Riesgos:** Se mantiene el riesgo de cuello de botella en I/O si la carga de peticiones concurrentes excede el pool de workers de WSGI.