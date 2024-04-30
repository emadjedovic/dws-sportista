from datetime import datetime, timedelta
import bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from requests import Session
from jose import jwt, JWTError

from backend import models, schemas
from ..dependencies import get_db


router = APIRouter()


# Secret key i algoritam za JWT token
SECRET_KEY = "neki-tajni-kljuc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 nosilac lozinke za token autentifikaciju
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


@router.get("/items/", tags=["items"])
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.post("/register", response_model=schemas.Korisnik)
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
    ).decode("utf-8")

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

    # Dodavanje sportova korisnika
    for sport in user_data.sportovi:
        new_user.sportovi.append(models.KorisnikSport(sport_id=sport))

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
@router.post("/token", response_model=schemas.Token)
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