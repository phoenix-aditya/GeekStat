import { useState , useEffect} from 'react';
//import Graph from './components/graph'
import './App.css';
import axios from './components/axios';
import {Router, Route, Routes} from 'react-router-dom';
// import MyForm from './form';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'

import { Line } from 'react-chartjs-2'
import { render } from '@testing-library/react';
import MyForm from './form';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

function App() {

  const [question, setQuestion] = useState([]);
  const [gra, setGra] = useState([]);
  const [username,setUsername] = useState('parvg555');
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }
  const handleSubmit = (event) => {
    event.preventDefault();
    <Routes />
    // console.log(inputs.SPOJ);
    // console.log(inputs.atcoder);
    // console.log(inputs.Codeforces);

  }

  useEffect (() => {
    async function fetchData(){
        const req = await axios.get(`recommendq/${username}`);
        const req1 = await axios.get(`genuser/${username}`);
        setQuestion(req.data.questions);
        // req1.data.data.cf_graph.map((item,i)=>{
        //   //console.log(item)
        //     return setGra(s => {
        //       [
        //         ...s,
        //         item
        //       ]
        //     })
        // });
        //console.log(req1.data.data.cf_graph);
    }
    fetchData();
},[])


return (
      <div>
      <h1 className='h69'>GEEKSTAT</h1>
      <div className='App'>
      <div className='card1'>
      <div>

      <form onSubmit={handleSubmit}>
      <label>SPOJ
        <input
            id="2"
          type="text"
          name="SPOJ"
          value={inputs.SPOJ || ""}
          onChange={handleChange}
        />
        </label>
        <label>Codeforces
        <input
          type="text"
          name="Codeforces"
          value={inputs.Codeforces || ""}
          onChange={handleChange}
        />
        </label>
        <label>atcoder
        <input
          type="text"
          name="atcoder"
          value={inputs.atcoder || ""}
          onChange={handleChange}
        />
        </label>
        <input type="submit" />
    </form>

      </div>
      <div>
      <Line
      data={
        {
labels: ['', '',''],
datasets: [
{
  label: 'Rating',
  fill: false,
  lineTension: 0.5,
  backgroundColor: 'rgba(75,192,192,1)',
  borderColor: 'rgba(0,0,0,1)',
  borderWidth: 2,
  data: [66,76,44],
  fill: false
}
]
}
      }
      options={{
        title:{
          display:true,
          text:'Average Rainfall per month',
          fontSize:20
        },
        legend:{
          display:true,
          position:'right'
        }
      }}
    />
    </div>
      </div>
          <div className="card2">
            <div>
            <h3> Suggested questions</h3>
            <div className='scroller'>
            {question.map(i=>
            <div className = "cointainer"><p> <a href={i[3]}>{i[0]}</a></p></div>
            )}</div>
            </div>
          </div>
      </div>
      </div>
  )
}

export default App;