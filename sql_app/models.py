from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Korisnik(Base):
    __tablename__ = "korisnik_tabela"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    username = Column(String, index=True)
    ime = Column(String, nullable=False)
    prezime = Column(String, nullable=False)
    datum_rodjenja = Column(Date, nullable=False)
    lokacija = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    telefon = Column(String, nullable=True)
    hashed_password = Column(String)
    disabled = Column(Boolean)

class Vlasnik(Base):
    __tablename__ = "vlasnik_tabela"

    id = Column(Integer, primary_key = True, autoincrement = True)
    sifra = Column(String, nullable = False)
    ime = Column(String, nullable = False)
    prezime = Column(String, nullable = False)
    datum_rodjenja = Column(Date, nullable = False)
    lokacija = Column(String, nullable = False)
    mail = Column(String, unique = True, index=True)
    telefon = Column(String, nullable=True)

    # one to many
    tereni = relationship("Teren", back_populates="vlasnik")

class Sport(Base):

    __tablename__ = "sport_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    naziv = Column(String, nullable=False)

    # one to many
    tereni = relationship("Teren", back_populates="sport")

class Teren(Base):
    __tablename__ = "teren_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vlasnik_id = Column(Integer, ForeignKey("vlasnik_tabela.id"), nullable=False)
    sport_id = Column(Integer, ForeignKey("sport_tabela.id"), nullable=False)
    #ocjene_id = Column(Integer, ForeignKey("ocjene_tabela.id"), nullable=False)
    vrsta = Column(String, nullable=False)
    lokacija = Column(String, nullable=False)
    cijena = Column(Integer, nullable=False)

    # one to many
    vlasnik = relationship("Vlasnik", back_populates="tereni")
    # one to many
    sport = relationship("Sport", back_populates="tereni")
    # one to one
    ocjene = relationship("Ocjene", back_populates="teren")
    # one to many
    termini = relationship("Termin", back_populates="teren")

class Ocjene(Base):
    __tablename__ = "ocjene_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = Column(Integer, ForeignKey("korisnik_tabela.id"), nullable=False)
    teren_id = Column(Integer, ForeignKey("teren_tabela.id"), nullable=False)
    ocjena = Column(Integer, nullable=False)

    # one to one
    teren = relationship("Teren", back_populates="ocjene")

class Termin(Base):
    __tablename__ = "termin_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teren_id = Column(Integer, ForeignKey("teren_tabela.id"), nullable=False)
    tim_id = Column(Integer, ForeignKey("tim_tabela.id"), nullable=False)
    vrijeme_pocetka = Column(DateTime, nullable=False)
    vrijeme_kraja = Column(DateTime, nullable=False)
    je_li_privatni = Column(Boolean, nullable=False)

    # one to many
    teren = relationship("Teren", back_populates="termini")
    # one to many
    tim = relationship("Tim", back_populates="termini")

class Tim(Base):
    __tablename__ = "tim_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sport_id = Column(Integer, ForeignKey("sport_tabela.id"), nullable=False)
    potreban_broj_igraca = Column(Integer) # dinamicki se mijenja?
    max_broj_igraca = Column(Integer, nullable=False)
    nivo_vjestine = Column(Integer, nullable=False) # Koliki nivo vjestine korisnici moraju imati da bi mogli biti u timu
    lokacija_tima = Column(String, nullable=False)
    broj_slobodnih_mjesta = Column(Integer) # dinamicki se mijenja?

    # one to many
    termini = relationship("Termin", back_populates="tim")

# Tabela kreirana zbog many-to-many veze izmedju korisnika i tima
# jedan korisnik moze biti u vise timova
class KorisnikTim(Base):
    
    __tablename__ = "korisnik_tim_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = Column(Integer, ForeignKey("korisnik_tabela.id"), nullable=False)
    tim_id = Column(Integer, ForeignKey("tim_tabela.id"), nullable=False)

