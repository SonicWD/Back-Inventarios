from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Esquema base para la salida de usuario
class UserBase(BaseModel):
    username: str
    email: EmailStr


# Crear un nuevo usuario
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Esquema para la salida de usuario (sin contraseña)
class UserOut(UserBase):
    id_user: int
    created_at: datetime

    class Config:
        from_attributes = True


# Actualización de usuario
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# Esquema de inicio de sesión
class LoginUser(BaseModel):
    username: str
    password: str


# Token de autenticación
class Token(BaseModel):
    access_token: str
    token_type: str