# ADR 5.2: Selección del Formato de Serialización y Protocolo de API

* **Contexto:** La arquitectura anterior devolvía únicamente vistas HTML renderizadas por el servidor, impidiendo la integración con clientes móviles o servicios de terceros.
* **Alternativas:** 
  1. Mantener Server-Side Rendering (SSR) con plantillas HTML (Jinja2).
  2. Implementar una API RESTful exponiendo cargas útiles en formato JSON con esquemas estrictos.
  3. Adoptar Protocol Buffers / gRPC para comunicación binaria.
* **Criterio de Selección:** Priorizar la interoperabilidad con clientes externos, la velocidad de parseo en frontend y la facilidad de pruebas automatizadas.
* **Evidencia Empírica:** La prueba de serialización (`src/tests/test_spike_5_2.py`) confirmó la velocidad y ligereza de las respuestas JSON según el siguiente registro:

```text
============================================================
EVIDENCIA DE EJECUCIÓN - SPIKE 5.2 (SERIALIZACIÓN API)
TIMESTAMP : 2026-08-08T10:54:53.991356
HOSTNAME  : Nayibdlcm
PLATFORM  : Windows-11-10.0.26200-SP0
============================================================
[+] Serialización JSON (1,000 iteraciones): 0.1850 s
[+] Tamaño de carga útil JSON: 8214 bytes
------------------------------------------------------------
```
* **Decisión:** Adoptar una arquitectura de API REST utilizando JSON como formato estándar de intercambio de datos y códigos de estado HTTP semánticos.

* **Consecuencias Positivas:** Desacoplamiento total entre el backend de lógica de negocio y cualquier cliente consumidor (Web/Mobile/API clients).

* **Consecuencias Negativas / Riesgos:** Manejo explícito de serializadores/esquemas para evitar exponer información confidencial del modelo de dominio.