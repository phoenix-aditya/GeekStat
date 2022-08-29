/* Library import */
import {useState,useEffect} from 'react';

/* Dependency import */
import './css/main.css';
/* Component import */
import Navbar from './navbar';
import MainContentConatiner from './mainContentConatiner'
/* Asset imports */

function Main(){
    // change it back to "" & false below
    const [username, setUsername] = useState("parvg555");
    const [dataSubmitted, setDataSubmitted] = useState(false);
    return(
        <div className='main'>
            <Navbar
                username={username}
                setUsername={setUsername}
                dataSubmitted = {dataSubmitted}
                setDataSubmitted = {setDataSubmitted}
            />
            <MainContentConatiner
                username = {username}
                setUsername={setUsername}
                dataSubmitted = {dataSubmitted}
                setDataSubmitted = {setDataSubmitted}
            />
            
        </div>
    );
}

export default Main;