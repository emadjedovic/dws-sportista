import React from 'react';
import './Home.css';
import Feed from '../../Components/Home/Feed';
import Sidebar from '../../Components/Home/Sidebar';
import Navbar from '../../Components/Home/Navbar';
import { Box, Stack } from '@mui/material';

// komponenta koja sadrži opis projekta, svrhu aplikacije i autore

function Home() {
  return (
    <Box>
      <Navbar/>
      <Stack direction={'row'} spacing={1} justifyContent={'space-between'}>
        <Feed/>
        <Sidebar/>

      </Stack>
    </Box>
  );
}

export default Home;
