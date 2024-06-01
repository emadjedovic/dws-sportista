from datetime import datetime, timedelta
import bcrypt
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Union
from jose import JWTError, jwt

import models, schemas
from dependencies import get_db

router = APIRouter()

# Secret key i algoritam za JWT token
SECRET_KEY = "28ce7ef416bc95f20ad945201344226bd03aaeee7d734fa4d2ce0d14ce2a2084"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 nosilac lozinke za token autentifikaciju
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Funkcija za dekodiranje tokena i dobijanje trenutnog korisnika
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )

        # Provjera je li korisnik ili vlasnik
        if role == "korisnik":
            user = db.query(models.Korisnik).filter(models.Korisnik.username == username).first()
        elif role == "vlasnik":
            user = db.query(models.Vlasnik).filter(models.Vlasnik.username == username).first()
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )

        if user:
            return {"user":user, "role":role}
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

# Trenutni korisnik
@router.get("/users/me")
async def read_users_me(current_user: Union[schemas.KorisnikRead, schemas.VlasnikRead] = Depends(get_current_user)):
    return current_user

#Funkcija za kreiranje JWT pristupnog tokena
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Registracija korisnika ili vlasnika
@router.post("/register", response_model=Union[schemas.KorisnikRead, schemas.VlasnikRead])
def register_user_or_owner(
    user_data: Union[schemas.KorisnikCreate, schemas.VlasnikCreate],
    db: Session = Depends(get_db)
):
    if isinstance(user_data, schemas.KorisnikCreate):
         return register_korisnik(user_data, db)
    elif isinstance(user_data, schemas.VlasnikCreate):
        return register_vlasnik(user_data, db)


# Funkcija za registraciju korisnika
def register_korisnik(korisnik_data: schemas.KorisnikCreate, db: Session):
    # Provjera da li je username zauzet
    existing_user = (
        db.query(models.Korisnik)
        .filter(models.Korisnik.username == korisnik_data.username)
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
        .filter(models.Korisnik.email == korisnik_data.email)
        .first()
    )
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    # Hash-ovanje sifre
    hashed_password = bcrypt.hashpw(
        korisnik_data.password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    # Kreiranje novog korisnika
    novi_korisnik = models.Korisnik(
        username=korisnik_data.username,
        email=korisnik_data.email,
        ime=korisnik_data.ime,
        prezime=korisnik_data.prezime,
        datum_rodjenja=korisnik_data.datum_rodjenja,
        lokacija=korisnik_data.lokacija,
        hashed_password=hashed_password,
        telefon = korisnik_data.telefon,
        disabled=False,
    )

    #Dodavanje sportova korisnika
    for sport in korisnik_data.sportovi:
        novi_korisnik.sportovi.append(models.KorisnikSport(sport_id=sport))

    #Dodavanje korisnika u bazu
    db.add(novi_korisnik)
    db.commit()
    db.refresh(novi_korisnik)

    access_token = create_access_token(data={"sub": novi_korisnik.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": novi_korisnik.email,
        "id": novi_korisnik.id,
        "is_active": not novi_korisnik.disabled,
    }


# Funkcija za registraciju vlasnika
def register_vlasnik(vlasnik_data: schemas.VlasnikCreate, db: Session):
    #Provjera da li je username zauzet
    existing_user = (
        db.query(models.Vlasnik)
        .filter(models.Vlasnik.username == vlasnik_data.username)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Provjera da li je email vec registrovan
    existing_email = (
        db.query(models.Vlasnik)
        .filter(models.Vlasnik.email == vlasnik_data.email)
        .first()
    )
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    # Hash-ovanje sifre
    hashed_password = bcrypt.hashpw(
        vlasnik_data.password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    # Kreiranje novog vlasnika
    novi_vlasnik = models.Vlasnik(
        password=hashed_password,
        username = vlasnik_data.username,
        ime=vlasnik_data.ime,
        prezime=vlasnik_data.prezime,
        datum_rodjenja=vlasnik_data.datum_rodjenja,
        lokacija=vlasnik_data.lokacija,
        email=vlasnik_data.email,
        telefon=vlasnik_data.telefon,
    )

    # Dodavanje vlasnika u bazu
    db.add(novi_vlasnik)
    db.commit()
    db.refresh(novi_vlasnik)

    access_token = create_access_token(data={"sub": novi_vlasnik.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": novi_vlasnik.email,
        "id": novi_vlasnik.id,
        "is_active": True,  
    }




@router.post("/token", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Provjera da li je korisnik
    user = (
        db.query(models.Korisnik)
        .filter(models.Korisnik.username == form_data.username)
        .first()
    )
    if user and bcrypt.checkpw(form_data.password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        access_token = create_access_token(data={"sub": user.username, "role": "korisnik"})
        return {"access_token": access_token, "token_type": "bearer"}

    # Provjera da li je vlasnik
    vlasnik = (
        db.query(models.Vlasnik)
        .filter(models.Vlasnik.username == form_data.username)
        .first()
    )
    if vlasnik and bcrypt.checkpw(form_data.password.encode("utf-8"), vlasnik.password.encode("utf-8")):
        access_token = create_access_token(data={"sub": vlasnik.username, "role": "vlasnik"})
        return {"access_token": access_token, "token_type": "bearer"}

    # Ako nije korisnik niti vlasnik 
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect username or password",
    )
