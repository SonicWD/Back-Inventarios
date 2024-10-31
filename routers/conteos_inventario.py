from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.schemas import conteo_schema as schemas
from database.models.conteo_model import ConteoInventario
from database.database import get_db

router = APIRouter(
    prefix="/conteos_inventario",
    tags=["conteos_inventario"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener todos los conteos de inventario
@router.get("/", response_model=List[schemas.ConteoInventario])
def obtener_conteos_inventario(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(ConteoInventario)
    return query.offset(skip).limit(limit).all()

# Obtener un conteo de inventario por ID
@router.get("/{count_id}", response_model=schemas.ConteoInventario)
def obtener_conteo_inventario(count_id: int, db: Session = Depends(get_db)):
    conteo = db.query(ConteoInventario).filter(ConteoInventario.id == count_id).first()
    if conteo is None:
        raise HTTPException(status_code=404, detail="Conteo de inventario no encontrado")
    return conteo

# Crear un nuevo conteo de inventario
@router.post("/", response_model=schemas.ConteoInventario)
def crear_conteo_inventario(conteo: schemas.CrearConteoInventario, db: Session = Depends(get_db)):
    db_conteo = ConteoInventario(**conteo.dict())
    try:
        db.add(db_conteo)
        db.commit()
        db.refresh(db_conteo)
        return db_conteo
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se pudo crear el conteo de inventario: {str(e)}"
        )

# Actualizar un conteo de inventario existente
@router.put("/{count_id}", response_model=schemas.ConteoInventario)
def actualizar_conteo_inventario(
    count_id: int,
    conteo: schemas.CrearConteoInventario,
    db: Session = Depends(get_db)
):
    db_conteo = db.query(ConteoInventario).filter(ConteoInventario.id == count_id).first()
    if db_conteo is None:
        raise HTTPException(status_code=404, detail="Conteo de inventario no encontrado")
    
    for key, value in conteo.dict().items():
        setattr(db_conteo, key, value)
    
    try:
        db.commit()
        db.refresh(db_conteo)
        return db_conteo
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al actualizar el conteo de inventario: {str(e)}"
        )

# Eliminar un conteo de inventario
@router.delete("/{count_id}")
def eliminar_conteo_inventario(count_id: int, db: Session = Depends(get_db)):
    conteo = db.query(ConteoInventario).filter(ConteoInventario.id == count_id).first()
    if conteo is None:
        raise HTTPException(status_code=404, detail="Conteo de inventario no encontrado")
    
    try:
        db.delete(conteo)
        db.commit()
        return {"mensaje": "Conteo de inventario eliminado exitosamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al eliminar el conteo de inventario: {str(e)}"
        )
