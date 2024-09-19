import React, { useState, useEffect } from 'react';

function App() {
  const [solos, setSolos] = useState([]);

  useEffect(() => {
    fetch('http://localhost:2004/solos')
      .then(res => res.json())
      .then(data => setSolos(data))
      .catch(err => console.error('Error fetching solos:', err));
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Famous Guitar Solos</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {solos.map(solo => (
          <div key={solo._id} className="rounded-lg shadow-md p-4 bg-gradient-to-r from-cyan-500 to-purple-500 hover:from-cyan-700 hover:to-purple-700 transition duration-300 ease-in-out">
            <img src={solo.imageUrl} alt={solo.title} className="rounded-lg mb-2" />
            <h2 className="text-xl font-bold mb-1">{solo.title}</h2>
            <p className="text-gray-700">{solo.artist}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;