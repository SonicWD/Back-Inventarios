from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import signal
import sys

from routers.router import router as main_router
from database.database import engine, Base
from utils.security import ALGORITHM, SECRET_KEY
from routers.middelware import AuthMiddleware


app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(AuthMiddleware, secret_key=SECRET_KEY, algorithm=ALGORITHM)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir el enrutador principal
app.include_router(main_router)

# Definir el manejador de señales
def receive_signal(signalNumber, frame):
    print('Received signal:', signalNumber)
    sys.exit(0)

# Configurar los manejadores de señales
signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGTERM, receive_signal)

@app.get("/")
def read_root():
    return {"Hola": "Mundo, por favo entrar a /docs# pofavo"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
