# ADR 5.1: Selección del Modelo de Ejecución del Servidor

* **Contexto:** La aplicación heredada de la arquitectura base requiere procesar solicitudes concurrentes sin presentar cuellos de botella ni bloqueos I/O en peticiones simultáneas.
* **Alternativas:** 
  1. Servidor WSGI monohilo síncrono por defecto.
  2. Servidor de aplicaciones multiproceso con Gunicorn y workers síncronos/gevent.
  3. Reescritura completa del framework a modelo asíncrono ASGI.
* **Criterio de Selección:** Maximizar el throughput y la tolerancia a cargas simultáneas garantizando compatibilidad con la base de código existente sin requerir migración asíncrona total.
* **Evidencia Empírica:** La ejecución del benchmark concuerda con la salida cruda registrada en las pruebas del sistema:

```text
============================================================
EVIDENCIA DE EJECUCIÓN - SPIKE 5.1
TIMESTAMP : 2026-08-08T10:15:27.102938
HOSTNAME  : NAYIB-PC
PLATFORM  : Windows-10-10.0.19045-SP0
============================================================
Peticiones exitosas (HTTP 200) : 10/10
Tiempo total de ráfaga         : 0.1248 s
Latencia promedio              : 0.0381 s
Throughput estimado            : 80.13 req/s
============================================================
```
* **Decisión:** Adoptar un modelo de ejecución multiproceso apoyado en servidor WSGI de producción (Gunicorn/Waitress) configurado con la fórmula de 2N+1 workers.
* **Consecuencias Positivas:** Se elimina el bloqueo por hilo individual, aumentando la capacidad de respuesta concurrente con bajo esfuerzo de refactorización.
* **Consecuencias Negativas/Riesgos:** Incremento en el consumo de memoria RAM por cada proceso worker e imposibilidad de mantener variables globales en memoria compartida.








