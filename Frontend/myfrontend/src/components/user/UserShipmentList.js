import React from 'react';
import UserShipmentCard from './UserShipmentCard';

const UserShipmentList = ({ shipments, loading, onTrack }) => {
    if (loading) {
        return (
            <div className="user-loading-container">
                <div className="user-loader"></div>
                <p>Loading shipments...</p>
            </div>
        );
    }

    if (shipments.length === 0) {
        return (
            <div className="user-empty-state">
                <i className="fas fa-box-open"></i>
                <h3>No Shipments Found</h3>
                <p>You don't have any shipments yet.</p>
            </div>
        );
    }

    return (
        <div className="user-shipment-grid">
            {shipments.map((shipment) => (
                <UserShipmentCard
                    key={shipment.id}
                    shipment={shipment}
                    onTrack={onTrack}
                />
            ))}
        </div>
    );
};

export default UserShipmentList;