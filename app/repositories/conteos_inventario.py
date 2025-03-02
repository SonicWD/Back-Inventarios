"""
Este módulo gestiona las consultas a la base de datos para los conteos de inventario.

Incluye funciones para:
- Obtener todos los conteos.
- Obtener un conteo por ID.
- Crear un conteo.
- Actualizar un conteo.
- Eliminar un conteo.
"""

from sqlalchemy.orm import Session
from app.models.conteo_model import ConteoInventario


def get_conteos(db: Session, skip: int, limit: int):
    """ Obtener todos los conteos de inventario """
    return db.query(ConteoInventario).offset(skip).limit(limit).all()


def get_conteo_by_id(db: Session, count_id: int):
    """ Obtener un conteo de inventario por su ID """
    return db.query(ConteoInventario).filter(ConteoInventario.id == count_id).first()


def create_conteo(db: Session, conteo):
    """ Crear un nuevo conteo de inventario """
    db.add(conteo)
    db.commit()
    db.refresh(conteo)
    return conteo


def update_conteo(db: Session, conteo):
    """ Actualizar un conteo de inventario """
    db.commit()
    db.refresh(conteo)
    return conteo


def delete_conteo(db: Session, conteo):
    """ Eliminar un conteo de inventario """
    db.delete(conteo)
    db.commit()
    return {"mensaje": "Conteo de inventario eliminado exitosamente"}
