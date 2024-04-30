from typing import Annotated, List

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from starlette.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models
import schemas


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


# Funkcija za dekodiranje i provjeru JWT tokena
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
    existing_user = (
        db.query(models.Korisnik)
        .filter(models.Korisnik.username == user_data.username)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Provjera da li je email vec registrovan
    existing_email = (
        db.query(models.Korisnik)
        .filter(models.Korisnik.email == user_data.email)
        .first()
    )
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    # Hash-ovanje sifre
    hashed_password = bcrypt.hashpw(
        user_data.password.encode("utf-8"), bcrypt.gensalt()
    ).encode("utf-8")

    # Kreiranje novog korisnika
    new_user = models.Korisnik(
        username=user_data.username,
        email=user_data.email,
        ime=user_data.ime,
        prezime=user_data.prezime,
        datum_rodjenja=user_data.datum_rodjenja,
        lokacija=user_data.lokacija,
        hashed_password=hashed_password,
        disabled=False,
    )

    # Dodavanje korisnika u bazu
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": new_user.email,
        "id": new_user.id,
        "is_active": not new_user.disabled,
    }


# Login endpoint
@app.post("/token", response_model=schemas.Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = (
        db.query(models.Korisnik)
        .filter(models.Korisnik.username == form_data.username)
        .first()
    )
    if not user or not bcrypt.checkpw(
        form_data.password.encode("utf-8"), user.hashed_password.encode("utf-8")
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# GET

@app.get("/korisnici", response_model=List[schemas.KorisnikRead])
def get_korisnici_list(db: Session = Depends(get_db)):
    korisnici_list = db.query(models.Korisnik).all()

    if korisnici_list:
        for korisnik in korisnici_list:
            print(korisnik)
        return korisnici_list
    else:
        raise HTTPException(status_code=404, detail="Not found")
    
@app.get("/korisnik/{id}")
def get_korisnik_by_id(id: int, db: Session = Depends(get_db)):

    korisnik = db.query(models.Korisnik).filter(models.Korisnik.id == id).first()
    if not korisnik:
        raise HTTPException(status_code=404, detail="Not found")

    return korisnik
    
@app.get("/vlasnici", response_model=List[schemas.VlasnikRead])
def get_vlasnici_list(db: Session = Depends(get_db)):
    vlasnici_list = db.query(models.Vlasnik).all()

    if vlasnici_list:
        for vlasnik in vlasnici_list:
            print(vlasnik)
        return vlasnici_list
    else:
        raise HTTPException(status_code=404, detail="Not found")

@app.get("/tereni", response_model=List[schemas.TerenRead])
def get_tereni_list(db: Session = Depends(get_db)):
    tereni_list = db.query(models.Teren).all()

    if tereni_list:
        for teren in tereni_list:
            print(teren)
        return tereni_list
    else:
        raise HTTPException(status_code=404, detail="Not found")
    
@app.get("/termini", response_model=List[schemas.TerminRead])
def get_termini_list(db: Session = Depends(get_db)):
    termini_list = db.query(models.Termin).all()

    if termini_list:
        for termin in termini_list:
            print(termin)
        return termini_list
    else:
        raise HTTPException(status_code=404, detail="Not found")
    
@app.get("/timovi", response_model=List[schemas.TimRead])
def get_timovi_list(db: Session = Depends(get_db)):
    timovi_list = db.query(models.Tim).all()

    if timovi_list:
        for tim in timovi_list:
            print(tim)
        return timovi_list
    else:
        raise HTTPException(status_code=404, detail="Not found")