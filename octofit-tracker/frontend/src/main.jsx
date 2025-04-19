import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// Set the base API URL from environment variables or default to '/api/v1/'
const BASE_API_URL = import.meta.env.VITE_BASE_API_URL || '/api/v1/';

// Make the base API URL globally accessible
window.BASE_API_URL = BASE_API_URL;

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
