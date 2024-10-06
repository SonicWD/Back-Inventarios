from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database.schemas import ItemProveedor, CrearItemProveedor
from database.database import get_db
from database.models import ProveedorItem  # Asegúrate de que este sea el nombre correcto del modelo

router = APIRouter(
    prefix="/items_proveedor",
    tags=["Items de Proveedor"]
)

# Obtener todos los items de proveedor
@router.get("/", response_model=List[ItemProveedor])
def obtener_items_proveedor(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items_proveedor = db.query(ProveedorItem).offset(skip).limit(limit).all()
    return items_proveedor

# Obtener un item de proveedor por ID
@router.get("/{item_proveedor_id}", response_model=ItemProveedor)
def obtener_item_proveedor(item_proveedor_id: int, db: Session = Depends(get_db)):
    item_proveedor = db.query(ProveedorItem).filter(ProveedorItem.id == item_proveedor_id).first()
    if item_proveedor is None:
        raise HTTPException(status_code=404, detail="Item de proveedor no encontrado")
    return item_proveedor

# Crear un nuevo item de proveedor
@router.post("/", response_model=ItemProveedor)
def crear_item_proveedor(item_proveedor: CrearItemProveedor, db: Session = Depends(get_db)):
    nuevo_item_proveedor = ProveedorItem(**item_proveedor.dict())
    db.add(nuevo_item_proveedor)
    db.commit()
    db.refresh(nuevo_item_proveedor)
    return nuevo_item_proveedor

# Actualizar un item de proveedor existente
@router.put("/{item_proveedor_id}", response_model=ItemProveedor)
def actualizar_item_proveedor(item_proveedor_id: int, item_proveedor: CrearItemProveedor, db: Session = Depends(get_db)):
    item_proveedor_existente = db.query(ProveedorItem).filter(ProveedorItem.id == item_proveedor_id).first()
    if item_proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Item de proveedor no encontrado")
    
    for key, value in item_proveedor.dict().items():
        setattr(item_proveedor_existente, key, value)
    
    db.commit()
    db.refresh(item_proveedor_existente)
    return item_proveedor_existente

# Eliminar un item de proveedor
@router.delete("/{item_proveedor_id}")
def eliminar_item_proveedor(item_proveedor_id: int, db: Session = Depends(get_db)):
    item_proveedor_existente = db.query(ProveedorItem).filter(ProveedorItem.id == item_proveedor_id).first()
    if item_proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Item de proveedor no encontrado")
    
    db.delete(item_proveedor_existente)
    db.commit()
    return {"detail": "Item de proveedor eliminado correctamente"}
