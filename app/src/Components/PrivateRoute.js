import React from 'react';
import { useLocation, Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../AuthProvider';

const PrivateRoute = () => {
    const { user, token } = useAuth();
    const location = useLocation();
    
    if (!token) return <Navigate to="/" state={{ from: location }} replace/>;
    return <Outlet />;
};

export default PrivateRoute;

