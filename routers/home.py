from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.schemas.home import HomeInfo
from database.database import get_db
from database.models.proveedor_model import Proveedor
from database.models.item_model import Item
from database.models.almacen_model import Almacen
from database.models.conteo_model import ConteoInventario


router = APIRouter(
    prefix="/home",
    tags=["home"],
)

@router.get("/", response_model=HomeInfo)
def obtener_info_home(db: Session = Depends(get_db)):
    productos_count = db.query(Item).count()
    proveedores_count = db.query(Proveedor).count()
    almacenes_count = db.query(Almacen).count()
    inventario_count = db.query(ConteoInventario).count()

    return HomeInfo(
        productos=productos_count,
        proveedores=proveedores_count,
        almacenes=almacenes_count,
        inventario=inventario_count
    )