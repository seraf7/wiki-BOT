import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.bot import scrape

# Crea instancia de la API
app = FastAPI()


# Crea un modelo de datos para usar en la API
class Wiki(BaseModel):
    name: str


# Define ruta y funcionalidad para peticion GET
@app.get("/")
async def root():
    return {"mesage": "Hola desde FastAPI"}


# Ruta y funcionalidad para peticion POST al bot de wiki
# realiza validacion de datos con el modelo Wiki definido
@app.post("/wiki")
async def scrape_wiki(wiki: Wiki):
    # Realiza consulta del bot de Wikipedia
    respuesta = scrape(termino=wiki.name)
    payload = {"wikipage": respuesta}
    # Convierte respuesta a JSON
    respuesta_json = jsonable_encoder(payload)
    # Envia respuesta de la API
    return JSONResponse(content=respuesta_json)


# Ruta y funcionalidad GET para sumar dos numeros
# valida que los parametros sean numeros enteros
@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    total = num1 + num2
    return {"total": total}


# Ejecuta servidor web con la aplicacion de FastAPI
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
