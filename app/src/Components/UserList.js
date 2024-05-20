import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserList() {
  const [korisnici, setKorisnici] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedKorisnik, setSelectedKorisnik] = useState(null);

  useEffect(() => {
    // Dohvata listu korisnika sa backenda
    axios.get('/korisnici')
      .then(response => {
        setKorisnici(response.data);
      })
      .catch(error => {
        console.error('Error fetching korisnici:', error);
      });
  }, []);

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  const fetchKorisnikById = async (id) => {
    try {
      const response = await axios.get(`/korisnik/${id}`);
      setSelectedKorisnik(response.data);
    } catch (error) {
      console.error('Error fetching korisnik by ID:', error);
    }
  };

  const fetchKorisnikByUsername = async (username) => {
    try {
      const response = await axios.get(`/korisnik/${username}`);
      setSelectedKorisnik(response.data);
    } catch (error) {
      console.error('Error fetching korisnik by username:', error);
    }
  };

  // Filtrira korisnike na osnovu search podataka
  const filteredKorisnici = korisnici.filter(korisnik => {
    return korisnik.username.toLowerCase().includes(searchQuery.toLowerCase());
  });

  return (
    <div>
      <h1>Korisnici List</h1>
      {/* Traka za pretraživanje */}
      <input
        type="text"
        placeholder="Search for a user..."
        value={searchQuery}
        onChange={handleSearch}
      />
      {/* Prikazuje korisnika */}
      {selectedKorisnik && (
        <div>
          <h2>Korisnik: </h2>
          <p>Username: {selectedKorisnik.username}</p>
          <p>Email: {selectedKorisnik.email}</p>
          {/* Po potrebi ispisati i ostale informacije */}
        </div>
      )}
      <ul>
        {filteredKorisnici.map(korisnik => (
          <li key={korisnik.id}>
            {korisnik.username} - {korisnik.email}
            {/* Dugme da dobijemo korisnika po ID-u */}
            <button onClick={() => fetchKorisnikById(korisnik.id)}>ID</button>
            {/* Dugme da dobijemo korisnika po username-u */}
            <button onClick={() => fetchKorisnikByUsername(korisnik.username)}>Username</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
