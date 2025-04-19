import React, { useState, useEffect } from 'react';
import { getApiUrl } from '../config/api';
import './Teams.css';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(getApiUrl('teams'))
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams data:', data); // Debug log
        setTeams(data);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
        setError(error.message);
      });
  }, []);

  if (error) {
    return <div className="teams-container"><h2>Error: {error}</h2></div>;
  }

  return (
    <div className="teams-container">
      <h2>Teams</h2>
      <div className="teams-grid">
        {teams.map(team => (
          <div key={team.id || team._id} className="team-card">
            <h3>{team.name}</h3>
            <div className="team-members">
              <h4>Members</h4>
              <ul>
                {Array.isArray(team.members) 
                  ? team.members.map((member, index) => (
                      <li key={index}>{typeof member === 'string' ? member : member.name || member.email}</li>
                    ))
                  : typeof team.members === 'object' 
                    ? Object.values(team.members).map((member, index) => (
                        <li key={index}>{typeof member === 'string' ? member : member.name || member.email}</li>
                      ))
                    : <li>No members</li>
                }
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Teams;