# ADR 5.7: Estrategia de Pruebas Automatizadas y Resiliencia ante Fallos

* **Contexto:** Las pruebas manuales en el Módulo 4 resultaban lentas y propensas a omitir errores de regresión al realizar cambios en las rutas de la API o modelos.
* **Alternativas:** 
  1. Pruebas manuales orientadas a cliente mediante Postman o navegador.
  2. Pruebas unitarias básicas de componentes aislados sin evaluar integración.
  3. Suite automatizada de pruebas de integración con Pytest e inyección de fallos explícitos.
* **Criterio de Selección:** Maximizar la cobertura de código y garantizar que los controladores HTTP respondan con códigos de estado adecuados (4xx y 5xx) ante datos corruptos.
* **Evidencia Empírica:** La simulación en la suite (`src/tests/test_spike_5_7.py`) arrojó la captura completa de 5 vectores de error inyectados:

```text
============================================================
EVIDENCIA DE EJECUCIÓN - SPIKE 5.7 (SUITE Y SIMULACIÓN DE FALLOS)
TIMESTAMP : 2026-08-08T11:55:03.602368
HOSTNAME  : Nayibdlcm
PLATFORM  : Windows-11-10.0.26200-SP0
============================================================
[+] Ejecutando inyección de 5 vectores de fallo en la suite...
    - Vector #1: Payload JSON malformado -> CAPTURADO EXITOSAMENTE
    - Vector #2: Inyección de tipo (String en lugar de Int) -> CAPTURADO EXITOSAMENTE
    - Vector #3: Acceso a recurso inexistente (404) -> CAPTURADO EXITOSAMENTE
    - Vector #4: Violación de restricción UNIQUE en BD -> CAPTURADO EXITOSAMENTE
    - Vector #5: Timeout en servicio externo simulado -> CAPTURADO EXITOSAMENTE
------------------------------------------------------------
[+] Fallos inyectados : 5
[+] Fallos detectados : 5
[SUCCESS] Suite de pruebas validada: 100% de resistencia a fallos inyectados.
============================================================
```
* **Decisión:** Implementar Pytest como framework estandarizado de pruebas ejecutando suites de integración para la API REST.

* **Consecuencias Positivas:** Detección temprana de regresiones en el pipeline de desarrollo y mayor confiabilidad de la aplicación ante peticiones anómalas.

* **Consecuencias Negativas / Riesgos:** Aumento en el tiempo de construcción al ejecutar la suite completa en pipelines de CI/CD.