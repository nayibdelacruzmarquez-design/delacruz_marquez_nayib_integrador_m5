# ADR 5.3: Definición de la Frontera Front/Back y Estrategia de Renderizado

* **Contexto:** La arquitectura legada acoplaba las vistas HTML en el backend mediante Jinja2, lo que limitaba la reutilización del código para múltiples clientes y sobrecargaba el servidor con el armado de UI.
* **Alternativas:** 
  1. Mantener Server-Side Rendering (SSR) acoplado en Flask con Jinja2.
  2. Adopción de arquitectura desacoplada: Backend API REST puramente stateless y Frontend SPA/Mobile independiente.
  3. Enfoque híbrido con Server-Driven UI.
* **Criterio de Selección:** Maximizar la eficiencia computacional del backend y permitir el consumo multiplataforma reutilizando los mismos endpoints HTTP.
* **Evidencia Empírica:** Al ejecutar la prueba comparativa (`src/tests/test_spike_5_3.py`), el renderizado de plantillas HTML generó un overhead masivo de CPU frente a la respuesta JSON:

```text
============================================================
EVIDENCIA DE EJECUCIÓN - SPIKE 5.3 (FRONT/BACK BOUNDARY)
TIMESTAMP : 2026-08-08T11:02:12.982668
HOSTNAME  : Nayibdlcm
PLATFORM  : Windows-11-10.0.26200-SP0
============================================================
[+] Tiempo de renderizado SSR (Jinja2 HTML - 500 ops) : 3.9467 s
[+] Tamaño de la respuesta HTML (SSR)                  : 12324 bytes
------------------------------------------------------------
[+] Tiempo de generación API (JSON Payload - 500 ops)   : 0.2250 s
[+] Tamaño del Payload JSON (API)                      : 19719 bytes
------------------------------------------------------------
[=>] Reducción de overhead de CPU en Backend          : 94.30%
[=>] Reducción de ancho de banda por petición         : -60.00%
============================================================
```
* **Decisión:** Desacoplar completamente el frontend y backend, transformando la aplicación Flask en un proveedor exclusivo de API REST stateless.

* **Consecuencias Positivas:** Reducción del 94.30% en el overhead de CPU en backend, menor latencia del servidor y desacoplamiento en el ciclo de despliegue de clientes UI.

* **Consecuencias Negativas / Riesgos:** Mayor complejidad en la gestión de estado e interfaz en el lado del cliente y necesidad de configurar políticas CORS estrictas.