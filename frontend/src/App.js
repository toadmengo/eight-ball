import './App.css';
import React, { useEffect, useState } from 'react';


// const url = 'http://127.0.0.1:5000/ask?question='
const url = 'https://magic-eight-ball.herokuapp.com/ask?question='

function MagicEightBall() {

  useEffect(() => {
    document.title = 'Magic eight ball';
  });
  
  const [userInput, setUserInput] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const ask = async () => {
    setLoading(true);
    const response = await fetch(url + userInput);
    const data = await response.json(); //extract JSON from the http response
    console.log(data)
    setAnswer(data.message)
    setLoading(false)
  }

  const handleChange = (event) => {
    setUserInput(event.target.value)
  }

  let body = (answer !== '' && !loading) ? answer : <div className='eight'>8</div>

  return (
    <div>
      <div className='header-container'>
        <h1>Magic Eight Ball</h1>
        <p>Please don't take this seriously...</p>
      </div>
      <br/>
      <div className={`ball-container`}>
        <div className={`ball-black-outer ${loading ? "shaking" : "bouncing"}`}>
          <div className="ball-white-inner">
            <div>
              {body}
            </div>
          </div>
        </div>
        <div className={`ball-shadow ${loading ? "" : "scale"}`}></div>
      </div>

      <div className="question-container">
        <input
          type="text"
          value={userInput}
          onChange={handleChange}
          disabled={loading}
          />
        <button onClick={ask}>
          Ask the Magic Eight Ball!
        </button>
      </div>
      
    </div>
  );
  
};

export default function App() {
  return(
    <MagicEightBall/>
  )
}
