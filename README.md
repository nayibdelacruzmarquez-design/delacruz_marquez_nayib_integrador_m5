# Proyecto Integrador — Módulo 4: Server-Side Rendering & PaaS Deployment

* **Autor:** Nayib de la Cruz Márquez
* **Entorno de Ejecución:** Python 3.12.10
* **Despliegue PaaS:** [https://pdevs-ssr-m4-integrador.onrender.com](https://pdevs-ssr-m4-integrador.onrender.com)
* **Video de Defensa:** [Ver Video en Google Drive](https://drive.google.com/drive/folders/1j1lw28lWHji4ChnlmPaOqDly6VtWvA4Y?usp=sharing)
---

## 🚀 Instrucciones para Ejecución Local

1. **Clonar el repositorio:**
   ```powershell
   git clone [https://github.com/nayibdelacruzmarquez-design/pdevs-ssr-m4-integrador.git](https://github.com/nayibdelacruzmarquez-design/pdevs-ssr-m4-integrador.git)
   cd pdevs-ssr-m4-integrador
   ```
   
2. **Crear e inicializar el entorno virtual:**
   ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
   ```
   
3. **Ejecutar la aplicación web:**
   ```powershell
    python src/app/app.py
   ```
   
* Acceder a http://127.0.0.1:5000

* Credenciales Demo:

* Admin: admin / adminpassword

* Usuario: usuario / userpassword

## 🧪 Ejecución de Spikes y Pruebas
Para ejecutar el script de evidencia de optimización ORM:
   ```powershell
    python src/tests/spike_test.py
   ```
## 📂 Estructura del Proyecto
* dossier/: Registros de Decisiones Arquitectónicas (ADR-4.1 a 4.8 y ADR-9).
* src/app/: Código fuente de la aplicación web Flask (Modelos, Vistas y Formularios).
* src/tests/: Pruebas de concepto y logs de ejecución no falsificables.
* fuentes.md: Bitácora de 12 fuentes técnicas primarias y secundarias.
* autocritica.md: Análisis crítico y puntos de falla del sistema.
