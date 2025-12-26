# wiki-BOT
Practica de microservicio

## Llamada al microservicio

Para realizar la consulta de un termino en wikipedia se puede usar el siguiente comando de bash

```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Sucker Punch Film"
}'
```

## Creación del contenedor
Para crear la imagen del contenedor, se ejecuta
```bash
docker build .
docker image ls
```

## Ejecucion del contenedor
Para ejecutar el contenedor con una IP y un puerto específicos
```bash
docker run -p 127.0.0.1:8080:8080 <img_id>
```