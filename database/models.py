from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime
import enum

# Definimos los tipos de enum que corresponden a las categorías y perecibilidad
class CategoryTypeEnum(str, enum.Enum):
    INGREDIENT = "INGREDIENTE"
    BEVERAGE = "BEBIDA"
    UTENSIL = "UTENSILIO"
    FURNITURE = "MOBILIARIO"
    CLEANING = "LIMPIEZA"
    OFFICE = "OFICINA"
    PICNIC = "PICNIC"
    DECORATION = "DECORACION"
    UNIFORM = "UNIFORME"

class PerishableTypeEnum(str, enum.Enum):
    PERISHABLE = "PERECEDERO"
    NON_PERISHABLE = "NO_PERECEDERO"

# Modelo de Categoría
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(Enum(CategoryTypeEnum), nullable=False)
    description = Column(String, nullable=True)

    # Relación con Items
    items = relationship("Item", back_populates="category")

# Modelo de Item
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    perishable_type = Column(Enum(PerishableTypeEnum), nullable=True)
    minimum_stock = Column(Integer, nullable=True, default=0)
    unit = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)

    # Relación con la categoría
    category = relationship("Category", back_populates="items")

    # Relación con SupplierItem
    suppliers = relationship("SupplierItem", back_populates="item")

    # Relación con movimientos de inventario
    inventory_movements = relationship("InventoryMovement", back_populates="item")

# Modelo de Proveedor (Supplier)
class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_person = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)

    # Relación con SupplierItem
    items = relationship("SupplierItem", back_populates="supplier")

# Modelo de relación entre Proveedores e Items (SupplierItem)
class SupplierItem(Base):
    __tablename__ = "supplier_items"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    price = Column(Float, nullable=True)
    minimum_order_quantity = Column(Integer, nullable=True)
    lead_time_days = Column(Integer, nullable=True)

    # Relación con Supplier y Item
    supplier = relationship("Supplier", back_populates="items")
    item = relationship("Item", back_populates="suppliers")

# Modelo de Movimiento de Inventario (InventoryMovement)
class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    movement_type = Column(String, nullable=False)  # entrada/salida
    reference_number = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    date = Column(DateTime, server_default=func.now(), nullable=False)

    # Relación con Item
    item = relationship("Item", back_populates="inventory_movements")

# Modelo de Almacenamiento (Storage)
class Storage(Base):
    __tablename__ = "storages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    temperature_range = Column(String, nullable=True)
    capacity = Column(Float, nullable=False)
    current_usage = Column(Float, nullable=False, default=0)

    # Relación con conteo de inventario
    inventory_counts = relationship("InventoryCount", back_populates="storage")

# Modelo de Conteo de Inventario (InventoryCount)
class InventoryCount(Base):
    __tablename__ = "inventory_counts"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    storage_id = Column(Integer, ForeignKey("storages.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    counted_by = Column(String, nullable=False)
    last_count_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relación con Item y Storage
    item = relationship("Item")
    storage = relationship("Storage", back_populates="inventory_counts")
