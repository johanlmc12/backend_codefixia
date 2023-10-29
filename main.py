from db.base_datos import Base, SessionLocal
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
import uvicorn
from rutas import usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

def get_db():
    Base = SessionLocal()
    try:
        yield Base
    finally:
        Base.close()

app.include_router(usuario.router)

# Ejecutar la aplicación usando uvicorn si este script se ejecuta directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

