import React, { useEffect, useState } from 'react';
import './Teams.css';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(`${window.BASE_API_URL}teams/`)
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="teams-container">
      <header className="teams-header">
        <h1>Teams</h1>
        <p>Discover and join teams in OctoFit Tracker!</p>
      </header>
      <div className="teams-grid">
        {teams.map((team) => (
          <div className="team-card" key={team.id}>
            <h3 className="team-name">{team.name}</h3>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Teams;