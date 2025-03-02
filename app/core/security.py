"""
security.py

Este módulo gestiona la seguridad de la aplicación, incluyendo:
- Hashing y verificación de contraseñas utilizando bcrypt.
- Creación y validación de tokens JWT para autenticación de usuarios.

Funciones principales:
- verify_password: Verifica si una contraseña coincide con su hash almacenado.
- get_password_hash: Genera un hash seguro para una contraseña.
- create_access_token: Crea un token JWT de acceso con datos específicos y tiempo de expiración.
- decode_access_token: Decodifica y valida un token JWT.

¡IMPORTANTE! Asegúrate de mantener la SECRET_KEY segura y privada en un entorno de producción.
"""

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status

# Contexto de hashing para contraseñas con Bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# =====================================
# CONFIGURACIÓN DE JWT Y OAUTH2
# =====================================

SECRET_KEY = "kafklajf<<<<>><><&&&@@afaf__9o9n009n"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# =====================================
# FUNCIONES DE GESTIÓN DE CONTRASEÑAS
# =====================================

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash almacenado.

    Args:
        plain_password (str): La contraseña en texto plano proporcionada por el usuario.
        hashed_password (str): El hash almacenado de la contraseña.

    Returns:
        bool: True si las contraseñas coinciden, False en caso contrario.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Genera un hash seguro para una contraseña.

    Args:
        password (str): La contraseña en texto plano.

    Returns:
        str: Hash seguro de la contraseña.
    """
    return pwd_context.hash(password)


# =====================================
# FUNCIONES DE MANEJO DE TOKENS JWT
# =====================================

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Crea un token JWT de acceso con datos específicos y tiempo de expiración.

    Args:
        data (dict): Información a codificar en el token (ej: {"sub": username}).
        expires_delta (timedelta, opcional): Tiempo de expiración del token. 
                                             Si no se proporciona, expira en 15 minutos.

    Returns:
        str: Token JWT codificado.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.time() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Decodifica y valida un token JWT.

    Args:
        token (str): El token JWT a decodificar.

    Returns:
        dict: Los datos contenidos en el token si es válido.

    Raises:
        HTTPException: Si el token no es válido o ha expirado.
    """
    try:
        # Decodificar el token con la clave secreta y el algoritmo especificado
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Obtener el "sub" (subject) del token, normalmente el nombre de usuario
        username: str = payload.get("sub")
        
        # Verificar si el token contiene un "sub" válido
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudieron validar las credenciales.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    
    except JWTError:
        # Si hay un error en la decodificación, el token es inválido
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar las credenciales.",
            headers={"WWW-Authenticate": "Bearer"},
        )
