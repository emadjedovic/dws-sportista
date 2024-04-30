from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Korisnik(Base):
    __tablename__ = "korisnik"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True, nullable=False)
    ime = Column(String, nullable=False)
    prezime = Column(String, nullable=False)
    datum_rodjenja = Column(Date, nullable=False)
    lokacija = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    telefon = Column(String, nullable=True)
    hashed_password = Column(String)
    disabled = Column(Boolean)

    # veze iz drugih tabela
    sportovi = relationship("KorisnikSport", back_populates="korisnik")
    timovi = relationship("KorisnikTim", back_populates="korisnik")
    ocjene = relationship("Ocjene", back_populates="korisnik")


class Vlasnik(Base):
    __tablename__ = "vlasnik"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sifra = Column(String, nullable=False)
    ime = Column(String, nullable=False)
    prezime = Column(String, nullable=False)
    datum_rodjenja = Column(Date, nullable=False)
    lokacija = Column(String, nullable=False)
    mail = Column(String, unique=True, index=True)
    telefon = Column(String, nullable=True)

    # veze iz drugih tabela
    tereni = relationship("Teren", back_populates="vlasnik")


class Sport(Base):

    __tablename__ = "sport"

    id = Column(Integer, primary_key=True, autoincrement=True)
    naziv = Column(String, index=True, nullable=False)

    # veze iz drugih tabela
    tereni = relationship("Teren", back_populates="sport")
    korisnici = relationship("KorisnikSport", back_populates="sport")
    timovi = relationship("Tim", back_populates="sport")


# many to many
class KorisnikSport(Base):

    __tablename__ = "korisnikSport"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = vlasnik_id = Column(
        Integer, ForeignKey("korisnik.id"), nullable=False
    )
    sport_id = Column(Integer, ForeignKey("sport.id"), nullable=False)

    # veze iz ove tabele
    korisnik = relationship("Korisnik", back_populates="sportovi")
    sport = relationship("Sport", back_populates="korisnici")


class Teren(Base):
    __tablename__ = "teren"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vlasnik_id = Column(Integer, ForeignKey("vlasnik.id"), nullable=False)
    sport_id = Column(Integer, ForeignKey("sport.id"), nullable=False)
    vrsta = Column(String, nullable=False)
    lokacija = Column(String, nullable=False)
    cijena = Column(Integer, nullable=False)

    # veze iz ove tabele
    vlasnik = relationship("Vlasnik", back_populates="tereni")
    sport = relationship("Sport", back_populates="tereni")

    # veze iz drugih tabela
    ocjene = relationship("Ocjene", back_populates="teren")
    termini = relationship("Termin", back_populates="teren")


class Ocjene(Base):
    __tablename__ = "ocjene"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = Column(Integer, ForeignKey("korisnik.id"), nullable=False)
    teren_id = Column(Integer, ForeignKey("teren.id"), nullable=False)
    ocjena = Column(Integer, nullable=False)
    # komentari i vremenske oznake?

    # veze iz ove tabele
    korisnik = relationship("Korisnik", back_populates="ocjene")
    teren = relationship("Teren", back_populates="ocjene")


class Termin(Base):
    __tablename__ = "termin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teren_id = Column(Integer, ForeignKey("teren.id"), nullable=False)
    tim_id = Column(Integer, ForeignKey("tim.id"), nullable=False)
    vrijeme_pocetka = Column(DateTime, nullable=False)
    vrijeme_kraja = Column(DateTime, nullable=False)
    je_li_privatni = Column(Boolean, nullable=False)
    broj_slobodnih_mjesta = Column(Integer)
    potreban_broj_igraca = Column(Integer)
    max_broj_igraca = Column(Integer, nullable=False)
    nivo_vjestine = Column(
        Integer, nullable=False
    )  # Koliki nivo vjestine korisnici moraju imati da bi mogli pristupiti terminu
    
    lokacija_tima = Column(String, nullable=False)

    # veze iz ove tabele
    teren = relationship("Teren", back_populates="termini")
    tim = relationship("Tim", back_populates="termini")


class Tim(Base):
    __tablename__ = "tim"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sport_id = Column(Integer, ForeignKey("sport.id"), nullable=False)

    # veze iz ove tabele
    sport = relationship("Sport", back_populates="timovi")

    # veze iz drugih tabela
    termini = relationship("Termin", back_populates="tim")
    korisnici = relationship("KorisnikTim", back_populates="tim")


# Tabela kreirana zbog many-to-many veze izmedju korisnika i tima
# jedan korisnik moze biti u vise timova
class KorisnikTim(Base):

    __tablename__ = "korisnik_tim"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = Column(Integer, ForeignKey("korisnik.id"), nullable=False)
    tim_id = Column(Integer, ForeignKey("tim.id"), nullable=False)

    # veze
    korisnik = relationship("Korisnik", back_populates="timovi")
    tim = relationship("Tim", back_populates="korisnici")
