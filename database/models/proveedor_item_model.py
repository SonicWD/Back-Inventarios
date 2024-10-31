from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


# Modelo de relación entre Proveedores e Items (ProveedorItem)
class ProveedorItem(Base):
    __tablename__ = "proveedor_items"

    id = Column(Integer, primary_key=True, index=True)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    precio = Column(Float, nullable=True)
    cantidad_minima_orden = Column(Integer, nullable=True)
    dias_entrega = Column(Integer, nullable=True)

    # Relación con Proveedor y Item
    proveedor = relationship("Proveedor", back_populates="items")
    item = relationship("Item", back_populates="proveedores")
