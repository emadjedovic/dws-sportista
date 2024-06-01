import React, { useContext, createContext, useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import api from './api'; 

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem("token") || "");
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const tokenGot = localStorage.getItem('token');
        if (tokenGot) {
            const fetchUser = async () => {
                await getUser(tokenGot);
            };
            fetchUser();
        }
        else {
            setLoading(false);
        }
    }, []);

    const login = async (data) => {
        try {
            const response = await api.post("/token", data, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            });

            if (response.data && response.data.access_token) {
                setToken(response.data.access_token);
                localStorage.setItem("token", response.data.access_token);
                await getUser(response.data.access_token);
                navigate("/home");
                return;
            }
            throw new Error(response.message);
        } catch (err) {
            console.error(err);
            if (err.response && err.response.status === 400) {
                throw new Error('Korisničko ime ili lozinka su netačni.');
            } else {
                console.error('Unexpected error during login:', err);
                throw new Error('Neuspješno povezivanje s poslužiteljem.');
            }
        } 
    };

    const logOut = () => {
        setUser(null);
        setToken("");
        localStorage.removeItem('token');
        navigate("/");
    };

    const getUser = async (token) => {
        try {
            const response = await api.get('/users/me', {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            setUser(response.data);
        } catch (error) {
            console.error('Failed to fetch user:', error);
            logOut();
        } finally {
            setLoading(false); 
        }
    };

    return (
        <AuthContext.Provider value={{ token, user, login, logOut, loading }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;

export const useAuth = () => {
    return useContext(AuthContext);
};
