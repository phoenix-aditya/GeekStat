/* Library import */
import { useState, useEffect } from "react";

/* Dependency import */
import "./css/navbar.css";

/* Component import */
import SearchIcon from "@mui/icons-material/Search";
import CloseIcon from '@mui/icons-material/Close';
import { IconButton } from '@mui/material';

/* Asset imports */
import Logo from "../assets/img/logo.svg";

function Navbar({
    username, setUsername, dataSubmitted, setDataSubmitted
}) {
  // const varname, change karne ka fn, initial value
  // use state to declare variable
  
  const getUserData = () => {
    document.getElementsByClassName('searchFormInput')[0].style.width = username.length + "ch";
    var tempState = document.getElementsByClassName('searchFormInput')[0].value.length > 0;
    document.getElementsByClassName('searchFormInput')[0].disabled = tempState;
    setDataSubmitted(true);
    console.log("user data fn called");
  };

  const resetUserData = () => {
    document.getElementsByClassName('searchFormInput')[0].style.width = "250px";
    document.getElementsByClassName('searchFormInput')[0].disabled = false;
    setUsername("");
    setDataSubmitted(false);
  }

  return (
    <div className="navbar">
        {/* <div className="navItemDiv">
            <div className="navItem">
                home
            </div>
            <div className="navItem">
                home
            </div>
            <div className="navItem">
                home
            </div>
        </div> */}
      <div className="logo">
        <img src={Logo}></img>
      </div>
      <div className="searchBar">
        
          <form

            className="searchForm"
            onSubmit={(e) => {
              e.preventDefault();
              getUserData();
            }}
          >
            
            <input
                className="searchFormInput"
              type="text"
              placeholder="username"
              onChange={(e) => {
                setUsername(e.target.value);
              }}
              // lets input access the value in the variable username
              value={username}
            />
            <IconButton>
            {
                (!dataSubmitted)?(
                    <SearchIcon
                        fontSize="small"
                        onClick={() => {
                            getUserData();
                        }}
                    />
                ):(
                    <CloseIcon
                        fontSize="small"
                        onClick={() => {
                            resetUserData();
                        }}
                    />
                )
            }
            </IconButton>
          </form>
      </div>

      {/* <div className='rightOptions'>
                <div className='navOption'>
                    Porky
                </div>
            </div> */}
    </div>
  );
}

export default Navbar;

// used when we the page is loaded, so used once
//   useEffect(() => {
//     console.log(username)
//   }, [])

//   used when we can afford the promise being returned later
//   useEffect(() => {
//     console.log(username)
//   }, [username])

// runs all the time so dont use
// useEffect(() => {

// })

//   runs when we need a promise to be returned immediately
//   useEffect(() => {
//     return () => {
//       console.log('vaibhav')
//     }
//   }, [username])
