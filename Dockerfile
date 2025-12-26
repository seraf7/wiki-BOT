# Imagen de Python
FROM python:3.11

# Directorio para el contenedor de la aplicacion
RUN mkdir -p /app

# Copia de directorios al contenedor
COPY ./main.py /app/
COPY mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt

# Instalacion de paquetes requeridos
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Configuracion del directorio del proyecto
WORKDIR /app

# Seleccion del puerto
EXPOSE 8080

# Ejecucion del microservicio
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]