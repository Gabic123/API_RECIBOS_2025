# Imagen base con Python
FROM python:3.10

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY ./app /app

# Actualizar pip y luego instalar Django
RUN pip install --upgrade pip
RUN pip install django

# Exponer el puerto 8000 (Django por defecto)
EXPOSE 8000

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
