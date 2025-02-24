from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException, Request
from jose import JWTError, jwt


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, secret_key, algorithm):
        super().__init__(app)
        self.secret_key = secret_key
        self.algorithm = algorithm


    async def dispatch(self, request: Request, call_next):
        # Excluir la ruta de login
        if request.url.path == "/users/login" or request.url.path == "/docs":
            return await call_next(request)

        # Obtener el token de los headers
        token = request.headers.get("Authorization")

        # Si no hay token, retornar 401
        if not token:
            # print("_____________---PATH---_____________(error)", request.url.path)
            raise HTTPException(status_code=401, detail="No autorizado")

        # Si hay token, continuar con la solicitud
        response = await call_next(request)
        return response
