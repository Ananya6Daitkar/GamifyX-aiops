export default function handler(req, res) {
  res.setHeader('Content-Type','application/json');
  res.status(200).json({
    leaderboard: [
      {name: "Alice", prs: 12, score: 95},
      {name: "Bob", prs: 8, score: 78},
      {name: "You", prs: 1, score: 50}
    ]
  })
}
