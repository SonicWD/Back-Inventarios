# productos, proveedores, almacenes e invesntaiors
from pydantic import BaseModel

class HomeInfo(BaseModel):
    productos: int
    proveedores: int
    almacenes: int
    inventario: int