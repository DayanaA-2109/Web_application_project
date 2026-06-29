import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import UserDashboardPage from './pages/UserDashboardPage';

// Import your existing e-commerce dashboard
import Dashboard from './pages/Dashboard';

import './App.css';

function App() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Check if user is logged in
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            try {
                setUser(JSON.parse(storedUser));
            } catch (e) {
                localStorage.removeItem('user');
                localStorage.removeItem('token');
            }
        }
        setLoading(false);
    }, []);

    const handleLogin = (userData) => {
        setUser(userData);
        // Redirect will happen in the component
    };

    const handleLogout = () => {
        localStorage.removeItem('user');
        localStorage.removeItem('token');
        setUser(null);
        // Force refresh to login page
        window.location.href = '/';
    };

    if (loading) {
        return (
            <div className="app-loading">
                <div className="app-loader"></div>
                <p>Loading...</p>
            </div>
        );
    }

    // If no user, show login page
    if (!user) {
        return <LoginPage onLogin={handleLogin} />;
    }

    // User is logged in - show dashboard based on role
    return (
        <Router>
            <div className="app-container">
                {/* Logout Button */}
                <button
                    className="logout-btn"
                    onClick={handleLogout}
                >
                    <i className="fas fa-sign-out-alt"></i>
                    Logout ({user.role})
                </button>

                <Routes>
                    <Route path="/" element={
                        user.role === 'ecommerce' ? <Navigate to="/dashboard" /> :
                        user.role === 'user' ? <Navigate to="/user/dashboard" /> :
                        user.role === 'admin' ? <Navigate to="/admin/dashboard" /> :
                        <Navigate to="/user/dashboard" />
                    } />

                    {/* Friend's E-Commerce Dashboard */}
                    <Route path="/dashboard" element={<Dashboard />} />

                    {/* Your User Dashboard */}
                    <Route path="/user/dashboard" element={<UserDashboardPage />} />

                    {/* Admin Dashboard (Coming Soon) */}
                    <Route path="/admin/dashboard" element={
                        <div className="dashboard-placeholder">
                            <h2>👑 Admin Dashboard</h2>
                            <p>Coming Soon...</p>
                        </div>
                    } />

                    {/* Delivery Agent Dashboard (Coming Soon) */}
                    <Route path="/delivery/dashboard" element={
                        <div className="dashboard-placeholder">
                            <h2>🚚 Delivery Agent Dashboard</h2>
                            <p>Coming Soon...</p>
                        </div>
                    } />
                </Routes>
            </div>
        </Router>
    );
}

export default App;