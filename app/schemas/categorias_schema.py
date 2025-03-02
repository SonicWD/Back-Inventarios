"""
categorias_schema.py

Este módulo define los esquemas (schemas) utilizados para la validación y estructuración
de datos relacionados con las categorías de productos en la aplicación.

Enumeraciones:
- TipoCategoria: Enum que define los tipos de categorías disponibles, como INGREDIENTE, BEBIDA, 
  UTENSILIO, entre otros.
- TipoPerecedero: Enum que indica si un producto es PERECEDERO o NO_PERECEDERO.

Esquemas:
- CategoriaBase: Esquema base que incluye los atributos comunes de una categoría.
- CrearCategoria: Hereda de CategoriaBase y se utiliza al crear una nueva categoría.
- Categoria: Extiende CategoriaBase agregando el ID de la categoría, utilizado para respuestas de lectura.

Atributos:
- nombre (str): Nombre de la categoría.
- tipo (TipoCategoria): Tipo de categoría (e.g., INGREDIENTE, BEBIDA).
- descripcion (Optional[str]): Descripción detallada de la categoría (opcional).
- id (int): Identificador único de la categoría (solo en respuestas de lectura).

Este módulo facilita la validación de datos y la estructuración de respuestas 
relacionadas con el modelo de Categoría.
"""

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
