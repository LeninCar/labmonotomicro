# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en la imagen
WORKDIR /app

# Copia el archivo requirements.txt y el código de la aplicación
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]
