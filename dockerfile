# Usa la imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY ./app /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Definir el comando para correr el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]








