import React, { useState, useEffect } from 'react';
import { getApiUrl } from '../config/api';
import './Teams.css';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(getApiUrl('teams'))
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="teams-container">
      <h2>Teams</h2>
      <div className="teams-grid">
        {teams.map(team => (
          <div key={team._id} className="team-card">
            <h3>{team.name}</h3>
            <div className="team-members">
              <h4>Members</h4>
              <ul>
                {team.members.map(member => (
                  <li key={member._id}>{member.username}</li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Teams;