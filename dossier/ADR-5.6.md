# ADR 5.6: Estrategia de Gestión de Configuración e Inyección de Dependencias

* **Contexto:** La aplicación heredada mantenía parámetros de configuración y cadenas de conexión a base de datos codificados directamente en los archivos de la aplicación, dificultando las pruebas y violando principios de seguridad.
* **Alternativas:** 
  1. Archivos de configuración estáticos (`config.py` con valores globales hardcodeados).
  2. Variables de entorno leídas dinámicamente mediante `os.getenv` y patrón Application Factory.
  3. Servicios externos de gestión de secretos (AWS Secrets Manager / HashiCorp Vault).
* **Criterio de Selección:** Garantizar la separación estricta entre código y configuración siguiendo la metodología 12-Factor App, facilitando el cambio entre entornos de desarrollo, pruebas y producción.
* **Evidencia Empírica:** La prueba de inyección de configuración (`src/tests/test_spike_5_6.py`) demostró el aislamiento efectivo de credenciales y la capacidad de conmutar automáticamente a bases de datos efímeras en memoria para suites de prueba.
* **Decisión:** Adoptar el patrón Application Factory en Flask combinado con clases de configuración derivadas que leen variables de entorno.
* **Consecuencias Positivas:** Mayor seguridad al no exponer credenciales en el repositorio de código y facilidad para ejecutar pruebas automatizadas en entornos aislados.
* **Consecuencias Negativas / Riesgos:** Requerimiento de definir y documentar las variables de entorno obligatorias en el archivo `.env.example` para nuevos desarrolladores.