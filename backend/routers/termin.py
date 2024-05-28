from fastapi import APIRouter
from dependencies import get_db

router = APIRouter()

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, database

app = FastAPI()


@router.post("/termini/", response_model=schemas.TerminCreate)
def create_termin(termin: schemas.TerminCreate, db: Session = Depends(get_db)):
    db_termin = models.Termin(
        teren_id=termin.teren_id,
        tim_id=termin.tim_id,
        vrijeme_pocetka=termin.vrijeme_pocetka,
        vrijeme_kraja=termin.vrijeme_kraja,
        je_li_privatni=termin.je_li_privatni,
        #broj_slobodnih_mjesta=termin.broj_slobodnih_mjesta,
        potreban_broj_igraca=termin.potreban_broj_igraca,
        max_broj_igraca=termin.max_broj_igraca,
        nivo_vjestine=termin.nivo_vjestine,
        lokacija_tima=termin.lokacija_tima
    )
    db.add(db_termin)
    db.commit()
    db.refresh(db_termin)
    return db_termin

