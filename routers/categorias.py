from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import models, schemas
from database.database import get_db

router = APIRouter(
    prefix="/categorias",
    tags=["categorías"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener categorías
@router.get("/", response_model=List[schemas.Categoria])
def obtener_categorias(
    skip: int = 0,
    limit: int = 100,
    tipo: schemas.TipoCategoria = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Categoria)
    if tipo:
        query = query.filter(models.Categoria.tipo == tipo)
    return query.offset(skip).limit(limit).all()

# Obtener categoría por ID
@router.get("/{categoria_id}", response_model=schemas.Categoria)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# Crear categoría
@router.post("/", response_model=schemas.Categoria)
def crear_categoria(categoria: schemas.CrearCategoria, db: Session = Depends(get_db)):
    db_categoria = models.Categoria(**categoria.dict())
    try:
        db.add(db_categoria)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se pudo crear la categoría: {str(e)}"
        )

# Actualizar categoría
@router.put("/{categoria_id}", response_model=schemas.Categoria)
def actualizar_categoria(
    categoria_id: int,
    categoria: schemas.CrearCategoria,
    db: Session = Depends(get_db)
):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    for key, value in categoria.dict().items():
        setattr(db_categoria, key, value)
    
    try:
        db.commit()
        db.refresh(db_categoria)
        return db_categoria
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al actualizar la categoría: {str(e)}"
        )

# Eliminar categoría
@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    try:
        db.delete(categoria)
        db.commit()
        return {"mensaje": "Categoría eliminada exitosamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al eliminar la categoría: {str(e)}"
        )
