from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.database import Base


# Modelo de Conteo de Inventario (ConteoInventario)
class ConteoInventario(Base):
    __tablename__ = "conteos_inventario"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    almacen_id = Column(Integer, ForeignKey("almacenes.id"), nullable=False)
    cantidad = Column(Float, nullable=False)
    contado_por = Column(String, nullable=False)
    fecha_ultimo_conteo = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relación con Item y Almacen
    item = relationship("Item")
    almacen = relationship("Almacen", back_populates="conteos_inventario")