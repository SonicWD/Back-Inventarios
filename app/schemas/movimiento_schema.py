"""
movimiento_inventario_schema.py

Este módulo define los esquemas utilizados para la gestión de movimientos de inventario en la aplicación.

Esquemas:
- MovimientoInventarioBase: Esquema base que incluye los atributos comunes para crear y visualizar movimientos de inventario.
- CrearMovimientoInventario: Hereda de MovimientoInventarioBase y se utiliza al registrar un nuevo movimiento de inventario.
- MovimientoInventario: Extiende MovimientoInventarioBase con el identificador único (id) y la fecha en que se registró el movimiento.

Atributos:
- producto_id (int): ID del producto relacionado con el movimiento.
- cantidad (float): Cantidad de producto involucrada en el movimiento.
- tipo_movimiento (str): Tipo de movimiento (entrada/salida).
- numero_referencia (str, opcional): Número de referencia asociado al movimiento.
- notas (str, opcional): Notas adicionales sobre el movimiento.
- id (int): Identificador único del movimiento (solo en MovimientoInventario).
- fecha (datetime): Fecha y hora en que se registró el movimiento (solo en MovimientoInventario).

Estos esquemas son utilizados en las operaciones de creación, actualización y visualización de movimientos de inventario.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# Esquemas de Movimiento de Inventario
class MovimientoInventarioBase(BaseModel):
    producto_id: int = Field(..., description="ID del producto")
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