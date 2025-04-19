import React, { useEffect, useState } from 'react';
import './Users.css';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`${window.BASE_API_URL}users/`)
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div className="users-container">
      <header className="users-header">
        <h1>Users</h1>
        <p>Explore the list of registered users in OctoFit Tracker!</p>
      </header>
      <div className="users-grid">
        {users.map((user) => (
          <div className="user-card" key={user.id}>
            <h3 className="user-name">{user.name}</h3>
            <p className="user-email">{user.email}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Users;