from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

metadata = MetaData()

# Construir la URL de conexión a la base de datos
DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/codefixIA"


# Crear una nueva instancia de motor de base de datos usando create_engine
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# Crear una fábrica de sesiones configurada con el motor de base de datos
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)
    extend_existing=True

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(engine)

