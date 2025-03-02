"""
proveedor_schema.py

Este módulo define los esquemas utilizados para la gestión de proveedores en la aplicación.

Esquemas:
- ProveedorBase: Esquema base que incluye los atributos comunes para crear y visualizar un proveedor.
- CrearProveedor: Hereda de ProveedorBase y se utiliza al registrar un nuevo proveedor.
- Proveedor: Extiende ProveedorBase con el identificador único (id) del proveedor.

Atributos:
- nombre (str): Nombre del proveedor.
- persona_contacto (str, opcional): Nombre de la persona de contacto en el proveedor.
- correo (EmailStr, opcional): Correo electrónico de contacto del proveedor.
- telefono (str, opcional): Número de teléfono del proveedor.
- direccion (str, opcional): Dirección física del proveedor.
- id (int): Identificador único del proveedor (solo en Proveedor).

Estos esquemas son utilizados en las operaciones de creación, actualización y visualización de proveedores.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Esquemas de Proveedor
class ProveedorBase(BaseModel):
    nombre: str = Field(..., description="Nombre del proveedor")
    persona_contacto: Optional[str] = Field(None, description="Persona de contacto")
    correo: Optional[EmailStr] = Field(None, description="Correo electrónico")
    telefono: Optional[str] = Field(None, description="Teléfono")
    direccion: Optional[str] = Field(None, description="Dirección")

class CrearProveedor(ProveedorBase):
    pass

class Proveedor(ProveedorBase):
    id: int
    
    class Config:
        from_attributes = True