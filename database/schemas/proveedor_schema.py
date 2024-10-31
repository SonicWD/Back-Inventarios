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