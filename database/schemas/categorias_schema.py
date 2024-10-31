from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class TipoCategoria(str, Enum):
    INGREDIENTE = "INGREDIENTE"
    BEBIDA = "BEBIDA"
    UTENSILIO = "UTENSILIO"
    MOBILIARIO = "MOBILIARIO"
    LIMPIEZA = "LIMPIEZA"
    OFICINA = "OFICINA"
    PICNIC = "PICNIC"
    DECORACION = "DECORACION"
    UNIFORME = "UNIFORME"


class TipoPerecedero(str, Enum):
    PERECEDERO = "PERECEDERO"
    NO_PERECEDERO = "NO_PERECEDERO"


# Esquemas de Categoría
class CategoriaBase(BaseModel):
    nombre: str = Field(..., description="Nombre de la categoría")
    tipo: TipoCategoria = Field(..., description="Tipo de categoría")
    descripcion: Optional[str] = Field(None, description="Descripción de la categoría")


class CrearCategoria(CategoriaBase):
    pass


class Categoria(CategoriaBase):
    id: int
    
    class Config:
        from_attributes = True
