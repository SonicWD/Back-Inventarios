"""
Este módulo gestiona las consultas a la base de datos para productos.

Incluye funciones para:
- Obtener productos con filtros.
- Obtener un producto por ID.
- Crear un nuevo producto.
- Actualizar un producto existente.
- Eliminar un producto.
"""

from sqlalchemy.orm import Session
from app.models.producto_model import Producto

def get_productos(db: Session, skip: int, limit: int, categoria_id: int, tipo_perecedero, activo: bool):
    """
    Obtiene una lista de productos aplicando filtros opcionales.
    """
    query = db.query(Producto)
    if categoria_id:
        query = query.filter(Producto.categoria_id == categoria_id)
    if tipo_perecedero:
        query = query.filter(Producto.tipo_perecible == tipo_perecedero)
    if activo is not None:
        query = query.filter(Producto.activo == activo)
    return query.offset(skip).limit(limit).all()

def get_producto_by_id(db: Session, producto_id: int):
    """
    Obtiene un producto específico por su ID.
    """
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, producto_data):
    """
    Crea un nuevo producto en la base de datos.
    """
    db_producto = Producto(**producto_data.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, producto_data):
    """
    Actualiza un producto existente en la base de datos.
    """
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        return None
    
    # Actualizar los campos del producto
    for key, value in producto_data.dict().productos():
        setattr(db_producto, key, value)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int):
    """
    Elimina un producto de la base de datos.
    """
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        return None
    
    db.delete(db_producto)
    db.commit()
    return True
