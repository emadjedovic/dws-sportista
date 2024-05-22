import React, {useState, useEffect} from "react";
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';

import Home from './Pages/Home/Home';
import LoginSignup from './Pages/LoginSignup/LoginSignup';
import Profil from './Pages/Profil/Profil';


import Footer from './Components/Footer/Footer';
import Header from './Components/Header/Header';
import KorisnikList from "./Components/KorisnikList/KorisnikList";
import TereniList from './Components/TereniList/TereniList';
import TerminiList from './Components/TerminiList/TerminiList';
import TimoviList from './Components/TimoviList/TimoviList';
import VlasnikList from './Components/VlasnikList/VlasnikList';

import './App.css';


/*
Uslovno renderujemo Header i Footer komponente shodno tome je li LoginSignup komponenta aktivna.
Koristi se hook useLocation da odredimo trenutnu putanju i pokažemo Header samo kad nismo na
putanji "/", što je LoginSignup. Kreiramo novu komponentu Main koja koristi taj useLocation hook.
Ovime se osiguravamo da nemamo Header i Footer komponente na početnoj stranici
gdje se korisnik prijavljuje/registruje.
*/

function App() {
  return (
    <Router>
      <Main />
    </Router>
  );
}

function Main() {
  const location = useLocation();
  const isLoginSignupPage = location.pathname === '/';

  return (
    <div>
      {!isLoginSignupPage && <Header />}
      <Routes>
        <Route path="/" element={<LoginSignup />} />
        <Route path="/home" element={<Home />} />
        <Route path="/korisnici" element={<KorisnikList />} />
        <Route path="/vlasnici" element={<VlasnikList />} />
        <Route path="/tereni" element={<TereniList />} />
        <Route path="/termini" element={<TerminiList />} />
        <Route path="/timovi" element={<TimoviList />} />
        <Route path="/profil" element={<Profil />} />
      </Routes>
      {!isLoginSignupPage && <Footer />}
    </div>
    );
}

export default App;
