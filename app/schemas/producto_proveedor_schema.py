"""
producto_proveedor_schema.py

Este módulo define los esquemas utilizados para la gestión de la relación entre productos y proveedores en la aplicación.

Esquemas:
- ProductoProveedorBase: Esquema base que incluye los atributos comunes para crear y visualizar la relación producto-proveedor.
- CrearProductoProveedor: Hereda de ProductoProveedorBase y se utiliza al registrar un nuevo producto para un proveedor.
- ProductoProveedor: Extiende ProductoProveedorBase con el identificador único (id) de la relación.

Atributos:
- proveedor_id (int): ID del proveedor asociado al producto.
- producto_id (int): ID del producto relacionado con el proveedor.
- precio (float, opcional): Precio del producto ofrecido por el proveedor.
- cantidad_minima_orden (int, opcional): Cantidad mínima requerida para una orden.
- tiempo_entrega_dias (int, opcional): Tiempo estimado de entrega en días.
- id (int): Identificador único de la relación producto-proveedor (solo en ProductoProveedor).

Estos esquemas son utilizados en las operaciones de creación, actualización y visualización de la relación entre productos y proveedores.
"""

from pydantic import BaseModel, Field
from typing import Optional

# Esquemas de Producto de Proveedor
class ProductoProveedorBase(BaseModel):
    proveedor_id: int = Field(..., description="ID del proveedor")
    producto_id: int = Field(..., description="ID del producto")
    precio: Optional[float] = Field(None, description="Precio del proveedor")
    cantidad_minima_orden: Optional[int] = Field(None, description="Cantidad mínima de orden")
    tiempo_entrega_dias: Optional[int] = Field(None, description="Días de entrega")

class CrearProductoProveedor(ProductoProveedorBase):
    pass

class ProductoProveedor(ProductoProveedorBase):
    id: int
    
    class Config:
        from_attributes = True
