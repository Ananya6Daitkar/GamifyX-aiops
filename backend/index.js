const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const DATA_DIR = path.join(__dirname, 'data');
if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR);
const DB = path.join(DATA_DIR, 'learners.json');
if (!fs.existsSync(DB)) fs.writeFileSync(DB, '[]', 'utf8');

const readDB = () => JSON.parse(fs.readFileSync(DB,'utf8'));
const writeDB = (d) => fs.writeFileSync(DB, JSON.stringify(d, null, 2), 'utf8');

const app = express();
app.use(bodyParser.json());

app.post('/api/learners', (req,res) => {
  const { id, name, prs = 0, score = 0 } = req.body;
  const db = readDB();
  const idx = db.findIndex(x => x.id === id);
  if (idx >= 0) db[idx] = {...db[idx], prs, score};
  else db.push({ id, name, prs, score, badges: [] });
  writeDB(db);
  return res.json({ ok: true });
});

app.get('/api/leaderboard', (req,res) => {
  const db = readDB();
  db.sort((a,b) => b.score - a.score);
  res.json({ leaderboard: db });
});

app.get('/api/status', (req,res) => res.json({ status: 'ok' }));

// Export app for tests. Start only when called directly.
if (require.main === module) {
  const port = process.env.PORT || 4000;
  app.listen(port, ()=> console.log(`Listening ${port}`));
}
module.exports = app;
