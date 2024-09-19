

import { useState } from 'react';
import './App.css';

function App() {
  const [reloadKey, setReloadKey] = useState(0);
  const [idea, setIdea] = useState('');
  const [frontendSuggestion, setFrontendSuggestion] = useState('');
  const [additionalChanges, setAdditionalChanges] = useState('');

  const handleAdditionalSubmit = async () => {
    try {
      const response = await fetch("http://localhost:4000/change_frontend", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: additionalChanges
        })
      });

      const data = await response.json();
      console.log(data); // Check the response data

      await fetch("http://localhost:2008/make_change", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
    } catch (error) {
      console.error('Error submitting additional changes:', error);
    }
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch("http://localhost:4000/code", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: idea,
          front: frontendSuggestion
        })
      });

      const data = await response.json();
      console.log(data); // Check the response data

      await fetch("http://localhost:2008/make_change", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
    } catch (error) {
      console.error('Error submitting idea:', error);
    }
  };

  return (
    <div className='w-screen h-screen flex justify-center items-center'>
      <div className='flex w-[90vw] h-[60vh] justify-around items-center flex-wrap'>
        <iframe
          key={reloadKey}
          src="http://localhost:5173"
          title="Embedded Website"
          className='h-[50vh] w-[50vw] rounded-lg shadow-xl'
        />
        <div className='w-[30vw] h-[50vh] flex flex-col justify-around'>
          <div className='flex flex-col justify-center items-center w-[30vw] h-[30vh] bg-[#333333] rounded-lg shadow-xl p-4'>
            <h1 className='text-2xl font-bold mb-4'>
              Convert your ideas to full stack website
            </h1>
              <button
                onClick={() => window.location.href = 'http://localhost:5173/'}
                className='w-full mb-4 p-2 bg-blue-500 text-white rounded'
              >
                Go to your website
              </button>
            <input
              type="text"
              placeholder="Your Idea"
              value={idea}
              onChange={(e) => setIdea(e.target.value)}
              className='w-full p-2 mb-4 rounded'
            />
            <input
              type="text"
              placeholder="Frontend Suggestion"
              value={frontendSuggestion}
              onChange={(e) => setFrontendSuggestion(e.target.value)}
              className='w-full p-2 mb-4 rounded'
            />
            <button
              onClick={handleSubmit}
              className='w-full p-2 bg-red-500 text-white rounded'
            >
              Submit
            </button>
          </div>
          <div className='flex flex-col justify-center items-center w-[30vw] h-[14vh] bg-[#333333] rounded-lg shadow-xl p-4'>
            <input
              type="text"
              placeholder="Additional Frontend Changes"
              value={additionalChanges}
              onChange={(e) => setAdditionalChanges(e.target.value)}
              className='w-full p-2 mb-2 rounded'
            />
            <button
              onClick={handleAdditionalSubmit}
              className='w-full p-2 bg-red-500 text-white rounded'
            >
              Submit Changes
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

