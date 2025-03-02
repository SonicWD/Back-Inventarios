"""
Este módulo gestiona las consultas a la base de datos para obtener estadísticas de la página de inicio.

Incluye funciones para:
- Obtener el conteo de productos.
- Obtener el conteo de proveedores.
- Obtener el conteo de almacenes.
- Obtener el conteo de registros de inventario.
"""

from sqlalchemy.orm import Session
from app.models.producto_model import Producto
from app.models.proveedor_model import Proveedor
from app.models.almacen_model import Almacen
from app.models.conteo_model import ConteoInventario


def get_count_productos(db: Session) -> int:
    """
    Obtener el total de productos registrados.
    
    Parámetros:
    - db (Session): Sesión de base de datos.
    
    Retorna:
    - int: Total de productos.
    """
    return db.query(Producto).count()

def get_count_proveedores(db: Session) -> int:
    """
    Obtener el total de proveedores registrados.
    
    Parámetros:
    - db (Session): Sesión de base de datos.
    
    Retorna:
    - int: Total de proveedores.
    """
    return db.query(Proveedor).count()

def get_count_almacenes(db: Session) -> int:
    """
    Obtener el total de almacenes registrados.
    
    Parámetros:
    - db (Session): Sesión de base de datos.
    
    Retorna:
    - int: Total de almacenes.
    """
    return db.query(Almacen).count()

def get_count_inventario(db: Session) -> int:
    """
    Obtener el total de registros en inventario.
    
    Parámetros:
    - db (Session): Sesión de base de datos.
    
    Retorna:
    - int: Total de registros de inventario.
    """
    return db.query(ConteoInventario).count()
