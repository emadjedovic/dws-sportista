from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from starlette.middleware.cors import CORSMiddleware

from .database import SessionLocal, engine
from . import models
from . import schemas

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

# Secret key i algoritam za JWT token
SECRET_KEY = "neki-tajni-kljuc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 nosilac lozinke za token autentifikaciju
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

models.Base.metadata.create_all(bind=engine)

# Dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

##Funkcija za kreiranje JWT pristupnog tokena
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#Funkcija za dekodiranje i provjeru JWT tokena
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


@app.get("/items/", tags=["items"])
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.post("/register", response_model=schemas.Korisnik)
def register_user(user_data: schemas.KorisnikCreate, db: Session = Depends(get_db)):
    # Provjera da li je username zauzet
    existing_user = db.query(models.Korisnik).filter(models.Korisnik.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    # Provjera da li je email vec registrovan
    existing_email = db.query(models.Korisnik).filter(models.Korisnik.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Hash-ovanje sifre
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Kreiranje novog korisnika
    new_user = models.Korisnik(username=user_data.username,
                                email=user_data.email,
                                ime=user_data.ime,
                                prezime=user_data.prezime,
                                datum_rodjenja=user_data.datum_rodjenja,
                                lokacija=user_data.lokacija,
                                hashed_password=hashed_password,
                                disabled=False)

    # Dodavanje korisnika u bazu
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer", "email": new_user.email, "id": new_user.id, "is_active": not new_user.disabled}


# Login endpoint
@app.post("/token", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Korisnik).filter(models.Korisnik.username == form_data.username).first()
    if not user or not bcrypt.checkpw(form_data.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}



