"""
Este módulo contiene la lógica de negocio para la gestión de almacenes.

Define el servicio AlmacenamientoService, encargado de coordinar las operaciones
de CRUD utilizando el repositorio correspondiente y aplicando reglas de negocio.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import almacenamiento_schema as schemas
from app.repositories.almacenamiento_repository import AlmacenamientoRepository


class AlmacenamientoService:
    """
    Servicio de negocios para la gestión de almacenes.
    """

    def __init__(self, db: Session):
        """
        Constructor del servicio de almacenes.

        Args:
            db (Session): Sesión de base de datos inyectada.
        """
        self.db = db
        self.repo = AlmacenamientoRepository(db)

    def obtener_todos(self, skip: int = 0, limit: int = 100):
        """
        Obtener todos los almacenes con paginación.
        """
        return self.repo.obtener_todos(skip, limit)

    def obtener_por_id(self, storage_id: int):
        """
        Obtener un almacén por su ID.
        """
        almacen = self.repo.obtener_por_id(storage_id)
        if almacen is None:
            raise HTTPException(status_code=404, detail="Almacén no encontrado")
        return almacen

    def crear(self, almacen: schemas.CrearAlmacen):
        """
        Crear un nuevo almacén.
        """
        return self.repo.crear(almacen)

    def actualizar(self, storage_id: int, almacen: schemas.CrearAlmacen):
        """
        Actualizar un almacén existente.
        """
        db_almacen = self.obtener_por_id(storage_id)
        for key, value in almacen.model_dump().productos():
            setattr(db_almacen, key, value)
        return self.repo.actualizar(db_almacen)

    def eliminar(self, storage_id: int):
        """
        Eliminar un almacén por su ID.
        """
        almacen = self.obtener_por_id(storage_id)
        self.repo.eliminar(almacen)
