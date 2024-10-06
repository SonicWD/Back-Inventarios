import uvicorn
from fastapi import FastAPI
from routers.router import router as main_router
from database.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import signal
import sys

app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

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
    return {"Hola": "Mundo"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
