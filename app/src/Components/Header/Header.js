import React from 'react';
import './Header.css';
import { useAuth } from "../../AuthProvider";


// navigacijska traka

function Header() {
  const auth = useAuth();
  return (
    <header>
      <nav>
        <a href="/home">Home</a>
        <a href="/korisnici">Korisnici</a>
        <a href="/vlasnici">Vlasnici</a>
        <a href="/tereni">Tereni</a>
        <a href="/termini">Termini</a>
        <a href="/timovi">Timovi</a>
        <a href="/profil">Vaš profil</a>
        <a href="/terminForma">Forma za kreiranje termina</a>
        <a href="/">Login/Signup</a>
        <button onClick={() => auth.logOut()} className="btn-submit">Log out</button>
      </nav>
    </header>
  );
}

export default Header;
