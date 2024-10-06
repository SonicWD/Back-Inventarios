from fastapi import FastAPI
from .routers import categories, items, inventory
from .database import init_db 

app = FastAPI(
    title="Sistema de Inventario Restaurante",
    description="API para gestionar el inventario de un restaurante",
    version="1.0.0"
)

# Inicializar la base de datos
init_db()

# Incluir los routers
app.include_router(categories.router)
app.include_router(items.router)
app.include_router(inventory.router)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido al sistema de inventario del restaurante",
        "docs": "/docs"
    }