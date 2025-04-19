import React, { useState, useEffect } from 'react';
import { getApiUrl } from '../config/api';
import './Activities.css';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(getApiUrl('activities'))
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="activities-container">
      <h2>Activities</h2>
      <div className="activities-grid">
        {activities.map(activity => (
          <div key={activity._id} className="activity-card">
            <h3>{activity.activity_type}</h3>
            <p>Duration: {activity.duration}</p>
            <p>User: {activity.user}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Activities;