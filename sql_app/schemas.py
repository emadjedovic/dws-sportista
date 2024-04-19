from typing import Optional
from pydantic import BaseModel, EmailStr, Field, constr, validator
from datetime import datetime

"""
1Bazne klase1 sadrze sve podatke
Nasljedju BaseModel
"""

class KorisnikBase(BaseModel):

    sifra: str
    ime: str
    prezime: str
    datum_rodjenja: datetime
    lokacija: str
    mail: EmailStr
    telefon:str

class VlasnikBase(BaseModel):

    sifra: str
    ime: str
    prezime: str
    datum_rodjenja: datetime
    lokacija: str
    mail: EmailStr
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
    cijena: str #ili int??
    # 1:N
    # 1:1
    # 1:1
    # 1:N

class OcjeneBase(BaseModel):

    korisnik_id: int
    teren_id: int
    ocjena: int = Field(..., ge=0, le=5) # od 0 do 5

    # 1:1

class TerminBase(BaseModel):

    teren_id: int
    tim_id: int
    vrijeme_pocetka: datetime
    vrijeme_kraja: datetime
    je_li_privatni: bool

    @validator('vrijeme_kraja')
    def end_time_after_start_time(cls, v, values):
        if 'vrijeme_pocetka' in values and v <= values['vrijeme_pocetka']:
            raise ValueError('Vrijeme kraja mora biti nakon vremena početka.')
        return v

    # 1:N
    # 1:N

class TimBase(BaseModel):
    
    sport_id: int
    termin_id: int
    broj_igraca: int #je li ovo maksimalan broj igraca ili potreban broj igraca?
    nivo_vjestine: int = Field(..., ge=0, le=5) # od 0 do 5
    lokacija_tima: str
    broj_slobodnih_mjesta: int = Field(..., ge=0)

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
        from_attributes = True

class VlasnikRead(VlasnikBase):

    id: int    #RELACIJA PROBLEM
    # Mislim kako nemamo atribut za sve terene tog vlasnika da ne mozemo ni
    # ispisati sve njegove terene? To bismo mogli iz tabele Teren kao "select * gdje je vlasnik taj i taj..."
    # tereni = Optional[TerenRead] = None

    class Config: 
        from_attributes= True

class SportRead(SportBase):

    id: int     #RELACIJA PROBLEM
    # one-to-many, jedan sport moze imati vise terena, a oni bi se mogli izlistati iz
    # tabele Teren kao "select * where sport je taj i taj..."
    # teren: Optional[TerenRead] = None

    class Config:
        from_attributes = True

class TerenRead(TerenBase):

    id: int  #RELACIJA PROBLEM?, STA CE BITI VlasnikRead, SportRead
    # vlasnik: Optional[VlasnikRead] = None -- imamo vlasnik_id
    # sport: Optional[SportRead]= None -- ispisat ce se svejedno sport_id, to nam je dovoljno? nisam 100% sigurna
    # ocjene: Optional[Ocjene]= None -- isto ocjene_id ce bit, uvijek mozemo korisiti "select" upite da izlistamo
    # sve ocjene na zahtjev?
    
    # termini: Optional[Termin]= None -- necemo sve termine ispisivati, mozemo u "Termini" odraditi
    # select * where teren=eldinovTeren

    class Config:
        from_attributes = True

class OcjeneRead(OcjeneBase):

    id: int
    # teren: Optional[TerenRead] = None -- ispisat ce nam teren_id svejedno

    class Config:
        from_attributes = True

class TerminRead(TerminBase):

    id: int  #RELACIJA PROBLEM?
    # teren: Optional[TerenRead] = None  -- teren_id
    # tim: Optional[TimRead] = None -- tim_id

    class Config:
        from_attributes = True

class TimRead(TimBase):

    id: int
    # termini: Optional[TerminRead] = None -- "select * from Termin where tim=eldinovTim" i izlistat ce sve :D

    class Config:
        from_attributes = True

class KorisnikTimRead(KorisnikTimBase):

    id: int

    class Config:
        from_attributes = True

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