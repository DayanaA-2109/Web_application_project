import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import UserDashboardPage from './pages/UserDashboardPage';
import Dashboard from './pages/Dashboard';

import './App.css';

function App() {

    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        const storedUser = localStorage.getItem("user");

        if (storedUser) {

            try {
                setUser(JSON.parse(storedUser));
            } catch (e) {
                localStorage.removeItem("user");
                localStorage.removeItem("token");
            }

        }

        setLoading(false);

    }, []);

    const handleLogin = (userData) => {

        setUser(userData);

    };

    const handleLogout = () => {

        localStorage.removeItem("user");
        localStorage.removeItem("token");

        setUser(null);

    };

    if (loading) {

        return (
            <div className="app-loading">
                <div className="app-loader"></div>
                <p>Loading...</p>
            </div>
        );

    }

    if (!user) {

        return <LoginPage onLogin={handleLogin} />;

    }

    return (

        <Router>

            <Routes>

                <Route
                    path="/"
                    element={
                        user.role === "ecommerce"
                            ? <Navigate to="/dashboard" />
                            : user.role === "user"
                                ? <Navigate to="/user/dashboard" />
                                : user.role === "admin"
                                    ? <Navigate to="/admin/dashboard" />
                                    : <Navigate to="/delivery/dashboard" />
                    }
                />

                <Route
                    path="/dashboard"
                    element={<Dashboard onLogout={handleLogout} />}
                />

                <Route
                    path="/user/dashboard"
                    element={<UserDashboardPage />}
                />

                <Route
                    path="/admin/dashboard"
                    element={
                        <div className="dashboard-placeholder">
                            <h2>👑 Admin Dashboard</h2>
                            <p>Coming Soon...</p>
                        </div>
                    }
                />

                <Route
                    path="/delivery/dashboard"
                    element={
                        <div className="dashboard-placeholder">
                            <h2>🚚 Delivery Agent Dashboard</h2>
                            <p>Coming Soon...</p>
                        </div>
                    }
                />

            </Routes>

        </Router>

    );

}

export default App;