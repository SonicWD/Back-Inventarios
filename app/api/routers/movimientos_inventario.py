"""
Router MovimientoInventario:
Gestiona las rutas para la creación, consulta, 
actualización y eliminación de movimientos de inventario.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.movimiento_schema import MovimientoInventario, CrearMovimientoInventario
from app.core.config import get_db
from app.services import movimiento_inventario_service as service

router = APIRouter(
    prefix="/movimientos_inventario",
    tags=["Movimientos de Inventario"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener todos los movimientos de inventario
@router.get("/", response_model=List[MovimientoInventario])
def obtener_movimientos_inventario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene todos los movimientos de inventario con paginación.
    """
    return service.obtener_movimientos_inventario(skip, limit, db)

# Obtener un movimiento por ID
@router.get("/{movement_id}", response_model=MovimientoInventario)
def obtener_movimiento(movement_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un movimiento de inventario específico por su ID.
    """
    return service.obtener_movimiento_por_id(movement_id, db)

# Crear un nuevo movimiento de inventario
@router.post("/", response_model=MovimientoInventario)
def crear_movimiento(movimiento: CrearMovimientoInventario, db: Session = Depends(get_db)):
    """
    Crea un nuevo movimiento de inventario.
    """
    return service.crear_movimiento(movimiento, db)

# Actualizar un movimiento de inventario existente
@router.put("/{movement_id}", response_model=MovimientoInventario)
def actualizar_movimiento(movement_id: int, movimiento: CrearMovimientoInventario, db: Session = Depends(get_db)):
    """
    Actualiza un movimiento de inventario existente.
    """
    return service.actualizar_movimiento(movement_id, movimiento, db)

# Eliminar un movimiento de inventario
@router.delete("/{movement_id}")
def eliminar_movimiento(movement_id: int, db: Session = Depends(get_db)):
    """
    Elimina un movimiento de inventario por su ID.
    """
    return service.eliminar_movimiento(movement_id, db)
