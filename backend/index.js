const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 4000;

app.use(bodyParser.json());

let learners = [];

// Status endpoint
app.get('/api/status', (req, res) => {
  res.json({ status: 'ok' });
});

// Add a learner
app.post('/api/learners', (req, res) => {
  const { id, name, prs, score } = req.body;
  learners.push({ id, name, prs, score });
  res.json({ message: 'Learner added', learner: { id, name, prs, score } });
});

// Leaderboard
app.get('/api/leaderboard', (req, res) => {
  const sorted = learners.sort((a, b) => b.score - a.score);
  res.json(sorted);
});

app.listen(port, () => {
  console.log(`Listening ${port}`);
});

// Export app for Jest tests
module.exports = app;
