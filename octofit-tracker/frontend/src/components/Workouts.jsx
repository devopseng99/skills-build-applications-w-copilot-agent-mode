import React, { useEffect, useState } from 'react';
import './Workouts.css';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(`${window.BASE_API_URL}workouts/`)
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="workouts-container">
      <header className="workouts-header">
        <h1>Workouts</h1>
        <p>Explore a variety of workouts tailored for you!</p>
      </header>
      <div className="workouts-grid">
        {workouts.map((workout) => (
          <div className="workout-card" key={workout.id}>
            <h3 className="workout-title">{workout.name}</h3>
            <p className="workout-description">{workout.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;