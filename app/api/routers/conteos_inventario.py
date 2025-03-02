"""
Este módulo define las rutas para gestionar los conteos de inventario.

Incluye endpoints para:
- Obtener todos los conteos de inventario.
- Obtener un conteo de inventario por ID.
- Crear un nuevo conteo de inventario.
- Actualizar un conteo de inventario existente.
- Eliminar un conteo de inventario.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import conteo_schema as schemas
from app.core.config import get_db
from app.services.conteos_inventario import (
    obtener_conteos,
    obtener_conteo_por_id,
    crear_conteo,
    actualizar_conteo,
    eliminar_conteo
)

router = APIRouter(
    prefix="/conteos_inventario",
    tags=["conteos_inventario"],
    responses={404: {"description": "No encontrado"}}
)


@router.get("/", response_model=List[schemas.ConteoInventario])
def obtener_conteos_inventario(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtener todos los conteos de inventario.

    Parámetros:
    - skip (int): Número de registros a omitir (paginación).
    - limit (int): Número máximo de registros a devolver.
    - db (Session): Sesión de base de datos inyectada con Depends.

    Retorna:
    - List[schemas.ConteoInventario]: Lista de conteos de inventario.
    """
    return obtener_conteos(db, skip, limit)


@router.get("/{count_id}", response_model=schemas.ConteoInventario)
def obtener_conteo_inventario(count_id: int, db: Session = Depends(get_db)):
    """
    Obtener un conteo de inventario por su ID.

    Parámetros:
    - count_id (int): ID del conteo de inventario.
    - db (Session): Sesión de base de datos.

    Retorna:
    - schemas.ConteoInventario: Objeto del conteo de inventario.
    """
    conteo = obtener_conteo_por_id(db, count_id)
    if conteo is None:
        raise HTTPException(status_code=404, detail="Conteo de inventario no encontrado")
    return conteo


@router.post("/", response_model=schemas.ConteoInventario)
def crear_conteo_inventario(conteo: schemas.CrearConteoInventario, db: Session = Depends(get_db)):
    """
    Crear un nuevo conteo de inventario.

    Parámetros:
    - conteo (schemas.CrearConteoInventario): Datos del conteo a crear.
    - db (Session): Sesión de base de datos.

    Retorna:
    - schemas.ConteoInventario: Conteo de inventario creado.
    """
    return crear_conteo(db, conteo)


@router.put("/{count_id}", response_model=schemas.ConteoInventario)
def actualizar_conteo_inventario(
    count_id: int,
    conteo: schemas.CrearConteoInventario,
    db: Session = Depends(get_db)
):
    """
    Actualizar un conteo de inventario existente.

    Parámetros:
    - count_id (int): ID del conteo a actualizar.
    - conteo (schemas.CrearConteoInventario): Datos actualizados.
    - db (Session): Sesión de base de datos.

    Retorna:
    - schemas.ConteoInventario: Conteo de inventario actualizado.
    """
    return actualizar_conteo(db, count_id, conteo)


@router.delete("/{count_id}")
def eliminar_conteo_inventario(count_id: int, db: Session = Depends(get_db)):
    """
    Eliminar un conteo de inventario por su ID.

    Parámetros:
    - count_id (int): ID del conteo a eliminar.
    - db (Session): Sesión de base de datos.

    Retorna:
    - dict: Mensaje de confirmación de eliminación.
    """
    return eliminar_conteo(db, count_id)
