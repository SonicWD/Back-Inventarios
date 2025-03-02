"""
Servicio ProductoProveedor:
Gestiona la lógica de negocio para productos de proveedor,
coordinando las operaciones con el repositorio.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.producto_proveedor_schema import CrearProductoProveedor
from app.models.producto_proveedor_model import ProveedorProducto
from app.repositories import producto_proveedor_repository as repo

def obtener_productos_proveedor(skip: int, limit: int, db: Session):
    return repo.obtener_productos_proveedor(skip, limit, db)

def obtener_producto_proveedor_por_id(producto_proveedor_id: int, db: Session):
    producto_proveedor = repo.obtener_producto_proveedor_por_id(producto_proveedor_id, db)
    if producto_proveedor is None:
        raise HTTPException(status_code=404, detail="Producto de proveedor no encontrado")
    return producto_proveedor

def crear_producto_proveedor(producto_proveedor: CrearProductoProveedor, db: Session):
    nuevo_producto_proveedor = ProveedorProducto(**producto_proveedor.dict())
    return repo.crear_producto_proveedor(nuevo_producto_proveedor, db)

def actualizar_producto_proveedor(producto_proveedor_id: int, datos_actualizados: CrearProductoProveedor, db: Session):
    producto_proveedor_existente = repo.obtener_producto_proveedor_por_id(producto_proveedor_id, db)
    if producto_proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Producto de proveedor no encontrado")
    
    return repo.actualizar_producto_proveedor(db, producto_proveedor_existente, datos_actualizados.dict())

def eliminar_producto_proveedor(producto_proveedor_id: int, db: Session):
    producto_proveedor_existente = repo.obtener_producto_proveedor_por_id(producto_proveedor_id, db)
    if producto_proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Producto de proveedor no encontrado")
    
    repo.eliminar_producto_proveedor(producto_proveedor_existente, db)
    return {"detail": "Producto de proveedor eliminado correctamente"}
