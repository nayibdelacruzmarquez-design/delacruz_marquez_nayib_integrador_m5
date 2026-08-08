# ADR 5.8: Estrategia de Contenerización y Empaquetado para Despliegue

* **Contexto:** La ejecución directa en entornos locales genera inconsistencias de dependencias, versiones de Python y librerías del sistema entre las máquinas de desarrollo y evaluación.
* **Alternativas:** 
  1. Despliegue ejecutable directo mediante entornos virtuales locales (`.venv`).
  2. Uso de máquinas virtuales completas (Vagrant / VirtualBox).
  3. Contenerización liviana de la aplicación utilizando Docker y la imagen base `python:3.12-slim`.
* **Criterio de Selección:** Asegurar la reproductibilidad idéntica del entorno de ejecución con un consumo mínimo de recursos e imágenes livianas.
* **Evidencia Empírica:** La prueba de simulación (`src/tests/test_spike_5_8.py`) verificó las variables de entorno necesarias para un despliegue contenerizado estandarizado sin variables faltantes.
* **Decisión:** Empaquetar la aplicación Flask mediante un `Dockerfile` optimizado multicapa con servidor WSGI Gunicorn/Waitress.
* **Consecuencias Positivas:** Garantía total de portabilidad en cualquier sistema operativo que soporte Docker, eliminando discrepancias de dependencias.
* **Consecuencias Negativas / Riesgos:** Ligero incremento en la curva de aprendizaje y la necesidad de tener la herramienta Docker Desktop / Engine instalada.