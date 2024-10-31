from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from database.database import Base


# Modelo de Almacenamiento (Almacen)
class Almacen(Base):
    __tablename__ = "almacenes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    rango_temperatura = Column(String, nullable=True)
    capacidad = Column(Float, nullable=False)
    uso_actual = Column(Float, nullable=False, default=0)

    # Relación con conteo de inventario
    conteos_inventario = relationship("ConteoInventario", back_populates="almacen")
