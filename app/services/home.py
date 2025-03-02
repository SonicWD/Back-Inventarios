"""
Este módulo contiene la lógica de negocio para obtener estadísticas de la página de inicio.

Incluye funciones para:
- Obtener el conteo de productos.
- Obtener el conteo de proveedores.
- Obtener el conteo de almacenes.
- Obtener el conteo de inventario.
"""

from sqlalchemy.orm import Session
from app.schemas.home import HomeInfo
from app.repositories.home import (
    get_count_productos,
    get_count_proveedores,
    get_count_almacenes,
    get_count_inventario
)

def obtener_estadisticas_home(db: Session) -> HomeInfo:
    """
    Obtener estadísticas para la página de inicio.

    Incluye:
    - Total de productos.
    - Total de proveedores.
    - Total de almacenes.
    - Total de registros en inventario.

    Parámetros:
    - db (Session): Sesión de base de datos.

    Retorna:
    - HomeInfo: Objeto con las estadísticas generales.
    """
    productos_count = get_count_productos(db)
    proveedores_count = get_count_proveedores(db)
    almacenes_count = get_count_almacenes(db)
    inventario_count = get_count_inventario(db)

    return HomeInfo(
        productos=productos_count,
        proveedores=proveedores_count,
        almacenes=almacenes_count,
        inventario=inventario_count
    )
