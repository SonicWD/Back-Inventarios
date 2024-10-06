from fastapi import APIRouter
from .categorias import router as categorias_router
from .items import router as items_router

# Crear el enrutador principal
router = APIRouter()

# Incluir los routers de las categorías e items
router.include_router(categorias_router)
router.include_router(items_router)
