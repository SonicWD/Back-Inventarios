"""
Repositorio ProductoProveedor:
Encapsula la lógica de acceso a datos para los productos de proveedor,
facilitando las operaciones CRUD con la base de datos.
"""

from sqlalchemy.orm import Session
from app.models.producto_proveedor_model import ProveedorProducto

def obtener_productos_proveedor(skip: int, limit: int, db: Session):
    return db.query(ProveedorProducto).offset(skip).limit(limit).all()

def obtener_producto_proveedor_por_id(producto_proveedor_id: int, db: Session):
    return db.query(ProveedorProducto).filter(ProveedorProducto.id == producto_proveedor_id).first()

def crear_producto_proveedor(producto_proveedor: ProveedorProducto, db: Session):
    db.add(producto_proveedor)
    db.commit()
    db.refresh(producto_proveedor)
    return producto_proveedor

def actualizar_producto_proveedor(db: Session, producto_proveedor_existente: ProveedorProducto, datos_actualizados: dict):
    for key, value in datos_actualizados.productos():
        setattr(producto_proveedor_existente, key, value)
    
    db.commit()
    db.refresh(producto_proveedor_existente)
    return producto_proveedor_existente

def eliminar_producto_proveedor(producto_proveedor: ProveedorProducto, db: Session):
    db.delete(producto_proveedor)
    db.commit()
