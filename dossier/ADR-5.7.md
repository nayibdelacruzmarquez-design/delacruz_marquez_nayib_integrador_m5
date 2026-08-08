# ADR 5.7: Estrategia de Pruebas Automatizadas y Resiliencia ante Fallos

* **Contexto:** Las pruebas manuales en el Módulo 4 resultaban lentas y propensas a omitir errores de regresión al realizar cambios en las rutas de la API o modelos.
* **Alternativas:** 
  1. Pruebas manuales orientadas a cliente mediante Postman o navegador.
  2. Pruebas unitarias básicas de componentes aislados sin evaluar integración.
  3. Suite automatizada de pruebas de integración con Pytest e inyección de fallos explícitos.
* **Criterio de Selección:** Maximizar la cobertura de código y garantizar que los controladores HTTP respondan con códigos de estado adecuados (4xx y 5xx) ante datos corruptos.
* **Evidencia Empírica:** La prueba de inyección (`src/tests/test_spike_5_7.py`) validó la captura exitosa de 5 vectores de error simulados (JSON malformados, tipos inválidos, 404, restricciones UNIQUE y timeouts).
* **Decisión:** Implementar Pytest como framework estandarizado de pruebas ejecutando suites de integración para la API REST.
* **Consecuencias Positivas:** Detección temprana de regresiones en el pipeline de desarrollo y mayor confiabilidad de la aplicación ante peticiones anómalas.
* **Consecuencias Negativas / Riesgos:** Aumento en el tiempo de construcción al ejecutar la suite completa en pipelines de CI/CD.