
import os
import subprocess
def change_backend(index_js_content):
    os.chdir("project/server")
    with open('index.js', 'w') as file:
        file.write(index_js_content)
    subprocess.Popen(["node" , "index.js"], shell=True)
    os.chdir("../..")

def change_frontend(index_js_content):
    print(os.getcwd())
    os.chdir("project/client/src")
    with open('App.jsx', 'w') as file:
        file.write(index_js_content)
    with open('App.css', 'w') as file:
        file.write(" ")
    with open('index.css', 'w') as file:
        file.write(" ")
    os.chdir("../../..")

def change_backend_and_frontend(back, front):
    change_backend(back)
    change_frontend(front)

change_backend_and_frontend("""const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
const port = 2004;

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/guitar-solos', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Middleware
app.use(cors());
app.use(express.json());

// Models
const SoloSchema = new mongoose.Schema({
  title: { type: String, required: true },
  artist: { type: String, required: true },
  description: { type: String, required: true },
  tab: { type: String },
  imageUrl: { type: String }
});

const Solo = mongoose.model('Solo', SoloSchema);

// API routes
app.get('/solos', async (req, res) => {
  try {
    const solos = await Solo.find();
    res.json(solos);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching solos' });
  }
});

app.post('/solos', async (req, res) => {
  try {
    const newSolo = new Solo(req.body);
    await newSolo.save();
    res.status(201).json(newSolo);
  } catch (err) {
    res.status(400).json({ message: 'Error creating solo' });
  }
});

app.listen(port, () => console.log(`Server listening on port ${port}`));""", """import React, { useState, useEffect } from 'react';

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

export default App;""")
