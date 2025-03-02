"""
Repositorio MovimientoInventario:
Encapsula la lógica de acceso a datos para los movimientos de inventario,
facilitando las operaciones CRUD con la base de datos.
"""

from sqlalchemy.orm import Session
from app.models.movimiento_model import MovimientoInventario

def obtener_movimientos_inventario(skip: int, limit: int, db: Session):
    """
    Obtiene una lista de movimientos de inventario con paginación.
    """
    return db.query(MovimientoInventario).offset(skip).limit(limit).all()

def obtener_movimiento_por_id(movement_id: int, db: Session):
    """
    Obtiene un movimiento de inventario por su ID.
    """
    return db.query(MovimientoInventario).filter(MovimientoInventario.id == movement_id).first()

def crear_movimiento(movimiento: MovimientoInventario, db: Session):
    """
    Crea un nuevo movimiento de inventario.
    """
    db.add(movimiento)
    db.commit()
    db.refresh(movimiento)
    return movimiento

def actualizar_movimiento(db: Session, movimiento_existente: MovimientoInventario, datos_actualizados: dict):
    """
    Actualiza un movimiento de inventario existente con los datos proporcionados.
    """
    for key, value in datos_actualizados.productos():
        setattr(movimiento_existente, key, value)
    
    db.commit()
    db.refresh(movimiento_existente)
    return movimiento_existente

def eliminar_movimiento(movimiento: MovimientoInventario, db: Session):
    """
    Elimina un movimiento de inventario existente.
    """
    db.delete(movimiento)
    db.commit()
