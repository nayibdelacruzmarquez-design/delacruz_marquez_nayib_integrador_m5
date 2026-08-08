# ADR 5.3: Definición de la Frontera Front/Back y Estrategia de Renderizado

* **Contexto:** La arquitectura legada acoplaba las vistas HTML en el backend mediante Jinja2, lo que limitaba la reutilización del código para múltiples clientes y sobrecargaba el servidor con el armado de UI.
* **Alternativas:** 
  1. Mantener Server-Side Rendering (SSR) acoplado en Flask con Jinja2.
  2. Adopción de arquitectura desacoplada: Backend API REST puramente stateless y Frontend SPA/Mobile independiente.
  3. Enfoque híbrido con Server-Driven UI.
* **Criterio de Selección:** Maximizar la eficiencia computacional del backend y permitir el consumo multiplataforma reutilizando los mismos endpoints HTTP.
* **Evidencia Empírica:** Al ejecutar la prueba comparativa (`src/tests/test_spike_5_3.py`), el renderizado de plantillas HTML generó una carga adicional de CPU frente a la respuesta JSON, reduciendo además el tamaño del payload transmitido por la red al omitir etiquetas de marcado UI.
* **Decisión:** Desacoplar completamente el frontend y backend, transformando la aplicación Flask en un proveedor exclusivo de API REST stateless.
* **Consecuencias Positivas:** Reducción de la latencia del servidor, menor consumo de ancho de banda por solicitud y desacoplamiento en el ciclo de despliegue de clientes UI.
* **Consecuencias Negativas / Riesgos:** Mayor complejidad en la gestión de estado e interfaz en el lado del cliente y necesidad de configurar políticas CORS estrictas.