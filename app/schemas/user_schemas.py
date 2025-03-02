"""
user_schema.py

Este módulo define los esquemas utilizados para la gestión de usuarios y autenticación en la aplicación.

Esquemas:
- UserBase: Esquema base que incluye los atributos comunes para la visualización de un usuario.
- UserCreate: Se utiliza para registrar un nuevo usuario, incluyendo la contraseña.
- UserOut: Extiende UserBase y agrega el identificador único (id_user) y la fecha de creación (created_at).
- UserUpdate: Esquema para actualizar un usuario, permitiendo campos opcionales.
- LoginUser: Se utiliza para la autenticación del usuario mediante nombre de usuario y contraseña.
- Token: Representa el token de acceso JWT generado al autenticar un usuario.

Atributos:
- username (str): Nombre de usuario único.
- email (EmailStr): Correo electrónico del usuario.
- password (str, opcional): Contraseña del usuario (solo en UserCreate y UserUpdate).
- id_user (int): Identificador único del usuario (solo en UserOut).
- created_at (datetime): Fecha de creación del usuario (solo en UserOut).
- access_token (str): Token de acceso JWT (solo en Token).
- token_type (str): Tipo de token (ej. "bearer", solo en Token).

Estos esquemas son utilizados en las operaciones de creación, actualización, autenticación y visualización de usuarios.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(UserBase):
    id_user: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class LoginUser(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str