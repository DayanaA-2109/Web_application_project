// api.js - FIXED
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // ← Change from 3000 to 8000
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
});

export default api;