from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Francisco317@localhost:5432/codefixIA"
Base_datos = create_engine (SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker (bind=Base_datos, autocommit=False, autoflush=False)


DB = declarative_base()

