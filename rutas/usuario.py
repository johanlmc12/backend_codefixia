from fastapi import Request, APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

router = APIRouter()
templates = Jinja2Templates(directory="templates")

url = "http://localhost:8000"

class RegistroEsquema(BaseModel):
    email: str
    password: str

@router.post("/register", response_class=HTMLResponse)
async def registration(request: Request, data: RegistroEsquema):
    print("entre")
    usuarios = {
        "email": data.email,
        "password": data.password,
    }
    # Suponiendo que tienes una plantilla llamada "register_response.html"
    return templates.TemplateResponse("register_response.html", {"request": request, "usuarios": usuarios})
