from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database.schemas import Proveedor, CrearProveedor # Asegúrate de que los nombres sean correctos
from database.database import get_db
from database.models import Proveedor as ProveedorModel  # Asegúrate de que este nombre sea correcto

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

# Obtener todos los proveedores
@router.get("/", response_model=List[Proveedor])
def get_proveedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    proveedores = db.query(ProveedorModel).offset(skip).limit(limit).all()
    return proveedores

# Obtener un proveedor por ID
@router.get("/{proveedor_id}", response_model=Proveedor)
def get_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor = db.query(ProveedorModel).filter(ProveedorModel.id == proveedor_id).first()
    if proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

# Crear un nuevo proveedor
@router.post("/", response_model=Proveedor)
def create_proveedor(proveedor: CrearProveedor, db: Session = Depends(get_db)):
    nuevo_proveedor = ProveedorModel(**proveedor.dict())
    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)
    return nuevo_proveedor

# Actualizar un proveedor existente
@router.put("/{proveedor_id}", response_model=Proveedor)
def update_proveedor(proveedor_id: int, proveedor: CrearProveedor, db: Session = Depends(get_db)):
    proveedor_existente = db.query(ProveedorModel).filter(ProveedorModel.id == proveedor_id).first()
    if proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    
    for key, value in proveedor.dict().items():
        setattr(proveedor_existente, key, value)
    
    db.commit()
    db.refresh(proveedor_existente)
    return proveedor_existente

# Eliminar un proveedor
@router.delete("/{proveedor_id}")
def delete_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor_existente = db.query(ProveedorModel).filter(ProveedorModel.id == proveedor_id).first()
    if proveedor_existente is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    
    db.delete(proveedor_existente)
    db.commit()
    return {"detail": "Proveedor eliminado correctamente"}
