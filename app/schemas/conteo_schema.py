"""
conteo_schema.py

Este módulo define los esquemas (schemas) utilizados para la validación y estructuración
de datos relacionados con los conteos de inventario en la aplicación.

Esquemas:
- ConteoInventarioBase: Esquema base que incluye los atributos comunes de un conteo de inventario.
- CrearConteoInventario: Hereda de ConteoInventarioBase y se utiliza al registrar un nuevo conteo.
- ConteoInventario: Extiende ConteoInventarioBase agregando el ID del conteo y la fecha del último conteo, 
  utilizado para respuestas de lectura.

Atributos:
- producto_id (int): Identificador del producto contado.
- almacen_id (int): Identificador del almacén donde se realizó el conteo.
- cantidad (float): Cantidad contada del producto.
- responsable (str): Nombre del responsable que realizó el conteo.
- id (int): Identificador único del conteo de inventario (solo en respuestas de lectura).
- fecha_ultimo_conteo (datetime): Fecha y hora del último conteo registrado.

Este módulo facilita la validación de datos y la estructuración de respuestas 
relacionadas con el modelo de Conteo de Inventario.
"""

from pydantic import BaseModel, Field
from datetime import datetime


# Esquemas de Conteo de Inventario
class ConteoInventarioBase(BaseModel):
    producto_id: int = Field(..., description="ID del producto")
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
