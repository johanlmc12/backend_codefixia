from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# Configurar la información de la base de datos directamente
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "12345678"
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "codefixIA"

# Construir la URL de conexión a la base de datos
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Crear una nueva instancia de motor de base de datos usando create_engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una fábrica de sesiones configurada con el motor de base de datos
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Crear una nueva clase base para modelos declarativos usando declarative_base
Base = declarative_base()

# Definir el modelo Usuario para representar la tabla usuario en la base de datos
class Usuarios(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)

