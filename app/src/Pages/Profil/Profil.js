import React from 'react';
import './Profil.css';
import { useAuth } from '../../AuthProvider';

// komponenta koja prikazuje sve informacije o profilu na kojem smo ulogovani

function Profil() {
  const { user, loading } = useAuth();
  if (loading) return <div>Loading...</div>;
  return (
      <div>
          <h2>Korsnik: {user.user.ime} {user.user.prezime}</h2>
          <h2>Username: {user.user.username}</h2>
          <h2>Uloga: {user.role}</h2>
         {user.role === "vlasnik" ? (
          <>
              <h1>Komponente za vlasnika</h1>
          </>
         ) : (
          <>
             <h1>Komponente za korisnika</h1>
          </>
         )
      }
      </div>
  );
}

export default Profil;
