from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, constr, validator
from datetime import date, datetime

# Bazne klase


class KorisnikBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    ime: str | None = None
    disabled: bool | None = None
    datum_rodjenja: date | None = None
    lokacija: str | None = None


class KorisnikInDB(KorisnikBase):
    hashed_password: str


class Korisnik(KorisnikBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class VlasnikBase(BaseModel):
    sifra: str | None = None
    ime: str | None = None
    prezime: str | None = None
    datum_rodjenja: datetime | None = None
    lokacija: str | None = None
    mail: EmailStr | None = None
    telefon: str | None = None


class SportBase(BaseModel):
    naziv: str | None = None


class TerenBase(BaseModel):
    vlasnik_id: int
    sport_id: int
    ocjene_id: int
    vrsta: str
    lokacija: str
    cijena: int


class OcjeneBase(BaseModel):
    korisnik_id: int
    teren_id: int
    ocjena: int = Field(..., ge=0, le=5)  # od 0 do 5


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


class KorisnikTimBase(BaseModel):
    korisnik_id: int
    tim_id: int


# Klase za citanje podataka, nasljeduju bazne


class KorisnikRead(KorisnikBase):
    id: int

    class Config:
        from_attributes = True


class VlasnikRead(VlasnikBase):
    id: int

    class Config:
        from_attributes = True


class SportRead(SportBase):
    id: int

    class Config:
        from_attributes = True


class TerenRead(TerenBase):
    id: int

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


# Klase za kreiranje podataka, nasljeduju bazne klase


class KorisnikCreate(KorisnikBase):
    password: str
    sportovi: List[int]


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
