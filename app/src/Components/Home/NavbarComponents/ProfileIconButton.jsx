import React, { useState } from "react";
import IconButton from '@mui/material/IconButton';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

const ProfileIconButton = () => {
    const [anchorEl, setAnchorEl] = useState(null);

    const handleMenuOpen = (event) => {
        setAnchorEl(event.currentTarget);
    };
    
    const handleMenuClose = () => {
        setAnchorEl(null);
    };
    //nisam imao na sta dodati path za My Account
    return (
        <div>
            <IconButton
                aria-label="account"
                onClick={handleMenuOpen}
            >
                <AccountCircleIcon style={{ color: '#fff' }} />
            </IconButton>
            <Menu
                anchorEl={anchorEl}
                open={Boolean(anchorEl)}
                onClose={handleMenuClose}
            >
                <MenuItem onClick={handleMenuClose}>My Account</MenuItem>
                <MenuItem onClick={handleMenuClose}>Log Out</MenuItem>
            </Menu>
        </div>
    );
};

export default ProfileIconButton;
