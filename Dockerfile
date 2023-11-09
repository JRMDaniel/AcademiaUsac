# Usar una imagen base de Python
FROM python:3.9

#Establece variables de entorno para deshabilitar la salida en búfer
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

#Instala las dependencias de sistema requeridas.
RUN apt-get update && apt-get install -y postgresql-client

# Copiar los archivos de la aplicación al contenedor
COPY requeriments.txt /app/
COPY . /app

# Instalar las dependencias de la aplicación
RUN pip install -r requeriments.txt

# Comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]