from db.base_datos import Base
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
import uvicorn
from rutas import usuario  # Asegúrate de que este módulo y ruta de importación sean correctos
from rutas import usuario_router
from fastapi.middleware.cors import CORSMiddleware

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes de todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Incluir el router del módulo usuario en la aplicación
app.include_router(usuario.router)

# Ejecutar la aplicación usando uvicorn si este script se ejecuta directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

