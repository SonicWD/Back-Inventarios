from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# Esquemas de Movimiento de Inventario
class MovimientoInventarioBase(BaseModel):
    item_id: int = Field(..., description="ID del item")
    cantidad: float = Field(..., description="Cantidad")
    tipo_movimiento: str = Field(..., description="Tipo de movimiento (entrada/salida)")
    numero_referencia: Optional[str] = Field(None, description="Número de referencia")
    notas: Optional[str] = Field(None, description="Notas adicionales")

class CrearMovimientoInventario(MovimientoInventarioBase):
    pass

class MovimientoInventario(MovimientoInventarioBase):
    id: int
    fecha: datetime
    
    class Config:
        from_attributes = True