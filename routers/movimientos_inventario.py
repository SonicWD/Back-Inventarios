from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import models, schemas
from database.database import get_db

router = APIRouter(
    prefix="/movimientos_inventario",
    tags=["Movimientos de Inventario"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener todos los movimientos de inventario
@router.get("/", response_model=List[schemas.MovimientoInventario])
def obtener_movimientos_inventario(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(models.MovimientoInventario)
    return query.offset(skip).limit(limit).all()

# Obtener un movimiento por ID
@router.get("/{movement_id}", response_model=schemas.MovimientoInventario)
def obtener_movimiento(movement_id: int, db: Session = Depends(get_db)):
    movimiento = db.query(models.MovimientoInventario).filter(models.MovimientoInventario.id == movement_id).first()
    if movimiento is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return movimiento

# Crear un nuevo movimiento de inventario
@router.post("/", response_model=schemas.MovimientoInventario)
def crear_movimiento(movimiento: schemas.CrearMovimientoInventario, db: Session = Depends(get_db)):
    db_movimiento = models.MovimientoInventario(**movimiento.dict())
    try:
        db.add(db_movimiento)
        db.commit()
        db.refresh(db_movimiento)
        return db_movimiento
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se pudo crear el movimiento: {str(e)}"
        )

# Actualizar un movimiento de inventario
@router.put("/{movement_id}", response_model=schemas.MovimientoInventario)
def actualizar_movimiento(
    movement_id: int,
    movimiento: schemas.CrearMovimientoInventario,
    db: Session = Depends(get_db)
):
    db_movimiento = db.query(models.MovimientoInventario).filter(models.MovimientoInventario.id == movement_id).first()
    if db_movimiento is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    
    for key, value in movimiento.dict().items():
        setattr(db_movimiento, key, value)
    
    try:
        db.commit()
        db.refresh(db_movimiento)
        return db_movimiento
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al actualizar el movimiento: {str(e)}"
        )

# Eliminar un movimiento de inventario
@router.delete("/{movement_id}")
def eliminar_movimiento(movement_id: int, db: Session = Depends(get_db)):
    movimiento = db.query(models.MovimientoInventario).filter(models.MovimientoInventario.id == movement_id).first()
    if movimiento is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    
    try:
        db.delete(movimiento)
        db.commit()
        return {"mensaje": "Movimiento eliminado exitosamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al eliminar el movimiento: {str(e)}"
        )
