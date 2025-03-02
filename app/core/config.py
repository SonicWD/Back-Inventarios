"""
config.py

Este módulo configura la conexión a la base de datos para la aplicación, utilizando SQLAlchemy.

Componentes principales:
- SQLALCHEMY_DATABASE_URL: URL de conexión a la base de datos (en este caso, una base de datos SQLite local).
- engine: Motor de conexión a la base de datos.
- SessionLocal: Sesión de base de datos para realizar operaciones ORM.
- Base: Clase base para la declaración de modelos ORM.
- get_db: Generador de contexto para obtener y cerrar sesiones de base de datos de manera segura.

Este archivo centraliza la configuración de la base de datos para facilitar cambios futuros (como migrar a otro SGBD).
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./inventarios.db"  

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
