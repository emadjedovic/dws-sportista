import React, { useState } from 'react';
import ReactDOM from 'react-dom/client'
import Box from '@mui/material/Box';
import FormControl from '@mui/material/FormControl';
import TextField from '@mui/material/TextField';
import PersonIcon from '@mui/icons-material/Person';
import AlternateEmailIcon from '@mui/icons-material/AlternateEmail';
import PasswordIcon from '@mui/icons-material/Password';
import { Chip } from '@mui/material';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import PersonPinCircleIcon from '@mui/icons-material/PersonPinCircle';
import PhoneIcon from '@mui/icons-material/Phone';




import './LoginSignup.css';
/*import Login from './Login.jsx';
import Signup from './SignUp.jsx';*/

const Signup = ({ toggleMode }) => {
  const [selectedSports, setSelectedSports] = useState([]);
  const [currentSport, setCurrentSport] = useState('');
  const [availableSports, setAvailableSports] = useState(['Fudbal', 'Košarka', 'Tenis', 'Odbojka']);

  const handleSportSelect = (sport) => {
    if (selectedSports.length < 3 && !selectedSports.includes(sport)) {
      setSelectedSports([...selectedSports, sport]);
      setCurrentSport('');
    }
  };

  const handleSportRemove = (sportToRemove) => {
    setSelectedSports(selectedSports.filter(sport => sport !== sportToRemove));
  };

  return (
    <div className='container'>
      <div className='header'>
        <div className='text'>Sign Up</div>
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
              id="name"
              label="Name"
              InputProps={{
              
                startAdornment: (
                  <PersonIcon />
                ),
              }}
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="last-name"
              label="Last name"
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="email"
              label="E-mail"
              InputProps={{
                startAdornment: (
                  <AlternateEmailIcon />
                ),
              }}
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="password"
              label="Password"
              type="password"
              InputProps={{
                
                startAdornment: (
                  <PasswordIcon />
                ),
              }}
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="date_of_birth"
              placeholder="Date of birth"
              label="Date of birth"
              type="date"
              InputProps={{
                startAdornment: (
                  <CalendarMonthIcon/>
                ),
              }}
              
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="location"
              label="Location"
              InputProps={{
                startAdornment: (
                  <PersonPinCircleIcon />
                ),
              }}
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="phone"
              label="Phone"
              InputProps={{
                startAdornment: (
                  <PhoneIcon/>
                ),
              }}
            />
          </FormControl>

          <Box component="div" className="select-sport-div">
              <label className='select-sport-label'>Select up to 3 sports</label>
              
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
        </Box>
      </div>
      <div className='forgot-password'>Already have an account? <span onClick={toggleMode}>Sign in!</span></div>
      <div className='submit-container'>
        <div className='submit'>Sign Up</div>
      </div>
    </div>
  );
};


const Login = ({ toggleMode }) => {
  return (
    <div className='container'>
      <div className='header'>
        <div className='text'>Login</div>
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
              id="input-with-icon-adornment"
              label="E-mail"
              InputProps={{
                startAdornment: (
                  <AlternateEmailIcon />
                ),
              }}
            />
          </FormControl>
          <FormControl variant="standard">
            <TextField
              id="input-with-icon-adornment"
              label="Password"
              InputProps={{
                startAdornment: (
                  <PasswordIcon />
                ),
              }}
            />
          </FormControl>
        </Box>
      </div>
      <div className='forgot-password'>Don't have an account? <span onClick={toggleMode}>Sign up!</span></div>
      <div className='submit-container'>
        <div className='submit'>Sign In</div>
      </div>
    </div>
  );
};

const LoginSignup = () => {
  const [isSignUp, setIsSignUp] = useState(false);

  const toggleMode = () => {
    setIsSignUp(!isSignUp);
  };

  let component;
  if (!isSignUp) {
    component = <Login toggleMode={toggleMode} />;
  } else {
    component = <Signup toggleMode={toggleMode} />;
  }

  return (
    <>
      {component}
    </>
  );
};

export default LoginSignup;
