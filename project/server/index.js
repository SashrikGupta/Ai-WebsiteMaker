const express = require('express');
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

app.listen(port, () => console.log(`Server listening on port ${port}`));