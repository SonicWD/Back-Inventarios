"""
Router ProductoProveedor:
Gestiona las rutas para la creación, consulta, 
actualización y eliminación de productos de proveedor.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.producto_proveedor_schema import ProductoProveedor, CrearProductoProveedor
from app.core.config import get_db
from app.services import producto_proveedor_service as service

router = APIRouter(
    prefix="/productos_proveedor",
    tags=["Productos de Proveedor"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener todos los productos de proveedor
@router.get("/", response_model=List[ProductoProveedor])
def obtener_productos_proveedor(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.obtener_productos_proveedor(skip, limit, db)

# Obtener un producto de proveedor por ID
@router.get("/{producto_proveedor_id}", response_model=ProductoProveedor)
def obtener_producto_proveedor(producto_proveedor_id: int, db: Session = Depends(get_db)):
    return service.obtener_producto_proveedor_por_id(producto_proveedor_id, db)

# Crear un nuevo producto de proveedor
@router.post("/", response_model=ProductoProveedor)
def crear_producto_proveedor(producto_proveedor: CrearProductoProveedor, db: Session = Depends(get_db)):
    return service.crear_producto_proveedor(producto_proveedor, db)

# Actualizar un producto de proveedor existente
@router.put("/{producto_proveedor_id}", response_model=ProductoProveedor)
def actualizar_producto_proveedor(producto_proveedor_id: int, producto_proveedor: CrearProductoProveedor, db: Session = Depends(get_db)):
    return service.actualizar_producto_proveedor(producto_proveedor_id, producto_proveedor, db)

# Eliminar un producto de proveedor
@router.delete("/{producto_proveedor_id}")
def eliminar_producto_proveedor(producto_proveedor_id: int, db: Session = Depends(get_db)):
    return service.eliminar_producto_proveedor(producto_proveedor_id, db)
