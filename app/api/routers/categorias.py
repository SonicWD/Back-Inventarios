"""
Este módulo define las rutas (endpoints) para la gestión de categorías.

Utiliza FastAPI APIRouter para organizar los endpoints relacionados con categorías,
incluyendo operaciones CRUD: obtener, crear, actualizar y eliminar categorías.
Delegando la lógica de negocio al servicio correspondiente.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.categorias_schema import Categoria, CrearCategoria, TipoCategoria
from app.core.config import get_db
from app.services.categorias_service import CategoriaService

router = APIRouter(
    prefix="/categorias",
    tags=["categorías"],
    responses={404: {"description": "No encontrado"}}
)


def get_categoria_service(db: Session = Depends(get_db)):
    """
    Dependencia para obtener una instancia de CategoriaService.

    Args:
        db (Session): Sesión de base de datos inyectada.

    Returns:
        CategoriaService: Instancia del servicio de categorías.
    """
    return CategoriaService(db)


@router.get("/", response_model=List[Categoria])
def obtener_categorias(
    skip: int = 0,
    limit: int = 100,
    tipo: TipoCategoria = None,
    categoria_service: CategoriaService = Depends(get_categoria_service)
):
    """
    Obtener todas las categorías con paginación y filtro opcional por tipo.

    Args:
        skip (int): Número de registros a omitir (paginación).
        limit (int): Límite de registros a obtener.
        tipo (schemas.TipoCategoria): Filtro opcional por tipo de categoría.
        categoria_service (CategoriaService): Servicio de categorías inyectado.

    Returns:
        List[schemas.Categoria]: Lista de categorías.
    """
    return categoria_service.obtener_todas(skip, limit, tipo)


@router.get("/{categoria_id}", response_model=Categoria)
def obtener_categoria(
    categoria_id: int,
    categoria_service: CategoriaService = Depends(get_categoria_service)
):
    """
    Obtener una categoría por su ID.

    Args:
        categoria_id (int): ID de la categoría a obtener.
        categoria_service (CategoriaService): Servicio de categorías inyectado.

    Returns:
        schemas.Categoria: Detalles de la categoría solicitada.

    Raises:
        HTTPException: Si no se encuentra la categoría.
    """
    categoria = categoria_service.obtener_por_id(categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@router.post("/", response_model=Categoria)
def crear_categoria(
    categoria: CrearCategoria,
    categoria_service: CategoriaService = Depends(get_categoria_service)
):
    """
    Crear una nueva categoría.

    Args:
        categoria (schemas.CrearCategoria): Datos de la nueva categoría.
        categoria_service (CategoriaService): Servicio de categorías inyectado.

    Returns:
        schemas.Categoria: Categoría creada.
    """
    return categoria_service.crear(categoria)


@router.put("/{categoria_id}", response_model=Categoria)
def actualizar_categoria(
    categoria_id: int,
    categoria: CrearCategoria,
    categoria_service: CategoriaService = Depends(get_categoria_service)
):
    """
    Actualizar una categoría existente.

    Args:
        categoria_id (int): ID de la categoría a actualizar.
        categoria (schemas.CrearCategoria): Datos actualizados de la categoría.
        categoria_service (CategoriaService): Servicio de categorías inyectado.

    Returns:
        schemas.Categoria: Categoría actualizada.
    """
    return categoria_service.actualizar(categoria_id, categoria)


@router.delete("/{categoria_id}")
def eliminar_categoria(
    categoria_id: int,
    categoria_service: CategoriaService = Depends(get_categoria_service)
):
    """
    Eliminar una categoría por su ID.

    Args:
        categoria_id (int): ID de la categoría a eliminar.
        categoria_service (CategoriaService): Servicio de categorías inyectado.

    Returns:
        dict: Mensaje de éxito.
    """
    categoria_service.eliminar(categoria_id)
    return {"mensaje": "Categoría eliminada exitosamente"}
