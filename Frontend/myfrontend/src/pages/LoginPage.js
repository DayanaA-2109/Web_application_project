import React, { useState } from 'react';
import '../css/login.css';

const LoginPage = ({ onLogin }) => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        role: 'user'
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const roles = [
        { value: 'user', label: 'User (Customer)', icon: 'fa-user' },
        { value: 'admin', label: 'Admin', icon: 'fa-user-shield' },
        { value: 'ecommerce', label: 'E-Commerce', icon: 'fa-store' },
        { value: 'delivery', label: 'Delivery Agent', icon: 'fa-truck' }
    ];

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        // Simulate login - Replace with actual API call
        setTimeout(() => {
            // Store user info in localStorage
            const user = {
                id: 1,
                name: formData.role === 'user' ? 'John Doe' :
                       formData.role === 'admin' ? 'Admin User' :
                       formData.role === 'ecommerce' ? 'E-Commerce User' : 'Delivery Agent',
                email: formData.email,
                role: formData.role,
                token: 'dummy-token-123'
            };

            localStorage.setItem('user', JSON.stringify(user));
            localStorage.setItem('token', user.token);

            // Call the onLogin callback
            if (onLogin) {
                onLogin(user);
            }

            setLoading(false);
        }, 1000);
    };

    return (
        <div className="login-page-container">
            <div className="login-page-card">
                <div className="login-page-header">
                    <div className="login-page-logo">
                        <i className="fas fa-box"></i>
                        <span>Ship<span>Xpress</span></span>
                    </div>
                    <p>Sign in to your account</p>
                </div>

                <form onSubmit={handleSubmit} className="login-page-form">
                    <div className="login-page-form-group">
                        <label>Email Address</label>
                        <div className="login-page-input-wrapper">
                            <i className="fas fa-envelope"></i>
                            <input
                                type="email"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                placeholder="Enter your email"
                                required
                            />
                        </div>
                    </div>

                    <div className="login-page-form-group">
                        <label>Password</label>
                        <div className="login-page-input-wrapper">
                            <i className="fas fa-lock"></i>
                            <input
                                type="password"
                                name="password"
                                value={formData.password}
                                onChange={handleChange}
                                placeholder="Enter your password"
                                required
                            />
                        </div>
                    </div>

                    <div className="login-page-form-group">
                        <label>Login as</label>
                        <div className="login-page-role-selector">
                            {roles.map((role) => (
                                <label
                                    key={role.value}
                                    className={`login-page-role-option ${formData.role === role.value ? 'active' : ''}`}
                                >
                                    <input
                                        type="radio"
                                        name="role"
                                        value={role.value}
                                        checked={formData.role === role.value}
                                        onChange={handleChange}
                                    />
                                    <i className={`fas ${role.icon}`}></i>
                                    <span>{role.label}</span>
                                </label>
                            ))}
                        </div>
                    </div>

                    {error && (
                        <div className="login-page-error">
                            <i className="fas fa-exclamation-circle"></i>
                            {error}
                        </div>
                    )}

                    <button
                        type="submit"
                        className="login-page-btn"
                        disabled={loading}
                    >
                        {loading ? (
                            <>
                                <i className="fas fa-spinner fa-spin"></i>
                                Signing in...
                            </>
                        ) : (
                            <>
                                <i className="fas fa-sign-in-alt"></i>
                                Sign In
                            </>
                        )}
                    </button>
                </form>

                <div className="login-page-footer">
                    <p>Demo Credentials:</p>
                    <div className="login-page-demo-creds">
                        <span>Email: user@demo.com</span>
                        <span>Password: password123</span>
                    </div>
                    <div style={{ marginTop: '8px', fontSize: '12px', color: '#94a3b8' }}>
                        Select a role and click Sign In
                    </div>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;