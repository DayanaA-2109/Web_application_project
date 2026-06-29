import React, { useState, useEffect, useRef } from 'react';
import { shipmentAPI } from '../../services/api';
import UserTrackingMap from './UserTrackingMap';
import '../../css/User-Tracking-Modal.css';

const UserTrackingModal = ({ shipment, onClose }) => {
    const [trackingHistory, setTrackingHistory] = useState([]);
    const [loading, setLoading] = useState(true);
    const [currentStatus, setCurrentStatus] = useState(null);
    const modalRef = useRef();

    useEffect(() => {
        fetchTrackingHistory();
        const handleEscape = (e) => {
            if (e.key === 'Escape') onClose();
        };
        document.addEventListener('keydown', handleEscape);
        return () => document.removeEventListener('keydown', handleEscape);
    }, [shipment.id]);

    const fetchTrackingHistory = async () => {
        try {
            setLoading(true);
            // Replace with your actual API call
            // const response = await shipmentAPI.getTrackingHistory(shipment.id);
            // setTrackingHistory(response.data);

            // Sample data - REPLACE WITH API CALL
            const sampleData = [
                { status: "Order Placed", location: "Warehouse", remarks: "Order confirmed", created_at: "2024-12-18 10:00:00" },
                { status: "Picked Up", location: "Warehouse", remarks: "Picked by agent", created_at: "2024-12-18 14:30:00" },
                { status: "In Transit", location: "Mumbai Hub", remarks: "Package sorted at hub", created_at: "2024-12-19 09:00:00" },
                { status: "Out for Delivery", location: "Mumbai", remarks: "Out for delivery", created_at: "2024-12-20 08:30:00" },
                { status: "Delivered", location: "Mumbai", remarks: "Delivered to recipient", created_at: "2024-12-20 11:45:00" }
            ];
            setTrackingHistory(sampleData);
            if (sampleData.length > 0) {
                setCurrentStatus(sampleData[sampleData.length - 1]);
            }
        } catch (error) {
            console.error('Error fetching tracking:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleOutsideClick = (e) => {
        if (modalRef.current && !modalRef.current.contains(e.target)) {
            onClose();
        }
    };

    return (
        <div className="user-modal-overlay" onClick={handleOutsideClick}>
            <div className="user-modal" ref={modalRef}>
                <div className="user-modal-header">
                    <h2>
                        <i className="fas fa-truck" style={{ color: '#2563eb' }}></i>
                        Tracking Details
                        <span className="user-modal-awb">{shipment.awb_number}</span>
                    </h2>
                    <button className="user-modal-close" onClick={onClose}>&times;</button>
                </div>

                <div className="user-modal-body">
                    {/* Left: Timeline */}
                    <div className="user-tracking-timeline">
                        {loading ? (
                            <div className="user-loading-text">Loading tracking history...</div>
                        ) : trackingHistory.length === 0 ? (
                            <p style={{ color: '#5a6c7d', padding: '20px 0' }}>
                                No tracking updates available
                            </p>
                        ) : (
                            trackingHistory.map((track, index) => (
                                <div
                                    key={index}
                                    className={`user-timeline-item ${track.status === 'Delivered' ? 'user-delivered' : ''}`}
                                >
                                    <div className="user-tl-status">{track.status}</div>
                                    <div className="user-tl-location">
                                        <i className="fas fa-location-dot" style={{ fontSize: '12px' }}></i>
                                        {track.location}
                                    </div>
                                    <div className="user-tl-remark">{track.remarks}</div>
                                    <div className="user-tl-time">{track.created_at}</div>
                                </div>
                            ))
                        )}
                    </div>

                    {/* Right: Map */}
                    <div>
                        <UserTrackingMap
                            location={currentStatus?.location || 'Mumbai'}
                            status={currentStatus?.status || 'No data'}
                        />
                        <div className="user-map-info">
                            <div className="user-mi-row">
                                <span className="user-label">Current Status</span>
                                <span className="user-value">{currentStatus?.status || '-'}</span>
                            </div>
                            <div className="user-mi-row">
                                <span className="user-label">Location</span>
                                <span className="user-value">{currentStatus?.location || '-'}</span>
                            </div>
                            <div className="user-mi-row">
                                <span className="user-label">Last Updated</span>
                                <span className="user-value">{currentStatus?.created_at || '-'}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default UserTrackingModal;