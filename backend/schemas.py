from typing import Optional
from pydantic import BaseModel, EmailStr, Field, constr, validator
from datetime import date, datetime

"""
1Bazne klase1 sadrze sve podatke
Nasljedju BaseModel
"""

class Korisnik(BaseModel):
    username: str
    email:str | None = None
    ime: str | None = None
    disabled: bool | None = None

class KorisnikInDB(Korisnik):
    hashed_password: str


class KorisnikBase(BaseModel):
    email: str


class KorisnikCreate(KorisnikBase):
    password: str


class Korisnik(KorisnikBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class KorisnikBase(BaseModel):
    username: str
    email: str
    ime: str

class KorisnikCreate(KorisnikBase):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None


class KorisnikCreate(BaseModel):
    username: str
    email: str
    ime: str
    prezime: str
    datum_rodjenja: date
    lokacija: str
    password: str


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
    cijena: int #ispravljeno :P
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
    potreban_broj_igraca: int #Neka bude potreban broj igraca, tj. koliko igraca fali za termin
    max_broj_igraca: int #max broj igraca na terminu
    nivo_vjestine: int = Field(..., ge=0, le=5) # od 0 do 5
    lokacija_tima: str
    broj_slobodnih_mjesta: int = Field(..., ge=0)

    # 1:N

class KorisnikTimBase(BaseModel):

    korisnik_id: int
    tim_id: int

#Klase za citanje podataka, nasljeduju bazne

class KorisnikRead(KorisnikBase):

    id: int

    class Config:
        from_attributes = True

class VlasnikRead(VlasnikBase):

    id: int    
    #Ako je visak, onda brisem

    class Config: 
        from_attributes= True

class SportRead(SportBase):

    id: int 

    class Config:
        from_attributes = True

class TerenRead(TerenBase):

    id: int  #RELACIJA PROBLEM?, STA CE BITI VlasnikRead, SportRead
    # vlasnik: Optional[VlasnikRead] = None -- imamo vlasnik_id
    # sport: Optional[SportRead]= None -- ispisat ce se svejedno sport_id, to nam je dovoljno? nisam 100% sigurna
    # ocjene: Optional[Ocjene]= None -- isto ocjene_id ce bit, uvijek mozemo korisiti "select" upite da izlistamo
    # sve ocjene na zahtjev? 
    #Nisam siguran kako cemo koristiti select za ispis ako cemo sve preko fastapi ruta raditi?
   

    class Config:
        from_attributes = True

class OcjeneRead(OcjeneBase):

    id: int

    class Config:
        from_attributes = True

class TerminRead(TerminBase):

    id: int

    class Config:
        from_attributes = True

class TimRead(TimBase):

    id: int
  
    class Config:
        from_attributes = True

class KorisnikTimRead(KorisnikTimBase):

    id: int

    class Config:
        from_attributes = True

#Klase za kreiranje podataka, nasljeduju bazne klase

# class KorisnikCreate(KorisnikBase):
#     pass 

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