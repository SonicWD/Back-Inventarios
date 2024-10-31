from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
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

    # Relación con Items
    items = relationship("Item", back_populates="categoria")