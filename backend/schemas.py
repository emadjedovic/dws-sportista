from typing import List
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime

class KorisnikBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    ime: str | None = None
    prezime: str | None = None
    disabled: bool | None = None
    datum_rodjenja: date | None = None
    lokacija: str | None = None
    telefon: str | None = None


class KorisnikInDB(KorisnikBase):
    hashed_password: str


class KorisnikRead(KorisnikBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class KorisnikCreate(KorisnikBase):
    password: str
    sportovi: List[int]

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class VlasnikBase(BaseModel):
    
    ime: str | None = None
    username: str | None = None
    prezime: str | None = None
    datum_rodjenja: datetime | None = None
    lokacija: str | None = None
    email: EmailStr | None = None
    telefon: str | None = None


class VlasnikCreate(VlasnikBase):
    sifra:str

class VlasnikInDB(VlasnikBase):
    sifra: str


class VlasnikRead(VlasnikBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class SportBase(BaseModel):
    naziv: str | None = None


class SportRead(SportBase):
    id: int

    class Config:
        from_attributes = True


class SportCreate(SportBase):
    pass

class TerenBase(BaseModel):
    vlasnik_id: int
    sport_id: int
    ocjene_id: int
    vrsta: str
    lokacija: str
    cijena: int

class TerenRead(TerenBase):
    id: int

    class Config:
        from_attributes = True


class TerenCreate(TerenBase):
    pass

class OcjeneBase(BaseModel):
    korisnik_id: int
    teren_id: int
    ocjena: int = Field(..., ge=0, le=5)  # od 0 do 5

    
class OcjeneRead(OcjeneBase):
    id: int

    class Config:
        from_attributes = True


class OcjeneCreate(OcjeneBase):
    pass

class TerminBase(BaseModel):
    teren_id: int
    tim_id: int
    vrijeme_pocetka: datetime
    vrijeme_kraja: datetime
    je_li_privatni: bool

    @validator("vrijeme_kraja")
    def end_time_after_start_time(cls, v, values):
        if "vrijeme_pocetka" in values and v <= values["vrijeme_pocetka"]:
            raise ValueError("Vrijeme kraja mora biti nakon vremena početka.")
        return v


class TerminRead(TerminBase):
    id: int

    class Config:
        from_attributes = True


class TerminCreate(TerminBase):
    pass

class TimBase(BaseModel):
    sport_id: int
    termin_id: int
    potreban_broj_igraca: (
        int  # Neka bude potreban broj igraca, tj. koliko igraca fali za termin
    )
    max_broj_igraca: int  # max broj igraca na terminu
    nivo_vjestine: int = Field(..., ge=0, le=5)  # od 0 do 5
    lokacija_tima: str
    broj_slobodnih_mjesta: int = Field(
        ..., ge=0
    )  # da li je ovo duplikat, vec ima potreban_broj_igraca?
    # da li nam treba varijabla za trenutni broj igaca?

    @validator("max_broj_igraca")
    def provjera_broja_igraca(cls, v, values):
        if "potreban_broj_igraca" in values and v < values["potreban_broj_igraca"]:
            raise ValueError(
                "Broj potrebnih igraca ne može biti veći od maksimalnog broja igrača"
            )
        return v


class TimRead(TimBase):
    id: int

    class Config:
        from_attributes = True

class TimCreate(TimBase):
    pass

class KorisnikTimBase(BaseModel):
    korisnik_id: int
    tim_id: int

class KorisnikTimRead(KorisnikTimBase):
    id: int

    class Config:
        from_attributes = True

class KorisnikTimCreate(KorisnikTimBase):
    pass
