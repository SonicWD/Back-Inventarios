from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from sqlalchemy.sql import func


# Modelo de Movimiento de Inventario (MovimientoInventario)
class MovimientoInventario(Base):
    __tablename__ = "movimientos_inventario"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    cantidad = Column(Float, nullable=False)
    tipo_movimiento = Column(String, nullable=False)  # entrada/salida
    numero_referencia = Column(String, nullable=True)
    notas = Column(String, nullable=True)
    fecha = Column(DateTime, server_default=func.now(), nullable=False)

    # Relación con Item
    item = relationship("Item", back_populates="movimientos_inventario")
