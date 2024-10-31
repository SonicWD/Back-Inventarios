from pydantic import BaseModel, Field
from datetime import datetime


# Esquemas de Conteo de Inventario
class ConteoInventarioBase(BaseModel):
    item_id: int = Field(..., description="ID del item")
    almacen_id: int = Field(..., description="ID del almacén")
    cantidad: float = Field(..., description="Cantidad contada")
    responsable: str = Field(..., description="Responsable del conteo")

class CrearConteoInventario(ConteoInventarioBase):
    pass

class ConteoInventario(ConteoInventarioBase):
    id: int
    fecha_ultimo_conteo: datetime
    
    class Config:
        from_attributes = True
