import React, { useEffect, useState } from 'react';
import { Chip, Box } from '@mui/material';
import axios from 'axios'; 

import './SportSelection.css';

function SportSelection({ selectedSports = [], setSelectedSports }) {
  const [availableSports, setAvailableSports] = useState([]);

  useEffect(() => {
    const fetchSports = async () => {
      try {
        const response = await axios.get('http://localhost:8000/sportovi');
        setAvailableSports(response.data);
      } catch (error) {
        console.log(error);
      }
    };
  
    fetchSports(); 
  }, []);

  const handleSportSelect = (sport) => {
    if (selectedSports.length < 3 && !selectedSports.includes(sport)) {
      setSelectedSports([...selectedSports, sport]);
    }
  };

  const handleSportRemove = (sportToRemove) => {
    setSelectedSports(selectedSports.filter(sport => sport !== sportToRemove));
  };

  return (
    <div className="sport-selection-container">
      <label>Izaberite do 3 sporta:</label>
      <Box
        className="input"
        component="fieldset"
        id="sports"
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
        {selectedSports.map((sport) => (
          <Chip
            key={sport.id}
            label={sport.naziv}
            onDelete={() => handleSportRemove(sport)}
            style={{
              cursor: 'pointer',
              margin: '0.5rem',
              backgroundColor: 'lightblue',
            }}
          />
        ))}
      </Box>
      <Box component="div">
        {availableSports.map((sport) => (
          <Chip
            key={sport.id}
            label={sport.naziv}
            onClick={() => handleSportSelect(sport)}
            style={{
              cursor: 'pointer',
              margin: '0.5rem',
            }}
          />
        ))}
      </Box>
    </div>
  );
}

export default SportSelection;
