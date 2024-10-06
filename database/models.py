from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime
import enum

# Definimos los tipos de enum que corresponden a las categorías y perecibilidad
class TipoCategoriaEnum(str, enum.Enum):
    INGREDIENTE = "INGREDIENTE"
    BEBIDA = "BEBIDA"
    UTENSILIO = "UTENSILIO"
    MOBILIARIO = "MOBILIARIO"
    LIMPIEZA = "LIMPIEZA"
    OFICINA = "OFICINA"
    PICNIC = "PICNIC"
    DECORACION = "DECORACION"
    UNIFORME = "UNIFORME"

class TipoPerecibleEnum(str, enum.Enum):
    PERECEDERO = "PERECEDERO"
    NO_PERECEDERO = "NO_PERECEDERO"

# Modelo de Categoría
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(Enum(TipoCategoriaEnum), nullable=False)
    descripcion = Column(String, nullable=True)

    # Relación con Items
    items = relationship("Item", back_populates="categoria")

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
