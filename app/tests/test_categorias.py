import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_db, Base
from main import app
from app.models import models
from app.schemas import schemas

# Configuración para la base de datos de pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear todas las tablas en la base de datos de pruebas
Base.metadata.create_all(bind=engine)

# Crear una función para obtener la sesión de pruebas
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Fixture para crear una categoría de prueba
@pytest.fixture
def crear_categoria():
    categoria = models.Categoria(nombre="Test Category", tipo="Test Type")
    with TestingSessionLocal() as db:
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
    return categoria

# Prueba: Obtener todas las categorías
def test_obtener_categorias():
    response = client.get("/categorias/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Prueba: Obtener una categoría por ID
def test_obtener_categoria(crear_categoria):
    response = client.get(f"/categorias/{crear_categoria.id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Test Category"

# Prueba: Crear una nueva categoría
def test_crear_categoria():
    nueva_categoria = {"nombre": "Nueva Categoría", "tipo": "Nuevo Tipo"}
    response = client.post("/categorias/", json=nueva_categoria)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Nueva Categoría"

# Prueba: Actualizar una categoría existente
def test_actualizar_categoria(crear_categoria):
    categoria_actualizada = {"nombre": "Categoría Actualizada", "tipo": "Tipo Actualizado"}
    response = client.put(f"/categorias/{crear_categoria.id}", json=categoria_actualizada)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Categoría Actualizada"

# Prueba: Eliminar una categoría
def test_eliminar_categoria(crear_categoria):
    response = client.delete(f"/categorias/{crear_categoria.id}")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Categoría eliminada exitosamente"
    
    # Comprobar que la categoría ha sido eliminada
    response = client.get(f"/categorias/{crear_categoria.id}")
    assert response.status_code == 404
