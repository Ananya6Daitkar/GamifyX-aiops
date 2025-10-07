export default function Home() {
  return (
    <main style={{fontFamily:'Arial, sans-serif', padding:24}}>
      <h1>Gamifyx — AIOps Demo (placeholder)</h1>
      <p>This is a small demo frontend for the Assignment. It shows:</p>
      <ul>
        <li>Leaderboard (mock)</li>
        <li>Buttons to create a demo PR (locally simulated)</li>
        <li>Link to backend API</li>
      </ul>
      <p>API endpoint: <a href="/api/leaderboard">/api/leaderboard</a></p>
    </main>
  )
}
