/* Library import */
import { useState, useEffect } from "react";
import axios from "axios";

/* Dependency import */
import "./css/Recommend.css";

/* Component import */

/* Asset imports */
const baseURL = "http://127.0.0.1:8000/";

function Recommend({ username, setUsername, dataSubmitted, setDataSubmitted }) {
  const [qData, setqData] = useState("no data");

  useEffect(() => {

    const getRecommendations = async () => {
        let url = baseURL + "update_recommended_questions/" +  username ;
        const {data} = await axios.get(url);
        setqData(data);
    }
    getRecommendations();

  }, [dataSubmitted]);

  return <div className="Recommend">
      <h2>Questions</h2>
     {(dataSubmitted && qData!=="no data" )? (qData.questions.map(ques=><a key={ques[0]} href={ques[3]} target="_blank">{ques[0]}</a>) ): "no data"}
  </div>;
}

export default Recommend;
