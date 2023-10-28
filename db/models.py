# Suponiendo que DB es tu clase base declarativa importada desde db.models
from db.models import DB
from sqlalchemy import Column, Integer, String

# Definición de la clase Usuario que hereda de DB (la clase base declarativa)
class Usuarios(DB):
    __tablename__ = "usuarios"  # Nombre de la tabla en la base de datos
    id_usuario = Column(Integer, primary_key=True, index=True)  # Columna id con un tipo de datos Integer y configurada como clave primaria
    email = Column(String, index=True)  # Columna correo con un tipo de datos String
    password = Column(String)  # Columna contrasena con un tipo de datos String, se ha cambiado 'contraseña' a 'contrasena'
