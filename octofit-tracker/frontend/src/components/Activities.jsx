import React, { useEffect, useState } from 'react';
import './Activities.css';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(`${window.BASE_API_URL}activity/`)
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="activities-container">
      <header className="activities-header">
        <h1>Activities</h1>
        <p>Track and explore all activities logged in OctoFit Tracker!</p>
      </header>
      <div className="activities-grid">
        {activities.map((activity) => (
          <div className="activity-card" key={activity.id}>
            <h3 className="activity-type">{activity.type}</h3>
            <p className="activity-duration">{activity.duration} minutes</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Activities;