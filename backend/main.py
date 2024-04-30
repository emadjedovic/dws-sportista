from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from .routers import auth, korisnik, vlasnik, sport

from .database import  engine
from . import models


def start_application():
    app = FastAPI()
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = start_application()


models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(korisnik.router)
app.include_router(vlasnik.router)
app.include_router(sport.router)

