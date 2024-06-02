/* Library import */
import {useState,useEffect} from 'react';
import axios from 'axios';
/* Dependency import */
import './css/UserData.css';

/* Component import */

/* Asset imports */
const baseURL = "https://geekstat-api.herokuapp.com/";


function UserData({username, setUsername, dataSubmitted, setDataSubmitted}){
    const [qData, setqData] = useState("no data");

  

        return(
            <div className='UserData'>
            <h1>hello</h1>
            </div>
        );
}

export default UserData;