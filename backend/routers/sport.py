from typing import List

from fastapi import Depends, HTTPException, APIRouter
from requests import Session

import models, schemas
from dependencies import get_db


router = APIRouter()


@router.get("/tereni", response_model=List[schemas.TerenRead])
def get_tereni_list(db: Session = Depends(get_db)):
    tereni_list = db.query(models.Teren).all()

    if tereni_list:
        for teren in tereni_list:
            print(teren)
        return tereni_list
    else:
        raise HTTPException(status_code=404, detail="Not found")
    
@router.get("/termini", response_model=List[schemas.TerminRead])
def get_termini_list(db: Session = Depends(get_db)):
    termini_list = db.query(models.Termin).all()

    if termini_list:
        for termin in termini_list:
            print(termin)
        return termini_list
    else:
        raise HTTPException(status_code=404, detail="Not found")
    
@router.get("/timovi", response_model=List[schemas.TimRead])
def get_timovi_list(db: Session = Depends(get_db)):
    timovi_list = db.query(models.Tim).all()

    if timovi_list:
        for tim in timovi_list:
            print(tim)
        return timovi_list
    else:
        raise HTTPException(status_code=404, detail="Not found")