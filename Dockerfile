# Imagen base oficial liviana de Python
FROM python:3.12-slim

# Evitar que Python escriba archivos .pyc y forzar salida de logs sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . /app/

# Exponer el puerto predeterminado de la API
EXPOSE 5000

# Comando por defecto para arrancar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--chdir", "src", "wsgi:application"]