/* Library import */
import { useState, useEffect } from "react";

/* Dependency import */
import "./css/mainContentConatiner.css";
import RatingChart from "./RatingChart";
import Recommend from "./Recommend";
import UserData from "./UserData";
/* Component import */

/* Asset imports */

function MainContentConatiner({
  username,
  setUsername,
  dataSubmitted,
  setDataSubmitted,
}) {
  return (
    <div className="mainContentConatiner">
      <div className="baharWalaDiv">
        <div className="smallContainer">Hello</div>
        <div className="smallContainer">Hello</div>
        <div className="smallContainer">Hello</div>
        <div className="smallContainer">Hello</div>
      </div>

      <div className="baharWalaDiv">
          
        <div className="container">
          <h1>hello</h1>
          <RatingChart
            username={username}
            setUsername={setUsername}
            dataSubmitted={dataSubmitted}
            setDataSubmitted={setDataSubmitted}
          />
        </div>

        <div className="container">
          <Recommend
            username={username}
            setUsername={setUsername}
            dataSubmitted={dataSubmitted}
            setDataSubmitted={setDataSubmitted}
          />
        </div>

      </div>
    </div>
  );
}

export default MainContentConatiner;
