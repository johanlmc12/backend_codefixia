from db.models import DB
from sqlalchemy import Table, Column, Integer, String

class Usuario(DB):
    __tablename__ = "usuarios"
    Column("id", Integer, primary_key=True),
    Column("correo", String),
    Column("contraseña", String),