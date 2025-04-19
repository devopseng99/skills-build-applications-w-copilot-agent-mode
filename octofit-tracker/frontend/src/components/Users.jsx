import React, { useState, useEffect } from 'react';
import { getApiUrl } from '../config/api';
import './Users.css';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(getApiUrl('users'))
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div className="users-container">
      <h2>Users</h2>
      <div className="users-grid">
        {users.map(user => (
          <div key={user._id} className="user-card">
            <h3>{user.username}</h3>
            <p>Email: {user.email}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Users;