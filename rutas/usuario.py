from fastapi import Request,APIRouter
from fastapi.templating import Jinja2Templates



router = APIRouter()

url = "http://localhost:8000"


@router.get("/register")
async def registration(request: Request):
    print("entre")
    form = await request.form()
    usuarios = {
        "email":form.get('email'),
        "password":form.get('password'),

    }

    