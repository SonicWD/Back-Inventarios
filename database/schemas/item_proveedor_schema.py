from pydantic import BaseModel, Field
from typing import Optional


# Esquemas de Item de Proveedor
class ItemProveedorBase(BaseModel):
    proveedor_id: int = Field(..., description="ID del proveedor")
    item_id: int = Field(..., description="ID del item")
    precio: Optional[float] = Field(None, description="Precio del proveedor")
    cantidad_minima_orden: Optional[int] = Field(None, description="Cantidad mínima de orden")
    tiempo_entrega_dias: Optional[int] = Field(None, description="Días de entrega")

class CrearItemProveedor(ItemProveedorBase):
    pass

class ItemProveedor(ItemProveedorBase):
    id: int
    
    class Config:
        from_attributes = True