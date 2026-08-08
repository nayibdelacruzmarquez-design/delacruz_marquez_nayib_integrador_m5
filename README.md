# Módulo 5: Proyecto Integrador - Refactorización de API REST, Tests y Contenerización

**Estudiante:** Nayib de la Cruz Márquez  
**Repositorio GitHub:** [https://github.com/nayibdelacruzmarquez-design/delacruz_marquez_nayib_integrador_m5](https://github.com/nayibdelacruzmarquez-design/delacruz_marquez_nayib_integrador_m5)  
**URL de Servicio en Producción (Render):** [https://delacruz-marquez-nayib-integrador-m5.onrender.com](https://pdevs-ssr-m4-integrador.onrender.com)  
**Enlace a Video de Defensa (5 min):** *[Poner enlace aquí]*  

---

## Descripción del Proyecto
Este proyecto corresponde al **Módulo 5 del Programa Integrador**, enfocado en la refactorización de la arquitectura base legada (Server-Side Rendering) hacia una **API REST desacoplada y profesional**. 

Durante el proceso se aplicó la metodología de arquitectura empírica mediante **Spikes de rendimiento**, documentando 8 Architecture Decision Records (**ADRs 5.1 a 5.8**) en la carpeta `dossier/`, culminando con el **ADR-9** de integración y empaquetado final con **Docker**.

---

## Arquitectura y Tecnologías
* **Backend:** Python 3.12, Flask (Application Factory Pattern, Blueprints).
* **ORM & Base de Datos:** SQLAlchemy, Flask-SQLAlchemy, SQLite / PostgreSQL.
* **Migraciones de Esquema:** Flask-Migrate (Alembic).
* **Pruebas Automatizadas:** Pytest, Inyección de Fallos, Captura de Evidencias No Falsificables.
* **Contenerización y Despliegue:** Docker, Gunicorn, Render PaaS.

---

## Estructura del Repositorio
```text
de_la_cruz_marquez_nayib_integrador_m5/
├── dossier/                # Registros de Decisiones de Arquitectura (ADR 5.1 - 5.8 y ADR-9)
├── src/
│   ├── app/                # Código fuente de la API REST (Application Factory)
│   └── tests/              # Suite de pruebas automatizadas y Spikes de rendimiento
├── migrations/             # Historial de migraciones de la base de datos (Alembic)
├── Dockerfile              # Manifiesto de contenerización oficial
├── Procfile                # Comando de arranque para servidores PaaS (Gunicorn)
├── requirements.txt        # Lista de dependencias del proyecto
├── fuentes.md              # Bitácora de 12 fuentes técnicas primarias
├── autocritica.md          # Respuestas escritas de autocrítica técnica
└── README.md               # Documentación general y guía de ejecución
```
## Instrucciones de Ejecución Local
1. Clonar el repositorio y configurar entorno
```PowerShell
git clone [https://github.com/nayibdelacruzmarquez-design/delacruz_marquez_nayib_integrador_m5.git](https://github.com/nayibdelacruzmarquez-design/delacruz_marquez_nayib_integrador_m5.git)
cd de_la_cruz_marquez_nayib_integrador_m5
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
2. Ejecutar la suite de pruebas y spikes de rendimiento
```PowerShell
python src/tests/test_spike_5_1.py
python src/tests/test_spike_5_3.py
python src/tests/test_spike_5_4.py
python src/tests/test_spike_5_5.py
python src/tests/test_spike_5_6.py
python src/tests/test_spike_5_7.py
python src/tests/test_spike_5_8.py
```
3. Levantar la aplicación localmente
```PowerShell
python -m flask run --host=0.0.0.0 --port=5000
```
## Ejecución Docker
Construir e iniciar el contenedor
```bash
docker build -t app-integrador-m5 .
docker run -p 5000:5000 app-integrador-m5
```
## Resumen de Decisiones de Arquitectura (ADRs)
Todas las evidencias empíricas con timestamp, hostname y platform no falsificables se encuentran en dossier/:

* ADR 5.1: Modelo de Ejecución del Servidor (WSGI Multiproceso).

* ADR 5.2: Serialización y Protocolo de API REST (JSON).

* ADR 5.3: Frontera Front/Back y Renderizado.

* ADR 5.4: Estrategia de Migración de Base de Datos.

* ADR 5.5: Prevención del problema N+1 en Consultas ORM.

* ADR 5.6: Inyección de Dependencias y 12-Factor Config.
 
* ADR 5.7: Suite de Pruebas y Resiliencia ante Fallos.

* ADR 5.8: Contenerización con Docker.

* ADR 9: Decisiones Finales de Integración y Despliegue.

