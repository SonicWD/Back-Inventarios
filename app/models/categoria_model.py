"""
categoria_model.py

Este módulo define el modelo de datos para las categorías de productos en la aplicación de inventarios.

Enumeraciones:
- TipoCategoriaEnum: Define los diferentes tipos de categorías disponibles para los productos.
  - INGREDIENTE, BEBIDA, UTENSILIO, MOBILIARIO, LIMPIEZA, OFICINA, PICNIC, DECORACION, UNIFORME.
- TipoPerecibleEnum: Indica si un producto es perecedero o no.
  - PERECEDERO, NO_PERECEDERO.

Modelo:
- Categoria: Representa una categoría de producto.

Atributos:
- id (int): Identificador único de la categoría.
- nombre (str): Nombre de la categoría.
- tipo (TipoCategoriaEnum): Tipo de categoría (por ejemplo, INGREDIENTE, BEBIDA, etc.).
- descripcion (str): Descripción adicional de la categoría (opcional).

Relaciones:
- productos: Relación con el modelo Producto para asociar productos pertenecientes a esta categoría.

Este modelo permite organizar y clasificar productos en diferentes categorías, mejorando la gestión del inventario.
"""

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.core.config import Base
import enum


# Definimos los tipos de enum que corresponden a las categorías y perecibilidad
class TipoCategoriaEnum(str, enum.Enum):
    INGREDIENTE = "INGREDIENTE"
    BEBIDA = "BEBIDA"
    UTENSILIO = "UTENSILIO"
    MOBILIARIO = "MOBILIARIO"
    LIMPIEZA = "LIMPIEZA"
    OFICINA = "OFICINA"
    PICNIC = "PICNIC"
    DECORACION = "DECORACION"
    UNIFORME = "UNIFORME"

class TipoPerecibleEnum(str, enum.Enum):
    PERECEDERO = "PERECEDERO"
    NO_PERECEDERO = "NO_PERECEDERO"


# Modelo de Categoría
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(Enum(TipoCategoriaEnum), nullable=False)
    descripcion = Column(String, nullable=True)

    # Relación con Productos
    productos = relationship("Producto", back_populates="categoria")