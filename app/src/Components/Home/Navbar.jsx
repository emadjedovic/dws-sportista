import React from "react";
import { AppBar, Toolbar, Typography, styled, Box, InputBase} from "@mui/material";
import SportsHandball from "@mui/icons-material/SportsHandball";
import DodajTerminButton from "./NavbarComponents/DodajTerminButton";
import ProfileIconButton from "./NavbarComponents/ProfileIconButton";


const StyledToolbar = styled(Toolbar)({
    display: "flex",
    justifyContent: "space-between",
    
});



const Search = styled("div")(({theme}) => ({
    backgroundColor: "white",
    padding: "0px 10px",
    width: "30%",
    borderRadius: theme.shape.borderRadius
}));

//Dodaj termin i profil ikonica (buttoni)
const Icons = styled(Box)(({theme}) => ({
    display : "flex"

}));
                        //Main function
const Navbar = () => {

    return(
        <AppBar style={{"background-image": "linear-gradient(to left, #333333, #808080)"}} position="sticky">
            <StyledToolbar>
                <div style={{ display: "flex", alignItems: "center" }}>
                    <SportsHandball sx={{ display: { xs: "block", sm: "block", md: "block", margin: "0 10px" } }} />
                    <Typography variant="h5" sx={{ display: { xs: "none", sm: "block" } }}>
                        Sportista
                    </Typography>


                </div>

                <Search>
                    <InputBase placeholder="Pretrazite..."/>
                </Search>
                
                <Icons>
                    <DodajTerminButton/>
                    <ProfileIconButton/>
                </Icons>
            </StyledToolbar>
        </AppBar>

    );

};
export default Navbar;