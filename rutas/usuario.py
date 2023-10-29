from fastapi import Request, APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from db.base_datos import Usuario, Base
from db.base_datos import SessionLocal
from fastapi import HTTPException


router = APIRouter()
url = "http://localhost:8000"

class RegistroEsquema(BaseModel):
    email: str
    password: str

@router.post("/register")
async def registration(data: RegistroEsquema):
    session = SessionLocal()
    try:
        user_exists = session.query(Usuario).filter(Usuario.email == data.email).first()
        if user_exists:
            raise HTTPException(status_code=400, detail="El correo electrónico ya existe")
        user = Usuario(email=data.email, password=data.password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"email": user.email, "password": user.password}
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

@router.post("/login")
async def login(data: RegistroEsquema):
    session = SessionLocal()
    try:
        user = session.query(Usuario).filter(Usuario.email == data.email).first()

        if not user or user.password != data.password:
            raise HTTPException(status_code=400, detail="Correo electrónico o contraseña incorrecta")
        return {"message": "Inicio de sesión exitoso"}

    except Exception as e:
        raise e
    finally:
        session.close()