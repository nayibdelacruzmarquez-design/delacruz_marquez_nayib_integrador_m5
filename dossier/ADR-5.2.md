# ADR 5.2: Selección del Formato de Serialización y Protocolo de API

* **Contexto:** La arquitectura anterior devolvía únicamente vistas HTML renderizadas por el servidor, impidiendo la integración con clientes móviles o servicios de terceros.
* **Alternativas:** 
  1. Mantener Server-Side Rendering (SSR) con plantillas HTML (Jinja2).
  2. Implementar una API RESTful exponiendo cargas útiles en formato JSON con esquemas estrictos.
  3. Adoptar Protocol Buffers / gRPC para comunicación binaria.
* **Criterio de Selección:** Priorizar la interoperabilidad con clientes externos, la velocidad de parseo en frontend y la facilidad de pruebas automatizadas.
* **Evidencia Empírica:** La prueba de serialización (`src/tests/test_spike_5_2.py`) demostró una baja latencia en el empaquetado de estructuras de datos a JSON y un consumo reducido de ancho de banda por payload en comparación con respuestas HTML completas.
* **Decisión:** Adoptar una arquitectura de API REST utilizando JSON como formato estándar de intercambio de datos y códigos de estado HTTP semánticos.
* **Consecuencias Positivas:** Desacoplamiento total entre el backend de lógica de negocio y cualquier cliente consumidor (Web/Mobile/API clients).
* **Consecuencias Negativas / Riesgos:** Necesidad de definir esquemas de validación estrictos y manejo explícito de errores en formato JSON.