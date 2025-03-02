"""
producto_schema.py

Este módulo define los esquemas utilizados para la gestión de productos en la aplicación.

Esquemas:
- ProductoBase: Esquema base que incluye los atributos comunes para crear y visualizar un producto.
- CrearProducto: Hereda de ProductoBase y se utiliza al registrar un nuevo producto.
- Producto: Extiende ProductoBase con el identificador único (id) del producto.

Atributos:
- nombre (str): Nombre del producto.
- descripcion (str, opcional): Descripción detallada del producto.
- categoria_id (int): ID de la categoría a la que pertenece el producto.
- tipo_perecible (TipoPerecedero, opcional): Tipo de perecibilidad del producto (PERECEDERO o NO_PERECEDERO).
- stock_minimo (int, opcional): Stock mínimo requerido para el producto.
- unidad (str, opcional): Unidad de medida del producto (ej. kg, litro, unidad).
- precio (float, opcional): Precio unitario del producto.
- activo (bool): Estado activo/inactivo del producto.
- id (int): Identificador único del producto (solo en Producto).

Estos esquemas son utilizados en las operaciones de creación, actualización y visualización de productos.
"""

from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.categorias_schema import TipoPerecedero


# Esquemas de Producto
class ProductoBase(BaseModel):
    nombre: str = Field(..., description="Nombre del producto")
    descripcion: Optional[str] = Field(None, description="Descripción del producto")
    categoria_id: int = Field(..., description="ID de la categoría a la que pertenece")
    tipo_perecible: Optional[TipoPerecedero] = Field(None, description="Tipo de perecibilidad")
    stock_minimo: Optional[int] = Field(0, description="Stock mínimo requerido")
    unidad: Optional[str] = Field(None, description="Unidad de medida")
    precio: Optional[float] = Field(None, description="Precio unitario")
    activo: bool = Field(True, description="Estado activo/inactivo del producto")

class CrearProducto(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    
    class Config:
        from_attributes = True
