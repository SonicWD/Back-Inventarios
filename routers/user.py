from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from database.database import get_db
from database.models.user_model import UserModel
from database.schemas.user_schemas import (UserCreate, UserUpdate, UserOut,
                                            LoginUser, Token)
from utils.security import (decode_access_token, verify_password, get_password_hash,
                            create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES,
                            SECRET_KEY, ALGORITHM)
from jose import JWTError, jwt
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/user-info", response_model=UserOut)
def get_user_info(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    username = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user



# Obtener información de usuario (por ID)
@router.get('/{user_id}', response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return user


# Crear nuevo usuario (registro)
@router.post('/', response_model=UserOut)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(username=user.username, email=user.email,
                        password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Actualizar usuario
@router.put('/{user_id}', response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate,
                db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")

    if user_update.username:
        user.username = user_update.username
    if user_update.email:
        user.email = user_update.email
    if user_update.password:
        user.password = get_password_hash(user_update.password)

    db.commit()
    db.refresh(user)
    return user


# Eliminar usuario
@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}


# Iniciar sesión y obtener token
@router.post("/login", response_model=dict)
def login(user: LoginUser, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")

    # Crear el access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.username},
                                       expires_delta=access_token_expires)

    # Crear el refresh token
    refresh_token_expires = timedelta(days=7)  # Mayor duración
    refresh_token = create_access_token(data={"sub": db_user.username, "type": "refresh"},
                                        expires_delta=refresh_token_expires)

    # Configurar el response con cookies para el refresh token
    response = JSONResponse(content={
        "access_token": access_token,
        "token_type": "bearer"
    })
    response.set_cookie(
        key="refresh_token", value=refresh_token, httponly=True, secure=True
    )

    return response
