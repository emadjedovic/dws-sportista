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

    #Poslovni tip profil
    da_li_je_poslovni = Column(bool, default = False)
    vlasnik_terena = relationship("Tereni", back_populates = "korisnik")
    #Jedan vlasnik vise terena. Vise terena jedan vlasnik

"""
class Poslovni(Base):
    __tablename__ = "poslovni_tabela"

                     Za diskusiju: sadržati Tabelu poslovni ili ukloniti
"""

class Tereni(Base):
    __tablename__ = "tereni_tabela"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vrsta = Column(String, nullable=False)
    lokacija = Column(String, nullable=False)
    cijena = Column(Integer, nullable=False)
    ocjene = Column(list[Integer], nullable=True) #lista intova od 0-5?? #napraviti posebnu tabelu s ocjenama? UserGradeField

    korisnik = relationship ("Korisnik", back_populates = "vlasnik_terena")

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
    teren_id = Column(Integer, ForeignKey("tereni_tabela.id"), nullable=False)
    termin_id = Column(Integer, ForeignKey("termin_tabela.id"), nullable=False)
    broj_igraca = Column(Integer) # dinamicki se mijenja?
    nivo_vjestine = Column(Integer, nullable=False) # Koliki nivo vjestine korisnici moraju imati da bi mogli biti u timu
    korisnici_u_timu = Column(list[Korisnik]) # Lista korisnika, napraviti novu tabelu jer n:n?
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

# class VrstaSporta(Base):

# class MaterijalTerena(Base):

# ostale tabele...

