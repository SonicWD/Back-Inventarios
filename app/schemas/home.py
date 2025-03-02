"""
home_schema.py

Este módulo define el esquema utilizado para la visualización de información general en la página de inicio de la aplicación.

Esquema:
- HomeInfo: Estructura que agrupa la información estadística de productos, proveedores, almacenes e inventario.

Atributos:
- productos (int): Cantidad total de productos registrados en el sistema.
- proveedores (int): Número de proveedores asociados a los productos.
- almacenes (int): Total de almacenes disponibles.
- inventario (int): Suma total de inventario disponible en todos los almacenes.

Este esquema se utiliza para presentar un resumen estadístico en el dashboard o página de inicio,
ofreciendo una visión general del estado actual del inventario.
"""

# productos, proveedores, almacenes e invesntaiors
from pydantic import BaseModel

class HomeInfo(BaseModel):
    productos: int
    proveedores: int
    almacenes: int
    inventario: int