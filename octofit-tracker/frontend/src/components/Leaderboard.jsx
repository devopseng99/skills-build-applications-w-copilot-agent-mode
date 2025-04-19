import React, { useEffect, useState } from 'react';
import './Leaderboard.css';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(`${window.BASE_API_URL}leaderboard/`)
      .then(response => response.json())
      .then(data => setLeaderboard(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="leaderboard-container">
      <header className="leaderboard-header">
        <h1>Leaderboard</h1>
        <p>See how you rank among other users in OctoFit Tracker!</p>
      </header>
      <div className="leaderboard-grid">
        {leaderboard.map((entry) => (
          <div className="leaderboard-card" key={entry.id}>
            <h3 className="leaderboard-user">{entry.user}</h3>
            <p className="leaderboard-points">{entry.points} points</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Leaderboard;