from typing import List

from fastapi import Depends, HTTPException, APIRouter
from requests import Session

import models, schemas
from dependencies import get_db


router = APIRouter()


@router.get("/vlasnici", response_model=List[schemas.VlasnikRead])
def get_vlasnici_list(db: Session = Depends(get_db)):
    vlasnici_list = db.query(models.Vlasnik).all()

    if vlasnici_list:
        for vlasnik in vlasnici_list:
            print(vlasnik)
        return vlasnici_list
    else:
        raise HTTPException(status_code=404, detail="Not found")