const express     = require('express');
const cors        = require('cors');
const bodyParser  = require('body-parser');
const MongoClient = require('mongodb').MongoClient;
const ObjectId    = require('mongodb').ObjectId;

const app         = express();
const port        = 3001;

app.use(bodyParser.json()); // json to be used
app.use(cors());

const mongoUrl    = 'mongodb+srv://anna:1AQ2ZS3ED@cluster0.pysxbay.mongodb.net/?retryWrites=true&w=majority';
const dbName      = 'telegram';

let db;

const connectToDB = async () => {
  const client = await MongoClient.connect(mongoUrl, { useNewUrlParser: true, useUnifiedTopology: true });
  db = client.db(dbName);
  console.log('Connected to MongoDB.');

  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
  });
}

app.post('/saveChannel', async (req, res) => {
  try {
    let { channelId } = req.body;
    channelId = parseInt(channelId, 10);
    if (isNaN(channelId)) {
      throw new Error('Invalid channelId');
    }
    await db.collection('channels').insertOne({ channelId });
    res.json({ success: true });
  } catch (error) {
    res.json({ success: false, message: error.message });
  }
});

app.get('/channels', async (req, res) => {
  try {
    const docs = await db.collection('channels').find({}).limit(100).toArray();
    res.json(docs);
  } catch (error) {
    res.status(500).send('Server Error');
  }
});

app.get('/relations', async (req, res) => {
  const docs = await db.collection('channels_similarity').find({}).limit(100).toArray();
  res.json(docs);
});


// Learning :
app.get('/message/:id', async (req, res) => {
  const id = req.params.id;
  const doc = await db.collection('messages').findOne({ _id: new ObjectId(id) });
  res.json(doc);
});

app.get('/all_messages', async (req, res) => {
  const docs = await db.collection('messages').find({}).limit(100).toArray();
  res.json(docs);
});

app.get('/characteristics', async (req, res) => {
  const docs = await db.collection('characteristics').find({}).limit(100).toArray();
  res.json(docs);
});

app.post('/update/:id', async (req, res) => {
  const id = req.params.id;
  await db.collection('messages').updateOne({ _id: new ObjectId(id) }, { $set: req.body });
  res.json({ success: true });
});


// Centralized error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

connectToDB().catch(err => console.error('Failed to connect to the database', err));