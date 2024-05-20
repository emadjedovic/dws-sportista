import React from 'react';
import './Header.css';

// navigacijska traka

function Header() {
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
        <a href="/">Login/Signup</a>
      </nav>
    </header>
  );
}

export default Header;
