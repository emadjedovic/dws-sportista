import React, { useState } from 'react'
import { FormControl, TextField } from '@mui/material';
import { useForm } from "react-hook-form";
import { useAuth } from "../../AuthProvider";

import './LoginForm.css'

function LoginForm({ toggleForm, currentFooter }) {
    const [dataIncorrect, setDataIncorrect] = useState(false);
    const { register, handleSubmit, formState: { errors, touchedFields } } = useForm();

    const auth = useAuth();
    const onSubmit = async (data) => {
        try {
            await auth.login(data);
        } catch (error) {
                console.error('Login failed:', error);
                setDataIncorrect(true);
        
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
                    onChange={() => setDataIncorrect(false)} 
                    {...register("username", { required: true })}
                />
                <TextField
                    className="input"
                    sx={{ margin: '2% auto' }}
                    id="password"
                    type="password"
                    label="Lozinka"
                    name="password"
                    onChange={() => setDataIncorrect(false)} 
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
