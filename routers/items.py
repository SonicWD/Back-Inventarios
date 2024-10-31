from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.schemas import item_schemas as schemas
from database.database import get_db
from database.models.item_model import Item
from database.models.categoria_model import Categoria


router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "No encontrado"}}
)
#   

# Obtener items
@router.get("/", response_model=List[schemas.Item])
def obtener_items(
    skip: int = 0,
    limit: int = 100,
    categoria_id: int = None,
    tipo_perecedero: schemas.TipoPerecedero = None,
    activo: bool = None,
    db: Session = Depends(get_db)
):
    query = db.query(Item)
    
    if categoria_id:
        query = query.filter(Item.categoria_id == categoria_id)
    if tipo_perecedero:
        query = query.filter(Item.tipo_perecedero == tipo_perecedero)
    if activo is not None:
        query = query.filter(Item.activo == activo)
    
    return query.offset(skip).limit(limit).all()

# Obtener item por id
@router.get("/{item_id}", response_model=schemas.Item)
def obtener_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

# Crear item
@router.post("/", response_model=schemas.Item)
def crear_item(item: schemas.CrearItem, db: Session = Depends(get_db)):
    # Verificar si existe la categoría
    if not db.query(Categoria).filter(Categoria.id == item.categoria_id).first():
        raise HTTPException(
            status_code=404,
            detail="La categoría especificada no existe"
        )
    
    db_item = Item(**item.dict())
    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se pudo crear el item: {str(e)}"
        )

# Actualizar item existente
@router.put("/{item_id}", response_model=schemas.Item)
def actualizar_item(
    item_id: int,
    item: schemas.CrearItem,
    db: Session = Depends(get_db)
):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    # Verificar si existe la categoría si se está actualizando
    if item.categoria_id:
        if not db.query(Categoria).filter(Categoria.id == item.categoria_id).first():
            raise HTTPException(
                status_code=404,
                detail="La categoría especificada no existe"
            )
    
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    
    try:
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al actualizar el item: {str(e)}"
        )

# Eliminar item
@router.delete("/{item_id}")
def eliminar_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    try:
        db.delete(item)
        db.commit()
        return {"mensaje": "Item eliminado exitosamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al eliminar el item: {str(e)}"
        )
