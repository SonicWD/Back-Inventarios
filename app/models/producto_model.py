"""
producto_model.py

Este módulo define el modelo de datos para los productos en la aplicación.

Modelo:
- Producto: Representa un producto almacenado en el inventario.

Atributos:
- id (int): Identificador único del producto.
- nombre (str): Nombre del producto.
- descripcion (str, opcional): Descripción detallada del producto.
- categoria_id (int): Identificador de la categoría a la que pertenece el producto (relacionado con la tabla 'categorias').
- tipo_perecible (Enum, opcional): Tipo de perecibilidad del producto (PERECEDERO o NO_PERECEDERO).
- stock_minimo (int, opcional): Cantidad mínima en stock para alertas de reposición (por defecto, 0).
- unidad (str, opcional): Unidad de medida del producto (ej. kg, litros, unidades).
- precio (float, opcional): Precio del producto.
- activo (bool): Estado del producto (activo o inactivo) (por defecto, True).

Relaciones:
- categoria: Relación con el modelo Categoria para acceder a la información de la categoría del producto.
- proveedores: Relación con el modelo ProveedorProducto para obtener los proveedores asociados al producto.
- movimientos_inventario: Relación con el modelo MovimientoInventario para rastrear los movimientos de inventario
  (entradas y salidas) del producto.

Este modelo permite gestionar los datos de los productos en el inventario, incluyendo su categoría, 
estado de perecibilidad, proveedores asociados y movimientos de stock.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.config import Base
from app.models.categoria_model import TipoPerecibleEnum


# Modelo de Product
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    tipo_perecible = Column(Enum(TipoPerecibleEnum), nullable=True)
    stock_minimo = Column(Integer, nullable=True, default=0)
    unidad = Column(String, nullable=True)
    precio = Column(Float, nullable=True)
    activo = Column(Boolean, default=True)

    # Relación con la categoría
    categoria = relationship("Categoria", back_populates="productos")

    # Relación con Supplierproducto
    proveedores = relationship("ProveedorProducto", back_populates="producto")

    # Relación con movimientos de inventario
    movimientos_inventario = relationship("MovimientoInventario", back_populates="producto")
