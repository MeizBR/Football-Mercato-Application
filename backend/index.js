const express = require("express");
const cors = require("cors");

require("dotenv").config();

const host = process.env.MONGODB_HOST;
const database = process.env.MONGODB_DATABASE;
const user = process.env.MONGODB_USER;
const password = process.env.MONGODB_PASSWORD;

const { MongoClient } = require('mongodb');

const client = new MongoClient(`mongodb+srv://${user}:${password}@${host}/${database}?retryWrites=true&w=majority`);

const app = express();

app.use(express.json());
app.use(cors());

// routes
app.get("/", (req, res) => {
  res.json({ status: "API is running 🚀" });
});

app.get('/api/transfers', async (req, res) => {
  try {
    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection('transfers');

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/tuttoMercato/getLatestNews', async (req, res) => {
  try {
    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection('tuttomercato-news');

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/transfermarkt/getPlayersList/:league', async (req, res) => {
  try {
    const league = req.params.league;

    const collectionName = league.concat('', '-players-list')

    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection(collectionName);

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/newsAPI/getLatestNews', async (req, res) => {
  try {
    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection('news-api-results');

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/transfermarkt/getLatestRumours', async (req, res) => {
  try {
    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection('transfermarkt-rumours-news');

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/transfermarkt/getTransfersHistory/:league', async (req, res) => {
  try {
    const league = req.params.league;

    const collectionName = league.concat('', '-transfers-history-football-apis')

    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection(collectionName);

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/transfermarkt/getLatestTransfers/:league', async (req, res) => {
  try {
    const league = req.params.league;

    const collectionName = league.concat('', '-latest-transfers')

    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection(collectionName);

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.get('/api/transfermarkt/getClubsList/:league', async (req, res) => {
  try {
    const league = req.params.league;

    const collectionName = league.concat('', '-clubs-list')

    await client.connect();

    const db = client.db('football-mercato');
    const collection = db.collection(collectionName);

    const data = await collection.find().toArray();

    res.json(data);

  } catch (err) {
    res.status(500).send(err.message);
  }
});

// server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
