from fastapi import FastAPI 
import uvicorn 
from db.base_datos import Base_datos
from rutas import usuario

app = FastAPI()

app.include_router(usuario.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)
