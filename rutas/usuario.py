from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy import create_engine, MetaData
from databases import Database  # Asegúrate de importar tu base de datos correctamente
from models import usuario
from fastapi import FastAPI

app = FastAPI()

router = APIRouter()

DATABASE_URL = "postgresql+psycopg2://posgrest:Francisco317@localhost:5432/codefixIA"

database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/usuarios/{usuario_id}")
async def leer_usuario(usuario_id: int):
    query = usuario.select().where(usuario.c.id == usuario_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result