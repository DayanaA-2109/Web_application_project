import React, { useState } from 'react';
import UserShipmentList from './UserShipmentList';
import UserTrackingModal from './UserTrackingModal';
import '../../css/User-DashBoard.css';

const UserDashboard = ({ shipments, loading, onRefresh }) => {
    const [selectedShipment, setSelectedShipment] = useState(null);
    const [showTrackingModal, setShowTrackingModal] = useState(false);
    const [searchQuery, setSearchQuery] = useState('');

    // Get user from localStorage
    const user = JSON.parse(localStorage.getItem('user') || '{}');

    const handleTrack = (shipment) => {
        setSelectedShipment(shipment);
        setShowTrackingModal(true);
    };

    const handleSearch = (e) => {
        setSearchQuery(e.target.value);
    };

    const filteredShipments = shipments.filter(shipment =>
        shipment.awb_number?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        shipment.receiver_name?.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="user-dashboard-container">
            {/* Welcome Banner */}
            <div className="user-welcome-banner">
                <div>
                    <h1>📦 My Shipments</h1>
                    <p>Welcome back, {user?.name || 'User'}! Track all your parcels in one place.</p>
                </div>
                <div className="user-search-box">
                    <i className="fas fa-search"></i>
                    <input
                        type="text"
                        placeholder="Search by AWB or Receiver..."
                        value={searchQuery}
                        onChange={handleSearch}
                    />
                </div>
            </div>

            {/* Shipment List */}
            <UserShipmentList
                shipments={filteredShipments}
                loading={loading}
                onTrack={handleTrack}
            />

            {/* Tracking Modal */}
            {showTrackingModal && selectedShipment && (
                <UserTrackingModal
                    shipment={selectedShipment}
                    onClose={() => {
                        setShowTrackingModal(false);
                        setSelectedShipment(null);
                    }}
                />
            )}
        </div>
    );
};

export default UserDashboard;