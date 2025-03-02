"""
almacen_model.py

Este módulo define el modelo de datos para los almacenes en la aplicación de inventarios.

Modelo:
- Almacen: Representa un almacén de almacenamiento de productos.

Atributos:
- id (int): Identificador único del almacén.
- nombre (str): Nombre del almacén.
- tipo (str): Tipo de almacén (por ejemplo, frío, seco, etc.).
- rango_temperatura (str): Rango de temperatura del almacén (opcional).
- capacidad (float): Capacidad total de almacenamiento.
- uso_actual (float): Capacidad utilizada actualmente.

Relaciones:
- conteos_inventario: Relación con el modelo ConteoInventario para rastrear los conteos de inventario realizados en este almacén.

Este modelo facilita la gestión de múltiples almacenes con diferentes capacidades y tipos en el sistema de inventarios.
"""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.core.config import Base


# Modelo de Almacenamiento (Almacen)
class Almacen(Base):
    __tablename__ = "almacenes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    rango_temperatura = Column(String, nullable=True)
    capacidad = Column(Float, nullable=False)
    uso_actual = Column(Float, nullable=False, default=0)

    # Relación con conteo de inventario
    conteos_inventario = relationship("ConteoInventario", back_populates="almacen")
