import React from "react";
import { Box, List, ListItem, ListItemIcon, ListItemText, colors } from "@mui/material";
import MessageIcon from '@mui/icons-material/Message';
import RecentActorsIcon from '@mui/icons-material/RecentActors';
import InfoIcon from '@mui/icons-material/Info';


    //nisam dodao path jer nema stranica
const Sidebar = () => {
    const menuItems =[
        {
            text: 'Poruke',
            icon: <MessageIcon style={{ color: 'white' }}/>,
            path: '/',

        },
        {
            text: 'Moji termini',
            icon: <RecentActorsIcon style={{ color: 'white' }}/>,
            path: '/',

        },
        {
            text: 'O nama',
            icon: <InfoIcon style={{ color: 'white' }}/>,
            path: '/',

        }
    ]

    return(
        <Box style={{"background-image": "linear-gradient(to bottom, #333333, #808080)"}} flex={1} p={2} sx={{display: {xs: "none", sm: "block"}}} >
           <List>
                {menuItems.map(item =>(
                    <ListItem
                        button
                        key={item.text}
                        //onClick={}
                        >
                        <ListItemIcon>{item.icon}</ListItemIcon>
                        <ListItemText primary={item.text}/>
                    </ListItem>
                ))}
            
            </List> 
        </Box>

    );

};
export default Sidebar;