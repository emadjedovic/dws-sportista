import React, {useState, useEffect} from "react"
import api from './api'
import logo from './logo.svg';
import './App.css';
import LoginSignup from './Components/LoginSignup';

function App() {
  return (
    <div >
      <LoginSignup/>
    </div>
  );
}

export default App;
