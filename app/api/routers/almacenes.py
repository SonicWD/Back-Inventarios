"""
Este módulo define las rutas (endpoints) para la gestión de almacenes.

Utiliza FastAPI APIRouter para organizar los endpoints relacionados con almacenes,
incluyendo operaciones CRUD: obtener, crear, actualizar y eliminar almacenes.
Delegando la lógica de negocio al servicio correspondiente.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import almacenamiento_schema as schemas
from app.core.config import get_db
from app.services.almacenamiento_service import AlmacenamientoService

router = APIRouter(
    prefix="/almacenes",
    tags=["almacenes"],
    responses={404: {"description": "No encontrado"}}
)


def get_almacen_service(db: Session = Depends(get_db)):
    """
    Dependencia para obtener una instancia de AlmacenamientoService.

    Args:
        db (Session): Sesión de base de datos inyectada.

    Returns:
        AlmacenamientoService: Instancia del servicio de almacenes.
    """
    return AlmacenamientoService(db)


@router.get("/", response_model=List[schemas.Almacen])
def obtener_almacenes(
    skip: int = 0,
    limit: int = 100,
    almacen_service: AlmacenamientoService = Depends(get_almacen_service)
):
    """
    Obtener todos los almacenes con paginación.

    Args:
        skip (int): Número de registros a omitir (paginación).
        limit (int): Límite de registros a obtener.
        almacen_service (AlmacenamientoService): Servicio de almacenes inyectado.

    Returns:
        List[schemas.Almacen]: Lista de almacenes.
    """
    return almacen_service.obtener_todos(skip, limit)


@router.get("/{storage_id}", response_model=schemas.Almacen)
def obtener_almacen(
    storage_id: int,
    almacen_service: AlmacenamientoService = Depends(get_almacen_service)
):
    """
    Obtener un almacén por su ID.

    Args:
        storage_id (int): ID del almacén a obtener.
        almacen_service (AlmacenamientoService): Servicio de almacenes inyectado.

    Returns:
        schemas.Almacen: Detalles del almacén solicitado.

    Raises:
        HTTPException: Si no se encuentra el almacén.
    """
    almacen = almacen_service.obtener_por_id(storage_id)
    if almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    return almacen


@router.post("/", response_model=schemas.Almacen)
def crear_almacen(
    almacen: schemas.CrearAlmacen,
    almacen_service: AlmacenamientoService = Depends(get_almacen_service)
):
    """
    Crear un nuevo almacén.

    Args:
        almacen (schemas.CrearAlmacen): Datos del nuevo almacén.
        almacen_service (AlmacenamientoService): Servicio de almacenes inyectado.

    Returns:
        schemas.Almacen: Almacén creado.
    """
    return almacen_service.crear(almacen)


@router.put("/{storage_id}", response_model=schemas.Almacen)
def actualizar_almacen(
    storage_id: int,
    almacen: schemas.CrearAlmacen,
    almacen_service: AlmacenamientoService = Depends(get_almacen_service)
):
    """
    Actualizar un almacén existente.

    Args:
        storage_id (int): ID del almacén a actualizar.
        almacen (schemas.CrearAlmacen): Datos actualizados del almacén.
        almacen_service (AlmacenamientoService): Servicio de almacenes inyectado.

    Returns:
        schemas.Almacen: Almacén actualizado.
    """
    return almacen_service.actualizar(storage_id, almacen)


@router.delete("/{storage_id}")
def eliminar_almacen(
    storage_id: int,
    almacen_service: AlmacenamientoService = Depends(get_almacen_service)
):
    """
    Eliminar un almacén por su ID.

    Args:
        storage_id (int): ID del almacén a eliminar.
        almacen_service (AlmacenamientoService): Servicio de almacenes inyectado.

    Returns:
        dict: Mensaje de éxito.
    """
    almacen_service.eliminar(storage_id)
    return {"mensaje": "Almacén eliminado exitosamente"}
