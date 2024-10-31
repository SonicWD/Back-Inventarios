from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.schemas import almacenamiento_schema as schemas
from database.models.almacen_model import Almacen
from database.database import get_db

router = APIRouter(
    prefix="/almacenes",
    tags=["almacenes"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener todos los almacenes
@router.get("/", response_model=List[schemas.Almacen])
def obtener_almacenes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(Almacen)
    return query.offset(skip).limit(limit).all()

# Obtener un almacén por ID
@router.get("/{storage_id}", response_model=schemas.Almacen)
def obtener_almacen(storage_id: int, db: Session = Depends(get_db)):
    almacen = db.query(Almacen).filter(Almacen.id == storage_id).first()
    if almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    return almacen

# Crear un nuevo almacén
@router.post("/", response_model=schemas.Almacen)
def crear_almacen(almacen: schemas.CrearAlmacen, db: Session = Depends(get_db)):
    db_almacen = Almacen(**almacen.dict())
    try:
        db.add(db_almacen)
        db.commit()
        db.refresh(db_almacen)
        return db_almacen
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se pudo crear el almacén: {str(e)}"
        )

# Actualizar un almacén existente
@router.put("/{storage_id}", response_model=schemas.Almacen)
def actualizar_almacen(
    storage_id: int,
    almacen: schemas.CrearAlmacen,
    db: Session = Depends(get_db)
):
    db_almacen = db.query(Almacen).filter(Almacen.id == storage_id).first()
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    
    for key, value in almacen.dict().items():
        setattr(db_almacen, key, value)
    
    try:
        db.commit()
        db.refresh(db_almacen)
        return db_almacen
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al actualizar el almacén: {str(e)}"
        )

# Eliminar un almacén
@router.delete("/{storage_id}")
def eliminar_almacen(storage_id: int, db: Session = Depends(get_db)):
    almacen = db.query(Almacen).filter(Almacen.id == storage_id).first()
    if almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    
    try:
        db.delete(almacen)
        db.commit()
        return {"mensaje": "Almacén eliminado exitosamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al eliminar el almacén: {str(e)}"
        )
