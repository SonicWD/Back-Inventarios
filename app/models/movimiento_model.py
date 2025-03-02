"""
movimiento_inventario_model.py

Este módulo define el modelo de datos para los movimientos de inventario en la aplicación.

Modelo:
- MovimientoInventario: Representa un movimiento de inventario que puede ser de entrada o salida.

Atributos:
- id (int): Identificador único del movimiento de inventario.
- producto_id (int): Identificador del producto afectado por el movimiento (relacionado con la tabla 'productos').
- cantidad (float): Cantidad del producto movido (positiva para entradas, negativa para salidas).
- tipo_movimiento (str): Tipo de movimiento ('entrada' o 'salida').
- numero_referencia (str, opcional): Número de referencia asociado al movimiento (ej. número de factura o pedido).
- notas (str, opcional): Notas adicionales sobre el movimiento.
- fecha (datetime): Fecha y hora en que se registró el movimiento (por defecto, la fecha y hora actual en el servidor).

Relaciones:
- producto: Relación con el modelo Producto para acceder a la información del producto afectado.

Este modelo permite rastrear los movimientos de inventario, tanto de entrada como de salida, facilitando
el control de stock y el historial de transacciones de productos.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.config import Base
from sqlalchemy.sql import func


# Modelo de Movimiento de Inventario (MovimientoInventario)
class MovimientoInventario(Base):
    __tablename__ = "movimientos_inventario"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Float, nullable=False)
    tipo_movimiento = Column(String, nullable=False)  # entrada/salida
    numero_referencia = Column(String, nullable=True)
    notas = Column(String, nullable=True)
    fecha = Column(DateTime, server_default=func.now(), nullable=False)

    # Relación con producto
    producto = relationship("producto", back_populates="movimientos_inventario")
