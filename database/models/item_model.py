from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from database.models.categoria_model import TipoPerecibleEnum


# Modelo de Item
class Item(Base):
    __tablename__ = "items"

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
    categoria = relationship("Categoria", back_populates="items")

    # Relación con SupplierItem
    proveedores = relationship("ProveedorItem", back_populates="item")

    # Relación con movimientos de inventario
    movimientos_inventario = relationship("MovimientoInventario", back_populates="item")
