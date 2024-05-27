import React, { useEffect, useState } from 'react'
import './LoginSignup.css'
import SignUp from '../../Components/LoginSignup/SignUpForm';
import LoginForm from '../../Components/LoginSignup/LoginForm';

function LoginSignup() {
  const [isSignUp, setIsSignUp] = useState(false);
  const [title, setTitle] = useState("");
  const footerContent = {
    signUp: {
      buttonText: "Registruj se",
      accountCheck: "Već imate nalog?",
      changeComponent: "Prijavite se!"
    },
    login: {
      buttonText: "Prijavite se",
      accountCheck: "Nemate nalog?",
      changeComponent: "Registrujte se!"
    }
  }

  useEffect(() => {
    isSignUp ? setTitle("Registracija") : setTitle("Prijava");
  }, [isSignUp]);

  const toggleForm = () => {
    setIsSignUp(prevIsSignUp => !prevIsSignUp);
  }

  const currentFooter = isSignUp ? footerContent.signUp : footerContent.login;

  return (
    <div className="form-container">
      <div className="form-header">
        <h1>{title}</h1>
      </div>
      <div className="form-body">
        {isSignUp ? (
          <SignUp toggleForm={toggleForm} currentFooter={currentFooter}/>
        ) : (
          <LoginForm toggleForm={toggleForm} currentFooter={currentFooter}/>
        )}
      </div>
    </div>
  )
}

export default LoginSignup;