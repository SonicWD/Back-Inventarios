"""
Este módulo define las rutas para gestionar productos.

Incluye endpoints para:
- Obtener todos los productos.
- Obtener un producto por ID.
- Crear un nuevo producto.
- Actualizar un producto existente.
- Eliminar un producto.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.producto_schemas import Producto, CrearProducto, TipoPerecedero
from app.core.config import get_db
from app.services.productos import (
    obtener_todos_los_productos,
    obtener_producto_por_id,
    crear_nuevo_producto,
    actualizar_producto_existente,
    eliminar_producto
)

router = APIRouter(
    prefix="/productos",
    tags=["productos"],
    responses={404: {"description": "No encontrado"}}
)

# Obtener productos
@router.get("/", response_model=List[Producto])
def obtener_productos(
    skip: int = 0,
    limit: int = 100,
    categoria_id: int = None,
    tipo_perecedero: TipoPerecedero = None,
    activo: bool = None,
    db: Session = Depends(get_db)
):
    """
    Obtener una lista de productos con filtros opcionales.
    
    Parámetros:
    - skip (int): Número de registros a saltar.
    - limit (int): Límite de registros a obtener.
    - categoria_id (int): Filtrar por ID de categoría.
    - tipo_perecedero (TipoPerecedero): Filtrar por tipo de perecibilidad.
    - activo (bool): Filtrar por estado activo/inactivo.
    """
    return obtener_todos_los_productos(db, skip, limit, categoria_id, tipo_perecedero, activo)

# Obtener producto por id
@router.get("/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    """
    Obtener un producto por su ID.
    
    Parámetros:
    - producto_id (int): ID del producto a buscar.
    """
    return obtener_producto_por_id(db, producto_id)

# Crear producto
@router.post("/", response_model=Producto)
def crear_producto(producto: CrearProducto, db: Session = Depends(get_db)):
    """
    Crear un nuevo producto.
    
    Parámetros:
    - producto (CrearProducto): Datos del nuevo producto.
    """
    return crear_nuevo_producto(db, producto)

# Actualizar producto existente
@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto(
    producto_id: int,
    producto: CrearProducto,
    db: Session = Depends(get_db)
):
    """
    Actualizar un producto existente.
    
    Parámetros:
    - producto_id (int): ID del producto a actualizar.
    - producto (CrearProducto): Datos actualizados del producto.
    """
    return actualizar_producto_existente(db, producto_id, producto)

# Eliminar producto
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    """
    Eliminar un producto por su ID.
    
    Parámetros:
    - producto_id (int): ID del producto a eliminar.
    """
    return eliminar_producto(db, producto_id)
