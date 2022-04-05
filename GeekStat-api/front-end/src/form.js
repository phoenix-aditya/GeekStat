import { useState } from "react";
import ReactDOM from "react-dom";

function MyForm() {
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(inputs.username);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
      <input
        id="1"
        type="text"
        name="username"
        value={inputs.username || ""}
        onChange={handleChange}
      />
      </label>
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
  )
}

export default MyForm;