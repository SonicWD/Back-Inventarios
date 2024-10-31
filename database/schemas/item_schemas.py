from pydantic import BaseModel, Field
from typing import Optional
from database.schemas.categorias_schema import TipoPerecedero


# Esquemas de Item
class ItemBase(BaseModel):
    nombre: str = Field(..., description="Nombre del item")
    descripcion: Optional[str] = Field(None, description="Descripción del item")
    categoria_id: int = Field(..., description="ID de la categoría a la que pertenece")
    tipo_perecible: Optional[TipoPerecedero] = Field(None, description="Tipo de perecibilidad")
    stock_minimo: Optional[int] = Field(0, description="Stock mínimo requerido")
    unidad: Optional[str] = Field(None, description="Unidad de medida")
    precio: Optional[float] = Field(None, description="Precio unitario")
    activo: bool = Field(True, description="Estado activo/inactivo del item")

class CrearItem(ItemBase):
    pass

class Item(ItemBase):
    id: int
    
    class Config:
        from_attributes = True