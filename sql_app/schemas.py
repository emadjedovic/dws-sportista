from typing import Optional
from pydantic import BaseModel
from datetime import datetime
"""
1Bazne klase1 sadrze sve podatke
Nasljedju BaseModel
"""
class KorisnikBase(BaseModel):

    sifra: str
    ime: str
    prezime: str
    datum_rodenja: datetime
    lokacija: str
    mail: str
    telefon:str

class VlasnikBase(BaseModel):

    sifra: str
    ime: str
    prezime: str
    datum_rodenja: datetime
    lokacija: str
    mail: str
    telefon:str   

    # 1:N rel

class SportBase(BaseModel):

    naziv: str
    # 1:1 rel

class TerenBase(BaseModel):

    vlasnik_id: int
    sport_id: int
    ocjene_id: int
    vrsta: str
    lokacija: str
    cijena: str
    # 1:N
    # 1:1
    # 1:1
    # 1:N

class OcjeneBase(BaseModel):

    korisnik_id: int
    teren_id: int
    ocjena: int

    # 1:1

class TerminBase(BaseModel):

    teren_id: int
    tim_id: int
    vrijeme_pocetka: datetime
    vrijeme_kraja: datetime
    je_li_privatni: bool

    # 1:N
    # 1:N

class TimBase(BaseModel):
    
    sport_id: int
    termin_id: int
    broj_igraca: int
    nivo_vjestine: int
    lokacija_tima: str
    broj_slobodnih_mjesta: int

    # 1:N

class KorisnikTimBase(BaseModel):

    korisnik_id: int
    tim_id: int

"""
Za citanje, nasljeduju klase tipa BaseModel
Sadrze id, relationship atribute i config
"""

class KorisnikRead(KorisnikBase):

    id: int

    class Config:
        orm_mode = True

class VlasnikRead(VlasnikBase):

    id: int    #RELACIJA PROBLEM
    tereni = Optional[TerenRead] = None

    class Config: 
        orm_mode = True

class SportRead(SportBase):

    id: int     #RELACIJA PROBLEM
    teren: Optional[TerenRead] = None

    class Config:
        orm_mode = True

class TerenRead(TerenBase):

    id: int  #RELACIJA PROBLEM?, STA CE BITI VlasnikRead, SportRead
    vlasnik: Optional[VlasnikRead] = None
    sport: Optional[SportRead]= None
    ocjene: Optional[Ocjene]= None
    termini: Optional[Termin]= None

    class Config:
        orm_mode = True

class OcjeneRead(OcjeneBase):

    id: int
    teren: Optional[TerenRead] = None

    class Config:
        orm_mode = True

class TerminRead(TerminBase):

    id: int  #RELACIJA PROBLEM?
    teren: Optional[TerenRead] = None  
    tim: Optional[TimRead] = None 

    class Config:
        orm_mode = True

class TimRead(TimBase):

    id: int
    termini: Optional[TerminRead] = None

    class Config:
        orm_mode = True

class KorisnikTimRead(KorisnikTimBase):

    id: int

    class Config:
        orm_mode = True

"""
Klase za kreiranje podataka, 
nasljeduje BaseModel klase 1
"""

class KorisnikCreate(KorisnikBase):
    pass 

class VlasnikCreate(VlasnikBase):
    pass

class SportCreate(SportBase):
    pass

class TerenCreate(TerenBase):
    pass

class OcjeneCreate(OcjeneBase):
    pass

class TerminCreate(TerminBase):
    pass

class TimCreate(TimBase):
    pass

class KorisnikTimCreate(KorisnikTimBase):
    pass