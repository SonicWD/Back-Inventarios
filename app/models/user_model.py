"""
user_model.py

Este módulo define el modelo de datos para los usuarios en la aplicación.

Modelo:
- UserModel: Representa a un usuario con credenciales de acceso y datos de contacto.

Atributos:
- id_user (int): Identificador único del usuario.
- username (str): Nombre de usuario único y obligatorio para el inicio de sesión.
- password (str): Contraseña en formato hash (obligatoria).
- email (str): Dirección de correo electrónico única y obligatoria.
- created_at (DateTime): Fecha y hora de creación del usuario, establecida automáticamente.
- updated_at (DateTime): Fecha y hora de la última actualización, modificada automáticamente.

Este modelo permite gestionar la información de autenticación y contacto 
de los usuarios registrados en la aplicación.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.config import Base


class UserModel(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
