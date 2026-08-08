# Autocrítica y Reflexión Técnica - Módulo 5

**Desarrollador:** Nayib de la Cruz Márquez  

### 1. ¿Qué no probaste, y qué riesgo aceptaste al no probarlo?
No se probaron **mecanismos de autenticación/autorización con tokens JWT en peticiones concurrentes masivas** ni **persistencia en bases de datos relacionales de producción (como PostgreSQL)** bajo volumen real de escrituras simultáneas, utilizando SQLite para los Spikes. El riesgo aceptado es que SQLite en un entorno contenerizado puede presentar bloqueos de concurrencia de lectura/escritura (`database is locked`) al recibir escrituras paralelas en producción.

### 2. ¿Dónde se rompe tu servicio con 10× peticiones? Sé concreto: qué componente, por qué, y con qué número lo sabes.
El servicio se rompe en la **capa del servidor WSGI y el pool de conexiones de la Base de Datos**. 
* **Evidencia:** En el Spike 5.1 alcanzamos un throughput de **76.35 req/s** con 10 peticiones concurrentes sin fallos. 
* **Punto de quiebre:** Si escalamos a 10× peticiones (100 peticiones concurrentes simultáneas), el componente que falla es el servidor síncrono de Flask/WSGI configurado por defecto con 1 solo proceso, saturando la cola de peticiones HTTP, elevando la latencia promedio por encima de los 5 segundos de timeout y provocando errores de conexión `504 Gateway Timeout` y agotamiento del pool del ORM.

### 3. ¿En qué ADR te equivocaste? ¿Qué evidencia te faltó ver a tiempo?
Me equivoqué en el **ADR 5.1 (Modelo de Ejecución del Servidor)** al mantener el servidor de desarrollo de Flask por defecto durante los spikes iniciales en lugar de haber configurado de entrada un servidor de grado de producción multiproceso como Gunicorn/Waitress. La evidencia que me faltó ver a tiempo fue el impacto directo que el bloqueo de un solo hilo tiene cuando el ORM en el ADR 5.5 realiza operaciones complejas de I/O a la base de datos.