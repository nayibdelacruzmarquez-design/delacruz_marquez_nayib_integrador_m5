import sys
import os

# Agregar el directorio app al path para resolucion de modulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app import app as application

if __name__ == "__main__":
    application.run()