# ADR 5.6: Estrategia de Gestión de Configuración e Inyección de Dependencias

* **Contexto:** La aplicación heredada mantenía parámetros de configuración y cadenas de conexión a base de datos codificados directamente en los archivos de la aplicación, dificultando las pruebas y violando principios de seguridad.
* **Alternativas:** 
  1. Archivos de configuración estáticos (`config.py` con valores globales hardcodeados).
  2. Variables de entorno leídas dinámicamente mediante `os.getenv` y patrón Application Factory.
  3. Servicios externos de gestión de secretos (AWS Secrets Manager / HashiCorp Vault).
* **Criterio de Selección:** Garantizar la separación estricta entre código y configuración siguiendo la metodología 12-Factor App, facilitando el cambio entre entornos de desarrollo, pruebas y producción.
* **Evidencia Empírica:** La prueba de inyección (`src/tests/test_spike_5_6.py`) confirmó la detección del entorno de testing y el aislamiento de credenciales:

```text
============================================================
EVIDENCIA DE EJECUCIÓN - SPIKE 5.6 (CONFIGURACIÓN / DI)
TIMESTAMP : 2026-08-08T11:39:46.040150
HOSTNAME  : Nayibdlcm
PLATFORM  : Windows-11-10.0.26200-SP0
============================================================
[+] Entorno detectado          : testing
[+] Modo Testing Activo        : True
[+] URI de BD Inyectada         : sqlite:///:memory:
------------------------------------------------------------
[SUCCESS] Configuración inyectada correctamente sin hardcodear credenciales.
============================================================
```
* **Decisión:** Adoptar el patrón Application Factory en Flask combinado con clases de configuración derivadas que leen variables de entorno.

* **Consecuencias Positivas:** Mayor seguridad al no exponer credenciales en el repositorio de código y facilidad para ejecutar pruebas automatizadas en entornos aislados.

* **Consecuencias Negativas / Riesgos:** Requerimiento de definir y documentar las variables de entorno obligatorias en el archivo .env.example.
