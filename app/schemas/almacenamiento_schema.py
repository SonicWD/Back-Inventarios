"""
almacenamiento_schema.py

Este módulo define los esquemas (schemas) utilizados para la validación y estructuración
de datos relacionados con los almacenes en la aplicación.

Esquemas:
- AlmacenBase: Esquema base que incluye los atributos comunes de un almacén.
- CrearAlmacen: Hereda de AlmacenBase y se utiliza al crear un nuevo almacén.
- Almacen: Extiende AlmacenBase agregando el ID del almacén, utilizado para respuestas de lectura.

Atributos:
- nombre (str): Nombre del almacén.
- tipo (str): Tipo de almacén (e.g., refrigerado, seco, general).
- rango_temperatura (Optional[str]): Rango de temperatura soportado (opcional).
- capacidad (float): Capacidad total del almacén.
- uso_actual (float): Capacidad en uso actualmente, por defecto es 0.
- id (int): Identificador único del almacén (solo en respuestas de lectura).

Este módulo facilita la validación de datos y la estructuración de respuestas 
relacionadas con el modelo de Almacén.
"""

from pydantic import BaseModel, Field
from typing import Optional


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