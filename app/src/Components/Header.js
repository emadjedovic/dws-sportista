import React from 'react';

function Header() {
  return (
    <header>
      <h1>Header</h1>
      <nav>
        <a href="/">Home</a>
        <a href="/login-signup">Login/Signup</a>
        <a href="/profile">Profile</a>
        <a href="/search">Search</a>
        <a href="/create-event">Create Event</a>
      </nav>
    </header>
  );
}

export default Header;
