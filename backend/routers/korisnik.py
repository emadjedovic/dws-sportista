from typing import List

from fastapi import Depends, HTTPException, APIRouter
from pydantic import EmailStr
from requests import Session

import models, schemas
from dependencies import get_db


router = APIRouter()


@router.get("/korisnici", response_model=List[schemas.KorisnikRead])
def get_korisnici_list(db: Session = Depends(get_db)):
    korisnici_list = db.query(models.Korisnik).all()

    if korisnici_list:
        for korisnik in korisnici_list:
            print(korisnik)
        return korisnici_list
    else:
        raise HTTPException(status_code=404, detail="Not found")
   
#@router.get("/korisnik/{id}")
#def get_korisnik_by_id(id: int, db: Session = Depends(get_db)):
#
#    korisnik = db.query(models.Korisnik).filter(models.Korisnik.id == id).first()
#   if not korisnik:
#       raise HTTPException(status_code=404, detail="Not found")
#
#    return korisnik

@router.get("/korisnik/{username}")
def get_korisnik_by_username(u: str, db: Session = Depends(get_db)):

    korisnik = db.query(models.Korisnik).filter(models.Korisnik.username == u).first()
    if not korisnik:
        raise HTTPException(status_code=404, detail="Not found")

    return korisnik


# POMOCNE FUNKCIJE

def get_korisnici_email(e: EmailStr, db: Session = Depends(get_db)):

    korisnik = db.query(models.Korisnik).filter(models.Korisnik.id == e).first()
    if not korisnik:
        raise HTTPException(status_code=404, detail="Not found")

    return korisnik

def get_korisnici_ime(i: str, db: Session = Depends(get_db)):

    korisnici_lista = db.query(models.Korisnik).filter(models.Korisnik.ime == i)
    if not korisnici_lista:
        raise HTTPException(status_code=404, detail="Not found")

    return korisnici_lista

def get_korisnici_prezime(p: str, db: Session = Depends(get_db)):

    korisnici_lista = db.query(models.Korisnik).filter(models.Korisnik.prezime == p)
    if not korisnici_lista:
        raise HTTPException(status_code=404, detail="Not found")

    return korisnici_lista