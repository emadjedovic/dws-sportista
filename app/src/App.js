import React, {useState, useEffect} from "react"
import api from './api'
import logo from './logo.svg';
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import LoginSignup from './Components/LoginSignup';
import Profile from './Components/Profile';
import Search from './Components/Search';
import CreateEvent from './Components/CreateEvent';
import EventDetails from './Components/EventDetails';
import Header from './Components/Header';
import Footer from './Components/Footer';
import './App.css';


/*
Uslovno renderujemo Header komponent shodno tome je li LoginSignup komponenta aktivna. Koristi se hook useLocation
da odredimo trenutnu putanju i pokažemo Header samo kad nismo na putanju "/", što je LoginSignup.
Kreiramo novu komponentu Main koja koristi taj useLocation hook.
Ovime se osiguravamo da nemamo Header komponentu na početnoj stranici gdje se korisnik prijavljuje/registruje.
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
        <Route path="/profile" element={<Profile />} />
        <Route path="/search" element={<Search />} />
        <Route path="/create-event" element={<CreateEvent />} />
        <Route path="/event-details" element={<EventDetails />} />
      </Routes>
      <Footer />
    </div>
    );
}

export default App;
