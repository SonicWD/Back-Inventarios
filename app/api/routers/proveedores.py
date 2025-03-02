"""
Router Proveedor:
Gestiona las rutas para la creación, consulta, 
actualización y eliminación de proveedores.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.proveedor_schema import Proveedor, CrearProveedor
from app.core.config import get_db
from app.services import proveedor_service as service

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener todos los proveedores
@router.get("/", response_model=List[Proveedor])
def obtener_proveedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene todos los proveedores con paginación.
    """
    return service.obtener_proveedores(skip, limit, db)

# Obtener un proveedor por ID
@router.get("/{proveedor_id}", response_model=Proveedor)
def obtener_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un proveedor específico por su ID.
    """
    return service.obtener_proveedor_por_id(proveedor_id, db)

# Crear un nuevo proveedor
@router.post("/", response_model=Proveedor)
def crear_proveedor(proveedor: CrearProveedor, db: Session = Depends(get_db)):
    """
    Crea un nuevo proveedor.
    """
    return service.crear_proveedor(proveedor, db)

# Actualizar un proveedor existente
@router.put("/{proveedor_id}", response_model=Proveedor)
def actualizar_proveedor(proveedor_id: int, proveedor: CrearProveedor, db: Session = Depends(get_db)):
    """
    Actualiza un proveedor existente.
    """
    return service.actualizar_proveedor(proveedor_id, proveedor, db)

# Eliminar un proveedor
@router.delete("/{proveedor_id}")
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """
    Elimina un proveedor por su ID.
    """
    return service.eliminar_proveedor(proveedor_id, db)
