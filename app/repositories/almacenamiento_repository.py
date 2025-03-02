"""
Este módulo gestiona las operaciones de base de datos para los almacenes.

Define el repositorio AlmacenamientoRepository, encargado de interactuar directamente
con la base de datos para realizar operaciones CRUD sobre el modelo Almacen.
"""

from sqlalchemy.orm import Session
from app.models.almacen_model import Almacen


class AlmacenamientoRepository:
    """
    Repositorio para operaciones de base de datos sobre almacenes.
    """

    def __init__(self, db: Session):
        """
        Constructor del repositorio de almacenes.

        Args:
            db (Session): Sesión de base de datos inyectada.
        """
        self.db = db

    def obtener_todos(self, skip: int = 0, limit: int = 100):
        """Obtener todos los almacenes."""
        return self.db.query(Almacen).offset(skip).limit(limit).all()

    def obtener_por_id(self, storage_id: int):
        """Obtener un almacén por su ID."""
        return self.db.query(Almacen).filter(Almacen.id == storage_id).first()

    def crear(self, almacen):
        """Crear un nuevo almacén."""
        db_storage = Almacen(**almacen.model_dump())
        self.db.add(db_storage)
        self.db.commit()
        self.db.refresh(db_storage)
        return db_storage

    def actualizar(self, almacen):
        """Actualizar un almacén existente."""
        self.db.commit()
        self.db.refresh(almacen)
        return almacen

    def eliminar(self, almacen):
        """Eliminar un almacén por su ID."""
        self.db.delete(almacen)
        self.db.commit()
