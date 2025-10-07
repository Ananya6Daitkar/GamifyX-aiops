const express = require('express');
const app = express();
const port = process.env.PORT || 4000;

app.get('/api/status', (req, res) => {
  res.json({status: 'ok', env: process.env.NODE_ENV || 'dev'});
});

app.get('/api/leaderboard', (req, res) => {
  res.json({
    leaderboard: [
      {name: "Alice", prs: 12, score: 95},
      {name: "Bob", prs: 8, score: 78},
      {name: "You", prs: 1, score: 50}
    ]
  });
});

app.listen(port, () => console.log(`Backend listening on ${port}`));
