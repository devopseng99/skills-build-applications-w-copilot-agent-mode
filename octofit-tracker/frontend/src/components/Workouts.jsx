import React, { useState, useEffect } from 'react';
import { getApiUrl } from '../config/api';
import './Workouts.css';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(getApiUrl('workouts'))
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="workouts-container">
      <h2>Workouts</h2>
      <div className="workouts-grid">
        {workouts.map(workout => (
          <div key={workout._id} className="workout-card">
            <h3>{workout.name}</h3>
            <p>{workout.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;