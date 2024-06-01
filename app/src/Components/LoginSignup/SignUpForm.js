import React, { useEffect, useState } from 'react'
import { FormControl, TextField, Switch } from '@mui/material';
import SportSelection from './SportSelection';
import { useForm } from "react-hook-form";
import api from '../../api';

import './SignUpForm.css';

function SignUp({ toggleForm, currentFooter }) {

  const [isPoslovni, setIsPoslovni] = useState(false);
  const [selectedSports, setSelectedSports] = useState([]);
  const [usernameTaken, setUsernameTaken] = useState(false);
  const [emailExists, setEmailExists] = useState(false);

  const { register, handleSubmit, formState: { errors, touchedFields } } = useForm();
  useEffect(() => {
  }, [isPoslovni])

  const onSubmit = async (data) => {
    setUsernameTaken(false);
    setEmailExists(false);
    if (!isPoslovni) {
      selectedSports.map((sport) => {
        data.sportovi = selectedSports.map(sport => sport.id);
      })
    } else {
      delete data.sportovi;
    }
    console.log(data);
    try {
      const response = await api.post('/register', data);
      toggleForm();
    } catch (error) {
      if (error.response.status === 400 && error.response.data.detail === "Username already registered") {
        setUsernameTaken(true);
      }
      else if (error.response.status === 400 && error.response.data.detail === "Email already registered") {
        setEmailExists(true);
      } else {
        console.error('Registration failed:', error);
      }
    }
  }


  return (
    <form className="register-container" onSubmit={handleSubmit(onSubmit)}>
      <FormControl variant="standard">
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="username"
          error={usernameTaken}
          helperText={usernameTaken ? "Korisničko ime je zauzeto" : null}
          label="Korisničko ime"
          name="username"
          onChange={() => setUsernameTaken(false)}
          {...register("username", { required: true })}
          required
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="ime"
          label="Ime"
          name="ime"
          {...register("ime", { required: true })}
          required
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="prezime"
          label="Prezime"
          name="prezime"
          {...register("prezime", { required: true })}
          required
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="email"
          label="E-mail"
          error={(!!errors.email && touchedFields.email) || emailExists}
          helperText={(!!errors.email && touchedFields.email) ? "Pogrešan unos" : emailExists ? "Već postoji nalog registrovan na ovaj e-mail" : null}
          onChange={() => setEmailExists(false)}
          name="email"
          {...register("email", {
            required: true,
            pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          })}
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="password"
          label="Lozinka"
          type="password"
          name="password"
          error={!!errors.password && touchedFields.password}
          helperText={(!!errors.password && touchedFields.password) ? "Šifra mora sadržati bar jedno malo, bar jedno veliko slovo, bar jednu cifru i imati između 6 i 15 karaktera" : null}
          {...register("password", {
            required: true,
            pattern: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,15}$/
          })}
          required
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="datum_rodjenja"
          placeholder="Datum rođenja"
          type="date"
          name="datum_rodjenja"
          {...register("datum_rodjenja", { required: true })}
          required
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="lokacija"
          label="Lokacija"
          name="lokacija"
          {...register("lokacija", { required: true })}
          required
        />
        <TextField
          className="input"
          sx={{ margin: '2% auto' }}
          id="telefon"
          label="Telefon"
          name="telefon"
          {...register("telefon")}
        />
        <div className='poslovni-switch'>
          <label>Poslovni</label>
          <Switch
            label='Poslovni'
            checked={isPoslovni}
            onChange={(e) => { setIsPoslovni(e.target.checked) }}
            inputProps={{ 'aria-label': 'controlled' }}
          />
        </div>
        {!isPoslovni ? <SportSelection selectedSports={selectedSports} setSelectedSports={setSelectedSports} /> : null}
        <div className="form-footer">
          <div className='account-check'>
            <span>{currentFooter.accountCheck} </span>
            <span className="clickable" onClick={toggleForm}>{currentFooter.changeComponent}</span>
          </div>
          <div className='submit-container'>
            <button type='submit' className='submit'>
              {currentFooter.buttonText}
            </button>
          </div>
        </div>
      </FormControl>
    </form>
  )
}

export default SignUp