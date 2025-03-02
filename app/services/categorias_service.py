"""
Este módulo contiene la lógica de negocio para la gestión de categorías.

Define el servicio CategoriaService, encargado de coordinar las operaciones
de CRUD utilizando el repositorio correspondiente y aplicando reglas de negocio.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.categorias_schema import CrearCategoria
from app.repositories.categorias_repository import CategoriaRepository


class CategoriaService:
    """
    Servicio de negocios para la gestión de categorías.
    """

    def __init__(self, db: Session):
        """
        Constructor del servicio de categorías.

        Args:
            db (Session): Sesión de base de datos inyectada.
        """
        self.db = db
        self.repo = CategoriaRepository(db)

    def obtener_todas(self, skip: int = 0, limit: int = 100, tipo=None):
        """Obtener todas las categorías con paginación y filtro opcional."""
        return self.repo.obtener_todas(skip, limit, tipo)

    def obtener_por_id(self, categoria_id: int):
        """Obtener una categoría por su ID."""
        categoria = self.repo.obtener_por_id(categoria_id)
        if categoria is None:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return categoria

    def crear(self, categoria: CrearCategoria):
        """Crear una nueva categoría."""
        return self.repo.crear(categoria)

    def actualizar(self, categoria_id: int, categoria: CrearCategoria):
        """Actualizar una categoría existente."""
        db_categoria = self.obtener_por_id(categoria_id)
        for key, value in categoria.model_dump().productos():
            setattr(db_categoria, key, value)
        return self.repo.actualizar(db_categoria)

    def eliminar(self, categoria_id: int):
        """Eliminar una categoría por su ID."""
        categoria = self.obtener_por_id(categoria_id)
        self.repo.eliminar(categoria)
