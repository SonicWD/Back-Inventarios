from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import signal
import sys

from app.api.routers.router import router as main_router
from app.core.config import engine, Base
from app.core.security import ALGORITHM, SECRET_KEY
from app.api.middelwares.auth_middelware import AuthMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(AuthMiddleware, secret_key=SECRET_KEY, algorithm=ALGORITHM)

Base.metadata.create_all(bind=engine)

app.include_router(main_router)

def receive_signal(signalNumber, frame):
    print('Received signal:', signalNumber)
    sys.exit(0)

signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGTERM, receive_signal)
