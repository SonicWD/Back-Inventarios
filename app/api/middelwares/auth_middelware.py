"""
AuthMiddleware:
Verifica la autenticidad del token JWT en los headers Authorization.
Excluye rutas específicas (login y docs) y pasa la información
del usuario autenticado al request.
"""

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException, Request, status
from app.core.security import decode_access_token
from jose import JWTError

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, secret_key, algorithm):
        """
        Inicializa el middleware con la clave secreta y el algoritmo de decodificación.
        """
        super().__init__(app)
        self.secret_key = secret_key
        self.algorithm = algorithm

    async def dispatch(self, request: Request, call_next):
        """
        Procesa cada solicitud HTTP para verificar el token de autenticación.
        Excluye rutas específicas y pasa la información del usuario autenticado al request.
        """
        rutas_excluidas = ["/users/login", "/docs", "/openapi.json"]
        if request.method == "OPTIONS" or any(request.url.path.startswith(ruta) for ruta in rutas_excluidas):
            return await call_next(request)

        token = request.headers.get("Authorization")
        
        if not token or not token.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No autorizado",
                headers={"WWW-Authenticate": "Bearer"}
            )

        token = token.split(" ")[1]
        
        try:
            payload = decode_access_token(token)
            request.state.user = payload.get("sub")
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado",
                headers={"WWW-Authenticate": "Bearer"}
            )

        response = await call_next(request)
        return response
