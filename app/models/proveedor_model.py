"""
proveedor_model.py

Este módulo define el modelo de datos para los proveedores en la aplicación.

Modelo:
- Proveedor: Representa a un proveedor que suministra productos al inventario.

Atributos:
- id (int): Identificador único del proveedor.
- nombre (str): Nombre del proveedor (obligatorio).
- persona_contacto (str, opcional): Nombre de la persona de contacto en el proveedor.
- correo (str, opcional): Dirección de correo electrónico del proveedor.
- telefono (str, opcional): Número de teléfono de contacto del proveedor.
- direccion (str, opcional): Dirección física del proveedor.

Relaciones:
- productos: Relación con el modelo ProveedorProducto para acceder a los productos 
  que el proveedor suministra.

Este modelo permite gestionar la información de los proveedores, 
incluyendo datos de contacto y la relación con los productos que proveen.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.config import Base

# Modelo de Proveedor
class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    persona_contacto = Column(String, nullable=True)
    correo = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    direccion = Column(String, nullable=True)

    # Relación con Supplierproducto
    productos = relationship("ProveedorProducto", back_populates="proveedor")
