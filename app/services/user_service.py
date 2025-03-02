"""
Servicio Usuario:
Gestiona la lógica de negocio para los usuarios,
coordinando las operaciones con el repositorio.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta
from app.schemas.user_schemas import UserCreate, UserUpdate, LoginUser
from app.models.user_model import UserModel
from app.repositories import user_repository as repo
from app.core.security import (
    decode_access_token, 
    verify_password, 
    get_password_hash,
    create_access_token, 
    ACCESS_TOKEN_EXPIRE_MINUTES
)

def obtener_usuario_por_username(username: str, db: Session):
    """
    Obtiene un usuario por su nombre de usuario.
    Lanza una excepción si no se encuentra.
    """
    usuario = repo.obtener_usuario_por_username(username, db)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

def obtener_usuario_por_id(user_id: int, db: Session):
    """
    Obtiene un usuario por su ID.
    Lanza una excepción si no se encuentra.
    """
    usuario = repo.obtener_usuario_por_id(user_id, db)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

def crear_usuario(user: UserCreate, db: Session):
    """
    Crea un nuevo usuario.
    """
    hashed_password = get_password_hash(user.password)
    nuevo_usuario = UserModel(username=user.username, email=user.email, password=hashed_password)
    return repo.crear_usuario(nuevo_usuario, db)

def actualizar_usuario(user_id: int, user_update: UserUpdate, db: Session):
    """
    Actualiza un usuario existente.
    Lanza una excepción si no se encuentra.
    """
    usuario_existente = repo.obtener_usuario_por_id(user_id, db)
    if usuario_existente is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    datos_actualizados = user_update.dict(exclude_unset=True)
    if user_update.password:
        datos_actualizados['password'] = get_password_hash(user_update.password)

    return repo.actualizar_usuario(db, usuario_existente, datos_actualizados)

def eliminar_usuario(user_id: int, db: Session):
    """
    Elimina un usuario.
    Lanza una excepción si no se encuentra.
    """
    usuario_existente = repo.obtener_usuario_por_id(user_id, db)
    if usuario_existente is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    repo.eliminar_usuario(usuario_existente, db)
    return {"detail": "Usuario eliminado correctamente"}

def autenticar_usuario(user: LoginUser, db: Session):
    """
    Autentica a un usuario y genera tokens de acceso y refresco.
    """
    db_user = repo.obtener_usuario_por_username(user.username, db)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Nombre de usuario o contraseña incorrectos")

    # Crear el access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.username},
                                       expires_delta=access_token_expires)

    # Crear el refresh token
    refresh_token_expires = timedelta(days=7)
    refresh_token = create_access_token(data={"sub": db_user.username, "type": "refresh"},
                                        expires_delta=refresh_token_expires)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": refresh_token
    }
