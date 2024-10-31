from pydantic import BaseModel, Field
from typing import Optional


# Esquemas de Almacenamiento
class AlmacenBase(BaseModel):
    nombre: str = Field(..., description="Nombre del almacén")
    tipo: str = Field(..., description="Tipo de almacén")
    rango_temperatura: Optional[str] = Field(None, description="Rango de temperatura")
    capacidad: float = Field(..., description="Capacidad total")
    uso_actual: float = Field(0, description="Uso actual")

class CrearAlmacen(AlmacenBase):
    pass

class Almacen(AlmacenBase):
    id: int
    
    class Config:
        from_attributes = True