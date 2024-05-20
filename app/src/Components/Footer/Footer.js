import React from 'react';
import './Footer.css';

// komponenta footera

function Footer() {
  return (
    <footer>
      <ul className="footer-links">
        <li><a href="/home">Home</a></li>
      </ul>
      <p>Copyright &copy; 2024</p>
    </footer>
  );
}

export default Footer;
