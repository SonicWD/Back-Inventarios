"""
proveedor_producto_model.py

Este módulo define el modelo de datos para la relación entre proveedores y productos en la aplicación.

Modelo:
- ProveedorProducto: Representa la relación entre un proveedor y un producto, 
  incluyendo detalles como precio, cantidad mínima de orden y tiempo de entrega.

Atributos:
- id (int): Identificador único de la relación proveedor-producto.
- proveedor_id (int): Identificador del proveedor asociado (relacionado con la tabla 'proveedores').
- producto_id (int): Identificador del producto asociado (relacionado con la tabla 'productos').
- precio (float, opcional): Precio del producto ofrecido por el proveedor.
- cantidad_minima_orden (int, opcional): Cantidad mínima requerida para realizar un pedido al proveedor.
- dias_entrega (int, opcional): Tiempo de entrega estimado en días.

Relaciones:
- proveedor: Relación con el modelo Proveedor para acceder a la información del proveedor asociado.
- producto: Relación con el modelo Producto para acceder a la información del producto asociado.

Este modelo permite gestionar la información sobre los proveedores de cada producto, 
incluyendo precios, mínimos de pedido y tiempos de entrega, lo que facilita la administración de inventarios.
"""

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base

class ProveedorProducto(Base):
    __tablename__ = "proveedor_productos"

    id = Column(Integer, primary_key=True, index=True)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    precio = Column(Float, nullable=True)
    cantidad_minima_orden = Column(Integer, nullable=True)
    dias_entrega = Column(Integer, nullable=True)

    proveedor = relationship("Proveedor", back_populates="productos")
    producto = relationship("Producto", back_populates="proveedores")
