import React, { useState } from 'react'
import { FormControl, TextField } from '@mui/material';
import { useForm } from "react-hook-form";
import axios from 'axios';

import './LoginForm.css'

function LoginForm({ toggleForm, currentFooter }) {
    const [dataIncorrect, setDataIncorrect] = useState(false);
    const { register, handleSubmit, formState: { errors, touchedFields } } = useForm();

    const onSubmit = async (data) => {
        console.log("user data: ", data)
        try {
            const response = await axios.post('http://localhost:8000/token', data, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log(response.data);
        } catch (error) {
            if (error.response.status === 400) {
                setDataIncorrect(true);
            } else {
                console.error('Login failed:', error);
            }
        }
    }

    return (
        <form className="login-container" onSubmit={handleSubmit(onSubmit)}>
            <FormControl variant="standard">
                <TextField
                    className="input"
                    sx={{ margin: '2% auto' }}
                    id="username"
                    label="Korisničko ime"
                    name="username"
                    onChange={() => setDataIncorrect(false)} // Reset dataIncorrect on change
                    {...register("username", { required: true })}
                />
                <TextField
                    className="input"
                    sx={{ margin: '2% auto' }}
                    id="password"
                    type="password"
                    label="Lozinka"
                    name="password"
                    onChange={() => setDataIncorrect(false)} // Reset dataIncorrect on change
                    {...register("password", { required: true })}
                />
                {dataIncorrect && (
                    <p className="incorrect-data">Korisničko ime ili lozinka su netačni.</p>
                )}
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

export default LoginForm;
