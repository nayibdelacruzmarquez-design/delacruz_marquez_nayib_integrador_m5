# ADR 9: Decisiones Finales de Despliegue, Mantenimiento y Evolución

* **Contexto:** Una vez refactorizada la API REST, validados los benchmarks de rendimiento (5.1 a 5.7) y definida la estrategia de empaquetado, se requiere formalizar la decisión arquitectónica para la distribución, despliegue y mantenimiento continuo de la aplicación en producción.
* **Alternativas:** 
  1. Despliegue tradicional directo en servidor VPS mediante entorno virtual de Python (`.venv`).
  2. Arquitectura distribuida en microservicios sobre orquestadores complejos (Kubernetes).
  3. Contenerización basada en Docker utilizando una imagen ligera (`python:3.12-slim`) en arquitectura monolítica modular stateless.
* **Criterio de Selección:** Garantizar la portabilidad total del entorno, la repetibilidad e idempotencia en la instalación y la facilidad de mantenimiento sin agregar sobreingeniería a la infraestructura.
* **Evidencia Empírica:** La factibilidad del empaquetado fue validada empíricamente en el Spike 5.8 (`src/tests/test_spike_5_8.py`), complementada por el manifiesto `Dockerfile` ubicado en la raíz del proyecto y la ejecución exitosa de la suite completa de pruebas de integración.
* **Decisión:** Adoptar la contenerización con Docker como estándar único para el empaquetado y despliegue de la API REST, apoyada en Flask-Migrate para la gestión de esquema de la base de datos relacional.
* **Consecuencias Positivas:** Eliminación absoluta de discrepancias de entorno ("en mi máquina sí funciona"), simplificación del proceso de integración continua (CI/CD) y aislamiento de dependencias del sistema operativo.
* **Consecuencias Negativas / Riesgos:** Necesidad de gestionar volúmenes persistentes para la base de datos en instancias mono-nodo y requerimiento del motor Docker en la máquina host.