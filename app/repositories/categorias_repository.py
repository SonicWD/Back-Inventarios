"""
Este módulo gestiona las operaciones de base de datos para las categorías.

Define el repositorio CategoriaRepository, encargado de interactuar directamente
con la base de datos para realizar operaciones CRUD sobre el modelo Categoria.
"""

from sqlalchemy.orm import Session
from app.models.categoria_model import Categoria


class CategoriaRepository:
    """
    Repositorio para operaciones de base de datos sobre categorías.
    """

    def __init__(self, db: Session):
        """Constructor del repositorio de categorías."""
        self.db = db

    def obtener_todas(self, skip=0, limit=100, tipo=None):
        """Obtener todas las categorías con filtro opcional por tipo."""
        query = self.db.query(Categoria)
        if tipo:
            query = query.filter(Categoria.tipo == tipo)
        return query.offset(skip).limit(limit).all()

    def obtener_por_id(self, categoria_id: int):
        """Obtener una categoría por su ID."""
        return self.db.query(Categoria).filter(Categoria.id == categoria_id).first()

    def crear(self, categoria):
        """Crear una nueva categoría."""
        db_categoria = Categoria(**categoria.model_dump())
        self.db.add(db_categoria)
        self.db.commit()
        self.db.refresh(db_categoria)
        return db_categoria

    def actualizar(self, categoria):
        """Actualizar una categoría existente."""
        self.db.commit()
        self.db.refresh(categoria)
        return categoria

    def eliminar(self, categoria):
        """Eliminar una categoría por su ID."""
        self.db.delete(categoria)
        self.db.commit()
