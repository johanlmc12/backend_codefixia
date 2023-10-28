from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData
from databases import Database
from models.usuario import usuarios
from fastapi import FastAPI
from rutas import usuario



DATABASE_URL = "postgresql://posgrest:12345678@localhost:5432/codefixIA"

database = Database(DATABASE_URL)
metadata = MetaData()

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(usuario.router)