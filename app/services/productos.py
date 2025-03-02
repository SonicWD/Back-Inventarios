"""
Este módulo contiene la lógica de negocio para gestionar productos.

Incluye funciones para:
- Obtener todos los productos.
- Obtener un producto por ID.
- Crear un nuevo producto.
- Actualizar un producto existente.
- Eliminar un producto.
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.producto_schemas import CrearProducto
from app.repositories.producto import (
    get_productos,
    get_producto_by_id,
    create_producto,
    update_producto,
    delete_producto
)

def obtener_todos_los_productos(db: Session, skip: int, limit: int, categoria_id: int, tipo_perecedero, activo: bool):
    return get_productos(db, skip, limit, categoria_id, tipo_perecedero, activo)

def obtener_producto_por_id(db: Session, producto_id: int):
    producto = get_producto_by_id(db, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

def crear_nuevo_producto(db: Session, producto: CrearProducto):
    return create_producto(db, producto)

def actualizar_producto_existente(db: Session, producto_id: int, producto: CrearProducto):
    return update_producto(db, producto_id, producto)

def eliminar_producto(db: Session, producto_id: int):
    return delete_producto(db, producto_id)
