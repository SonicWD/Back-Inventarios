"""
Servicio MovimientoInventario:
Gestiona la lógica de negocio para los movimientos de inventario,
coordinando las operaciones con el repositorio.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.movimiento_schema import CrearMovimientoInventario
from app.models.movimiento_model import MovimientoInventario
from app.repositories import movimiento_inventario_repository as repo

def obtener_movimientos_inventario(skip: int, limit: int, db: Session):
    """
    Obtiene una lista de movimientos de inventario con paginación.
    """
    return repo.obtener_movimientos_inventario(skip, limit, db)

def obtener_movimiento_por_id(movement_id: int, db: Session):
    """
    Obtiene un movimiento de inventario por su ID.
    Lanza una excepción si no se encuentra.
    """
    movimiento = repo.obtener_movimiento_por_id(movement_id, db)
    if movimiento is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return movimiento

def crear_movimiento(movimiento: CrearMovimientoInventario, db: Session):
    """
    Crea un nuevo movimiento de inventario.
    """
    nuevo_movimiento = MovimientoInventario(**movimiento.dict())
    return repo.crear_movimiento(nuevo_movimiento, db)

def actualizar_movimiento(movement_id: int, datos_actualizados: CrearMovimientoInventario, db: Session):
    """
    Actualiza un movimiento de inventario existente.
    Lanza una excepción si no se encuentra.
    """
    movimiento_existente = repo.obtener_movimiento_por_id(movement_id, db)
    if movimiento_existente is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    
    return repo.actualizar_movimiento(db, movimiento_existente, datos_actualizados.dict())

def eliminar_movimiento(movement_id: int, db: Session):
    """
    Elimina un movimiento de inventario.
    Lanza una excepción si no se encuentra.
    """
    movimiento_existente = repo.obtener_movimiento_por_id(movement_id, db)
    if movimiento_existente is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    
    repo.eliminar_movimiento(movimiento_existente, db)
    return {"detail": "Movimiento eliminado correctamente"}
