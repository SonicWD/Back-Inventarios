from fastapi import APIRouter
from .categorias import router as categorias_router
from .items import router as items_router
from .items_proveedor import router as items_proveedor_router
from .proveedores import router as proveedores_router
from .movimientos_inventario import router as movimientos_inventario_router
from .almacenes import router as almacenes_router
# Crear el enrutador principal
router = APIRouter()

# Incluir los routers de las categorías e items
router.include_router(categorias_router)
router.include_router(items_router)
router.include_router(items_proveedor_router)
router.include_router(proveedores_router)
router.include_router(movimientos_inventario_router)
router.include_router(almacenes_router)