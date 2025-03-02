"""
Repositorio Proveedor:
Encapsula la lógica de acceso a datos para los proveedores,
facilitando las operaciones CRUD con la base de datos.
"""

from sqlalchemy.orm import Session
from app.models.proveedor_model import Proveedor as ProveedorModel

def obtener_proveedores(skip: int, limit: int, db: Session):
    """
    Obtiene una lista de proveedores con paginación.
    """
    return db.query(ProveedorModel).offset(skip).limit(limit).all()

def obtener_proveedor_por_id(proveedor_id: int, db: Session):
    """
    Obtiene un proveedor por su ID.
    """
    return db.query(ProveedorModel).filter(ProveedorModel.id == proveedor_id).first()

def crear_proveedor(nuevo_proveedor: ProveedorModel, db: Session):
    """
    Crea un nuevo proveedor.
    """
    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)
    return nuevo_proveedor

def actualizar_proveedor(db: Session, proveedor_existente: ProveedorModel, datos_actualizados: dict):
    """
    Actualiza un proveedor existente con los datos proporcionados.
    """
    for key, value in datos_actualizados.productos():
        setattr(proveedor_existente, key, value)
    
    db.commit()
    db.refresh(proveedor_existente)
    return proveedor_existente

def eliminar_proveedor(proveedor: ProveedorModel, db: Session):
    """
    Elimina un proveedor existente.
    """
    db.delete(proveedor)
    db.commit()
