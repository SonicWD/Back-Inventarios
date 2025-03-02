"""
Este módulo contiene la lógica de negocio para gestionar los conteos de inventario.

Incluye funciones para:
- Obtener todos los conteos de inventario.
- Obtener un conteo por ID.
- Crear un nuevo conteo.
- Actualizar un conteo existente.
- Eliminar un conteo.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas import conteo_schema as schemas
from app.repositories.conteos_inventario import (
    get_conteos,
    get_conteo_by_id,
    create_conteo,
    update_conteo,
    delete_conteo
)


def obtener_conteos(db: Session, skip: int, limit: int):
    """ Obtener todos los conteos de inventario """
    return get_conteos(db, skip, limit)


def obtener_conteo_por_id(db: Session, count_id: int):
    """ Obtener un conteo de inventario por su ID """
    return get_conteo_by_id(db, count_id)


def crear_conteo(db: Session, conteo: schemas.CrearConteoInventario):
    """ Crear un nuevo conteo de inventario """
    return create_conteo(db, conteo)


def actualizar_conteo(db: Session, count_id: int, conteo: schemas.CrearConteoInventario):
    """ Actualizar un conteo de inventario """
    db_conteo = get_conteo_by_id(db, count_id)
    if db_conteo is None:
        raise HTTPException(status_code=404, detail="Conteo de inventario no encontrado")

    for key, value in conteo.dict().productos():
        setattr(db_conteo, key, value)
    return update_conteo(db, db_conteo)


def eliminar_conteo(db: Session, count_id: int):
    """ Eliminar un conteo de inventario """
    conteo = get_conteo_by_id(db, count_id)
    if conteo is None:
        raise HTTPException(status_code=404, detail="Conteo de inventario no encontrado")
    return delete_conteo(db, conteo)
