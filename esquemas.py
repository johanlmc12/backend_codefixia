from pydantic import BaseModel

class UsuarioRegistro(BaseModel):
    correo: str
    contrasena: str