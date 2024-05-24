import React from "react";
import PostAddIcon from '@mui/icons-material/PostAdd';
import IconButton from '@mui/material/IconButton';

const DodajTerminButton = () => {
    //nije implementirano kreiranje termina
    return(
        <IconButton 
        //onClick={}
        aria-label="delete" >
        
        <PostAddIcon style={{ color: '#fff' }} />
    </IconButton>

    );

};
export default DodajTerminButton;