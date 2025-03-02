"""
Servicio Proveedor:
Gestiona la lógica de negocio para los proveedores,
coordinando las operaciones con el repositorio.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.proveedor_schema import CrearProveedor
from app.models.proveedor_model import Proveedor as ProveedorModel
from app.repositories import proveedor_repository as repo

def obtener_proveedores(skip: int, limit: int, db: Session):
    """
    Obtiene una lista de proveedores con paginación.
    """
    return repo.obtener_proveedores(skip, limit, db)

def obtener_proveedor_por_id(proveedor_id: int, db: Session):
    """
    Obtiene un proveedor por su ID.
    Lanza una excepción si no se encuentra.
    """
    proveedor = repo.obtener_proveedor_por_id(proveedor_id, db)
    if proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

def crear_proveedor(proveedor: CrearProveedor, db: Session):
    """
    Crea un nuevo proveedor.
    """
    nuevo_proveedor = ProveedorModel(**proveedor.dict())
    return repo.crear_proveedor(nuevo_proveedor, db)

def actualizar_proveedor(proveedor_id: int, datos_actualizados: CrearProveedor, db: Session):
    """
    Actualiza un proveedor existente.
    Lanza una excepción si no se encuentra.
    """
    proveedor_existente = repo.obtener_proveedor_por_id(proveedor_id, db)
    if proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    
    return repo.actualizar_proveedor(db, proveedor_existente, datos_actualizados.dict())

def eliminar_proveedor(proveedor_id: int, db: Session):
    """
    Elimina un proveedor.
    Lanza una excepción si no se encuentra.
    """
    proveedor_existente = repo.obtener_proveedor_por_id(proveedor_id, db)
    if proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    
    repo.eliminar_proveedor(proveedor_existente, db)
    return {"detail": "Proveedor eliminado correctamente"}
# Compare this snippet from app/api/routers/__init__.py: