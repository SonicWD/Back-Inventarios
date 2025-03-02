"""
Repositorio Usuario:
Encapsula la lógica de acceso a datos para los usuarios,
facilitando las operaciones CRUD con la base de datos.
"""

from sqlalchemy.orm import Session
from app.models.user_model import UserModel

def obtener_usuario_por_username(username: str, db: Session):
    """
    Obtiene un usuario por su nombre de usuario.
    """
    return db.query(UserModel).filter(UserModel.username == username).first()

def obtener_usuario_por_id(user_id: int, db: Session):
    """
    Obtiene un usuario por su ID.
    """
    return db.query(UserModel).filter(UserModel.id_user == user_id).first()

def crear_usuario(nuevo_usuario: UserModel, db: Session):
    """
    Crea un nuevo usuario.
    """
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def actualizar_usuario(db: Session, usuario_existente: UserModel, datos_actualizados: dict):
    """
    Actualiza un usuario existente con los datos proporcionados.
    """
    for key, value in datos_actualizados.productos():
        setattr(usuario_existente, key, value)
    
    db.commit()
    db.refresh(usuario_existente)
    return usuario_existente

def eliminar_usuario(usuario: UserModel, db: Session):
    """
    Elimina un usuario existente.
    """
    db.delete(usuario)
    db.commit()
