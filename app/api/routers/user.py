"""
Router Usuario:
Gestiona las rutas para la creación, consulta, 
actualización, eliminación y autenticación de usuarios.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user_schemas import UserCreate, UserUpdate, UserOut, LoginUser
from app.core.config import get_db
from app.services import user_service as service
from fastapi.responses import JSONResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "No encontrado"}}
)

@router.get("/user-info", response_model=UserOut)
def get_user_info(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Obtiene la información del usuario autenticado.
    """
    payload = service.decode_access_token(token)
    username = payload.get("sub")
    return service.obtener_usuario_por_username(username, db)

@router.get('/{user_id}', response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Obtiene información de un usuario por ID.
    """
    return service.obtener_usuario_por_id(user_id, db)

@router.post('/', response_model=UserOut)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario (registro).
    """
    return service.crear_usuario(user, db)

@router.put('/{user_id}', response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Actualiza la información de un usuario.
    """
    return service.actualizar_usuario(user_id, user_update, db)

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario por su ID.
    """
    return service.eliminar_usuario(user_id, db)

@router.post("/login", response_model=dict)
def login(user: LoginUser, db: Session = Depends(get_db)):
    """
    Inicia sesión y obtiene tokens de acceso y refresco.
    """
    tokens = service.autenticar_usuario(user, db)
    response = JSONResponse(content=tokens)
    response.set_cookie(key="refresh_token", value=tokens['refresh_token'], httponly=True, secure=True)
    return response
