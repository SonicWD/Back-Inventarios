"""
conteo_model.py

Este módulo define el modelo de datos para el conteo de inventario en la aplicación.

Modelo:
- ConteoInventario: Representa un registro de conteo de inventario realizado en un almacén específico.

Atributos:
- id (int): Identificador único del conteo de inventario.
- producto_id (int): Identificador del producto contado (relacionado con la tabla 'productos').
- almacen_id (int): Identificador del almacén donde se realizó el conteo (relacionado con la tabla 'almacenes').
- cantidad (float): Cantidad del producto contada en el almacén.
- contado_por (str): Nombre de la persona que realizó el conteo.
- fecha_ultimo_conteo (datetime): Fecha y hora del último conteo (por defecto, la fecha y hora actual).

Relaciones:
- producto: Relación con el modelo Producto para acceder a la información del producto contado.
- almacen: Relación con el modelo Almacen para acceder a la información del almacén donde se realizó el conteo.

Este modelo permite registrar y gestionar los conteos de inventario, proporcionando un historial de las cantidades
de productos en los diferentes almacenes.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.config import Base


# Modelo de Conteo de Inventario (ConteoInventario)
class ConteoInventario(Base):
    __tablename__ = "conteos_inventario"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    almacen_id = Column(Integer, ForeignKey("almacenes.id"), nullable=False)
    cantidad = Column(Float, nullable=False)
    contado_por = Column(String, nullable=False)
    fecha_ultimo_conteo = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relación con producto y Almacen
    producto = relationship("producto")
    almacen = relationship("Almacen", back_populates="conteos_inventario")