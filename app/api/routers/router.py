from fastapi import APIRouter
from .categorias import router as categorias_router
from .producto import router as productos_router
from .producto_proveedor import router as productos_proveedor_router
from .proveedores import router as proveedores_router
from .movimientos_inventario import router as movimientos_inventario_router
from .almacenes import router as almacenes_router
from .conteos_inventario import router as conteos_inventario_router
from .user import router as users_router
from .home import router as home_router


# Crear el enrutador principal
router = APIRouter()

# Incluir los routers de las categorías e productos
router.include_router(categorias_router)
router.include_router(productos_router)
router.include_router(productos_proveedor_router)
router.include_router(proveedores_router)
router.include_router(movimientos_inventario_router)
router.include_router(almacenes_router)
router.include_router(conteos_inventario_router)
router.include_router(users_router)
router.include_router(home_router)