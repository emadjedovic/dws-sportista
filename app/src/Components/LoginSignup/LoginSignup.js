import React, { useState } from 'react';
import {FormControl,TextField,Chip,Box,Switch} from '@mui/material';
/*import AlternateEmailIcon from '@mui/icons-material/AlternateEmail';
import PasswordIcon from '@mui/icons-material/Password';
import PersonIcon from '@mui/icons-material/Person';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import PersonPinCircleIcon from '@mui/icons-material/PersonPinCircle';
import PhoneIcon from '@mui/icons-material/Phone';*/
import axios from 'axios';

import './LoginSignup.css';

// Komponenta za registraciju korisnika
const Signup = ({ toggleMode }) => {

  // Stanje za podatke korisnika
  const [userData, setUserData] = useState({
    username: '',
    ime: '',
    prezime: '',
    email: '',
    password: '',
    datum_rodjenja: '',
    lokacija: '',
    telefon: '',
    izabraniSportovi: [],
  });

  // Stanje za izabrane sportove
  const [selectedSports, setSelectedSports] = useState([]);
  // Stanje za trenutni sport
  const [currentSport, setCurrentSport] = useState('');
  // Stanje za dostupne sportove (trebao bi endpoint za dohvatanje sportova iz baze)
  const [availableSports, setAvailableSports] = useState(['Fudbal', 'Košarka', 'Tenis', 'Odbojka']);
  // Stanje za profil tipa poslovni ili korisnik
  const [poslovni, setPoslovni] = React.useState(false);

  // Funkcija za popunjavanje userData
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData({ ...userData, [name]: value });
    };

    // Funkcija za odabir poslovnog tipa profila
    const handleChange = (e) => {
      setPoslovni(e.target.checked);
      console.log(poslovni)
    };

  // Funkcija za registraciju
  const handleSubmit = async (e) => {
    e.preventDefault(); 
    try {
      if(!poslovni){
      const response = await axios.post('http://localhost:8000/register', userData);
      console.log(response.data);} 
    } catch (error) {
      console.error('Greška pri registraciji korisnika:', error);
    }
  };

  // Funkcija za dodavanje izabranog sporta (ako nije već odabrano 3 sporta)
  const handleSportSelect = (sport) => {
    if (selectedSports.length < 3 && !selectedSports.includes(sport)) {
      setSelectedSports([...selectedSports, sport]);
      setCurrentSport('');
    }
  };

  // Funkcija za uklanjanje izabranog sporta
  const handleSportRemove = (sportToRemove) => {
    setSelectedSports(selectedSports.filter(sport => sport !== sportToRemove));
  };

  // Prikaz forme za registraciju
  return (
    <form className='form' onSubmit={handleSubmit} >
      <div className='header'>
        <div className='text'>Registracija</div>
      </div>
      <div className='inputs'>
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            '& > :not(style)': {
              my: 1,
              width: '100%',
            },
          }}
        >
          <FormControl variant="standard">
            <TextField
              id="username"
              label="Korisničko ime"
              name="username"
              value={userData.username}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="ime"
              label="Ime"

              name="ime"
              value={userData.ime}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="prezime"
              label="Prezime"
              name="prezime"
              value={userData.prezime}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="email"
              label="E-mail"

              name="email"
              value={userData.email}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="password"
              label="Lozinka"
              type="password"
              name="password"
              value={userData.password}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="datum_rodjenja"
              placeholder="Datum rođenja"
              type="date"
              name="datum_rodjenja"
              value={userData.datum_rodjenja}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="lokacija"
              label="Lokacija"
              name="lokacija"
              value={userData.lokacija}
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="telefon"
              label="Telefon"
              
              name="telefon"
              value={userData.telefon}
              onChange={handleInputChange}
              
            />
          </FormControl>

          <Box component="div" className="select-sport-div">
            <label className='select-sport-label'>Izaberite do 3 sporta:</label>
            <Box
              component="fieldset"
              id="sports"
              value={selectedSports.join(', ')}
              onChange={(e) => setCurrentSport(e.target.value)}
              style={{
                position: 'relative',
                width: '98%',
                minHeight: '50px',
                padding: '0.2rem',
                borderRadius: '4px',
                border: '1px solid #b2abab',
                resize: 'none',
                caretColor: 'initial',
              }}
            >
              <div
                className="selected-sports"
                style={{ pointerEvents: 'none' }}
              >
                {selectedSports.map((sport, index) => (
                  <Chip
                    key={index}
                    label={sport}
                    onDelete={() => handleSportRemove(sport)}
                    style={{ margin: '0.5rem', pointerEvents: 'auto' }}
                  />
                ))}
              </div>
            </Box>

            <Box component="div">
              {availableSports.map((sport, index) => (
                <Chip
                  key={index}
                  label={sport}
                  onClick={() => handleSportSelect(sport)}
                  style={{ cursor: 'pointer', margin: '0.5rem' }}
                />
              ))}
            </Box>
          </Box>
          <div className='poslovni-switch'>
            <label>Poslovni</label>
              <Switch
              label='Poslovni'
                checked={poslovni}
                onChange={handleChange}
                inputProps={{ 'aria-label': 'controlled' }}
              />
          </div>
        </Box>
      </div>
      <div className='account-check'>Već imate nalog? <span onClick={toggleMode}>Prijavite se!</span></div>
      <div className='submit-container'>
        <button type="submit" className='submit'>Registracija</button>
      </div>
    </form>
  );
};

// Komponenta za prijavu korisnika
const Login = ({ toggleMode }) => {

  const formData = new FormData();

  // Funkcija za popunjavanje objekta formData podacima korisnika
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    formData.set(name, value); 
    }

  // Funkcija za prijavu
  const handleSubmit = async (e) => {
    e.preventDefault(); 
    try {
      const response = await axios.post('http://localhost:8000/token', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }); 
      console.log("Uspješan login!\n", response.data);
    } catch (error) {
      console.error('Greška pri prijavi korisnika:', error);
    }
  }
  
  // Forma za prijavu
  return (
    <form className='container' onSubmit={handleSubmit}>
      <div className='header'>
        <div className='text'>Prijava</div>
      </div>
      <div className='inputs' >
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            '& > :not(style)': {
              my: 1,
              width: '100%',
            },
          }}
        >
          <FormControl variant="standard">
            <TextField
              id="username"
              label="Korisničko ime"
              name="username"
              onChange={handleInputChange}
              required
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="password"
              type="password"
              label="Lozinka"
              name="password"
              onChange={handleInputChange}
              required
            />
          </FormControl>
        </Box>
      </div>
      <div className='account-check'>Nemate nalog? <span onClick={toggleMode}>Registrujte se!</span></div>
      <div className='submit-container'>
        <button type='submit' className='submit'>Prijavite se</button>
      </div>
    </form>
  );
};

// Komponenta za prijavu/registraciju
const LoginSignup = () => {

    // Stanje za praćenje režima (prijavljivanje ili registracija)
  const [isSignUp, setIsSignUp] = useState(false);

  // Funkcija za promjenu režima
  const toggleMode = () => {
    setIsSignUp(!isSignUp);
  };

  // Dodjeljivanje komponente u zavisnosti od režima
  let component;
  if (!isSignUp) {
    component = <Login toggleMode={toggleMode} />;
  } else {
    component = <Signup toggleMode={toggleMode} />;
  }
  
  // Prikaz komponente
  window.scrollTo(0, 0)
  return (
    <>
      {component}
    </>
  );
};

export default LoginSignup;
