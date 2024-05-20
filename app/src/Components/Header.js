import React from 'react';

function Header() {
  return (
    <header>
      {/* Navigacijska traka */}
      <nav>
        <a href="/">Home</a>
        <a href="/korisnici">Korisnici</a>
        <a href="/vlasnici">Vlasnici</a>
        <a href="/tereni">Tereni</a>
        <a href="/termini">Termini</a>
        <a href="/timovi">Timovi</a>
        <a href="/profil">Vaš profil</a>
        <a href="/login-signup">Login/Signup</a>
      </nav>
    </header>
  );
}

export default Header;
