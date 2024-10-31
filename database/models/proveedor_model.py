from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

# Modelo de Proveedor
class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    persona_contacto = Column(String, nullable=True)
    correo = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    direccion = Column(String, nullable=True)

    # Relación con SupplierItem
    items = relationship("ProveedorItem", back_populates="proveedor")
