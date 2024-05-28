import React, { useState } from 'react';
import { FormControl, TextField, Switch, FormControlLabel, Button } from '@mui/material';
import axios from 'axios';
import './TerminForma.css';

const TerminForm = () => {
    const [terenId, setTerenId] = useState('');
    const [timId, setTimId] = useState('');
    const [vrijemePocetka, setVrijemePocetka] = useState('');
    const [vrijemeKraja, setVrijemeKraja] = useState('');
    const [jeLiPrivatni, setJeLiPrivatni] = useState(false);
    // const [brojSlobodnihMjesta, setBrojSlobodnihMjesta] = useState('');
    const [potrebanBrojIgraca, setPotrebanBrojIgraca] = useState('');
    const [maxBrojIgraca, setMaxBrojIgraca] = useState('');
    const [nivoVjestine, setNivoVjestine] = useState('');
    const [lokacijaTima, setLokacijaTima] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const terminData = {
            teren_id: terenId,
            tim_id: timId,
            vrijeme_pocetka: vrijemePocetka,
            vrijeme_kraja: vrijemeKraja,
            je_li_privatni: jeLiPrivatni,
            // broj_slobodnih_mjesta: brojSlobodnihMjesta,
            potreban_broj_igraca: potrebanBrojIgraca,
            max_broj_igraca: maxBrojIgraca,
            nivo_vjestine: nivoVjestine,
            lokacija_tima: lokacijaTima,
        };

        try {
            const response = await axios.post('http://localhost:8000/termini/', terminData);
            console.log('Uspjesno kreiran', response.data);
        } catch (error) {
            console.error('Error!', error);
        }
        
    };


    const handlePotrebanBrojIgraca = (e) => {
        const value = e.target.value;
        if (value === '' || (Number(value) >= 0 && !isNaN(Number(value)))) {
            setPotrebanBrojIgraca(value)
        }
    };


    const handleMaxBrojIgraca = (e) => {
        const value = e.target.value;
        if (value === '' || (Number(value) > 0 && !isNaN(Number(value)))) {
            setMaxBrojIgraca(value)
        }
    };


    return (
        <div className="form-container">
            <h1 style={{color:'#1316e9', fontSize:"40px"}}>Kreiraj novi termin</h1>
            <form onSubmit={handleSubmit} className='termin-form'>
                <FormControl variant="standard" fullWidth>
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="terenId"
                        label="Teren ID"
                        type="number"
                        value={terenId}
                        onChange={(e) => setTerenId(e.target.value)}
                        required
                    />
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="timId"
                        label="Tim ID"
                        type="number"
                        value={timId}
                        onChange={(e) => setTimId(e.target.value)}
                        required
                    />
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="vrijemePocetka"
                        label="Vrijeme početka"
                        type="datetime-local"
                        value={vrijemePocetka}
                        onChange={(e) => setVrijemePocetka(e.target.value)}
                        required
                        InputLabelProps={{ shrink: true }}
                    />
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="vrijemeKraja"
                        label="Vrijeme kraja"
                        type="datetime-local"
                        value={vrijemeKraja}
                        onChange={(e) => setVrijemeKraja(e.target.value)}
                        required
                        InputLabelProps={{ shrink: true }}
                    />
                     {/* <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="brojSlobodnihMjesta"
                        label="Broj slobodnih mjesta"
                        type="number"
                        value={brojSlobodnihMjesta}
                        onChange={(e) => setBrojSlobodnihMjesta(e.target.value)}
                        required
                    />  */}
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="potrebanBrojIgraca"
                        label="Potreban broj igrača"
                        type="number"
                        value={potrebanBrojIgraca}
                        onChange={handlePotrebanBrojIgraca}
                        required
                    />
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="maxBrojIgraca"
                        label="Max broj igrača"
                        type="number"
                        value={maxBrojIgraca}
                        onChange={handleMaxBrojIgraca}
                        required
                    />
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="nivoVjestine"
                        label="Nivo vještine"
                        type="number"
                        value={nivoVjestine}
                        onChange={(e) => setNivoVjestine(e.target.value)}
                        required
                    />
                    <TextField
                        className="input"
                        sx={{ margin: '2% auto' }}
                        id="lokacijaTima"
                        label="Lokacija tima"
                        type="text"
                        value={lokacijaTima}
                        onChange={(e) => setLokacijaTima(e.target.value)}
                        required
                    />
                    <div className='poslovni-switch' id="sw">
                        <label>Privatni termin</label>
                        
                            
                        <Switch
                            checked={jeLiPrivatni}
                            onChange={(e) => setJeLiPrivatni(e.target.checked)}
                            inputProps={{ 'aria-label': 'controlled' }}
                        />
                    </div>
                    <Button type="submit" variant="contained" color="primary" className='submit'id="dugme" sx={{ margin: '2% auto' }}>
                        Kreiraj termin
                    </Button>
                </FormControl>
            </form>
        </div>
    );
};

export default TerminForm;
