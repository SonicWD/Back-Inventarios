"""
Este módulo define la ruta para obtener información resumida para la página de inicio.

Incluye un endpoint para:
- Obtener estadísticas generales sobre productos, proveedores, almacenes e inventario.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.home import HomeInfo
from app.core.config import get_db
from app.services.home import obtener_estadisticas_home

router = APIRouter(
    prefix="/home",
    tags=["home"],
)

@router.get("/", response_model=HomeInfo)
def obtener_info_home(db: Session = Depends(get_db)):
    """
    Obtener estadísticas para la página de inicio.

    Parámetros:
    - db (Session): Sesión de base de datos inyectada con Depends.

    Retorna:
    - HomeInfo: Objeto con el conteo de productos, proveedores, almacenes e inventario.
    """
    return obtener_estadisticas_home(db)
