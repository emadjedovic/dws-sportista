from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class Korisnik(Base):
    __tablename__ = "korisnici_tabela"

    id = Column(Integer, primary_key = True, autoincrement = True)
    ime = Column(String, nullable = False)
    prezime = Column(String, nullable = False)
    datum_rodenja = Column(Date, nullable = False)
    lokacija = Column(String, nullable = False)
    sport = Column(list[String], nullable = False)
    mail = Column(String, unique = True) #ne mogu 2 korisnika imati isti mail, niti se registrovati ukoliko je mail vec zauzet
    sifra = Column(String, nullable = False)
    telefon = Column(String, nullable=True)

    #Poslovni tip profil
    da_li_je_poslovni = Column(bool, default = False)
    vlasnik_terena = relationship("Tereni", back_populates = "korisnik")
    #Jedan vlasnik vise terena. Vise terena jedan vlasnik

# Ema: konsultovala sam se s kolegom od prosle godine koji kaze da je jedino logicno imati
# obje klase "korisnik" i "poslovni" tako da treba nam ovo!!
class Poslovni(Base):
    __tablename__ = "poslovni_tabela"
    # Ema: bolje mozda "Vlasnik" umjesto "Poslovni?"

    id = Column(Integer, primary_key=True, autoincrement=True)

class Sport(Base):

    __tablename__ = "sport_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    naziv = Column(String, nullable=False)

class Tereni(Base):
    __tablename__ = "tereni_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_vlasnik = Column(Integer, ForeignKey("poslovni_tabela.id"), nullable=False) # dodano (Ema)
    vrsta = Column(String, nullable=False)
    lokacija = Column(String, nullable=False)
    cijena = Column(Integer, nullable=False)
    sport_id = Column(Integer, ForeignKey("sport_tabela.id"), nullable=False)
    ocjena = Column(Integer, nullable=False) # ocjenu izracunati kao prosjek svih ocjena?

    korisnik = relationship ("Korisnik", back_populates = "vlasnik_terena")

class Ocjene(Base):
    __tablename__ = "ocjene_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = Column(Integer, ForeignKey("korisnici_tabela.id"), nullable=False)
    teren_id = Column(Integer, ForeignKey("tereni_tabela.id"), nullable=False)
    ocjena = Column(Integer, nullable=False)

class Termini(Base):
    __tablename__ = "termini_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teren_id = Column(Integer, ForeignKey("tereni_tabela.id"), nullable=False)
    tim_id = Column(Integer, ForeignKey("timovi_tabela.id"), nullable=False)
    vrijeme_pocetka = Column(datetime, nullable=False)
    vrijeme_kraja = Column(datetime, nullable=False)
    trajanje_igre_u_min = Column(Integer) # izracunati ovo kao vrijeme_pocetka - vrijeme_kraja
    je_li_privatni = Column(Boolean, nullable=False)

    teren = relationship("Tereni", back_populates="termini")
    # Jedan teren ima više termina. Jedan termin ima jedan teren.
    tim = relationship("Timovi", back_populates="teren")
    # Jedan termin ima jedan tim. Jedan tim rezerviše jedan termin.

class Timovi(Base):
    __tablename__ = "timovi_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sport_id = Column(Integer, ForeignKey("sport_tabela.id"), nullable=False)
    teren_id = Column(Integer, ForeignKey("tereni_tabela.id"), nullable=False)
    termin_id = Column(Integer, ForeignKey("termin_tabela.id"), nullable=False)
    broj_igraca = Column(Integer) # dinamicki se mijenja?
    nivo_vjestine = Column(Integer, nullable=False) # Koliki nivo vjestine korisnici moraju imati da bi mogli biti u timu
    lokacija_tima = Column(String, nullable=False)
    broj_slobodnih_mjesta = Column(Integer) # dinamicki se mijenja?

    teren = relationship("Tereni", back_populates="timovi")
    """
    Jedan tim rezerviše jedan teren.
    Jedan teren je za više timova.
    """

    termin = relationship("Termini", back_populates="tim")
    """
    Jedan tim rezerviše jedan termin.
    Jedan termin je za jedan tim.
    """

# Tabela kreirana zbog many-to-many veze izmedju korisnika i tima
class KorisniciTimovi(Base):
    
    __tablename__ = "korisnici_timovi_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    korisnik_id = Column(Integer, ForeignKey("korisnici_tabela.id"), nullable=False)
    tim_id = Column(Integer, ForeignKey("timovi_tabela.id"), nullable=False)


