import React from 'react';

const getStatusClass = (status) => {
    const map = {
        'Delivered': 'user-delivered',
        'In Transit': 'user-transit',
        'Pending': 'user-pending',
        'Created': 'user-created',
        'Order Placed': 'user-created',
        'Picked Up': 'user-transit',
        'Out for Delivery': 'user-transit'
    };
    return map[status] || 'user-created';
};

const getStatusBadge = (status) => {
    return React.createElement(
        'span',
        { className: `user-status-badge ${getStatusClass(status)}` },
        status
    );
};

const UserShipmentCard = ({ shipment, onTrack }) => {
    const handleTrackClick = (e) => {
        e.stopPropagation();
        onTrack(shipment);
    };

    return React.createElement(
        'div',
        { className: 'user-shipment-card' },
        React.createElement(
            'div',
            { className: 'user-shipment-left' },
            React.createElement('span', {
                className: `user-status-dot ${getStatusClass(shipment.status)}`
            }),
            React.createElement(
                'div',
                { className: 'user-shipment-info' },
                React.createElement('div', { className: 'user-awb' }, shipment.awb_number),
                React.createElement(
                    'div',
                    { className: 'user-details' },
                    shipment.receiver_name, ' • ', shipment.receiver_city, ' • ', shipment.weight
                ),
                React.createElement(
                    'div',
                    { className: 'user-date' },
                    'Expected: ', shipment.expected_delivery, ' • COD: ', shipment.cod_amount
                )
            )
        ),
        React.createElement(
            'div',
            { className: 'user-shipment-right' },
            getStatusBadge(shipment.status),
            React.createElement(
                'button',
                { className: 'user-track-btn', onClick: handleTrackClick },
                React.createElement('i', { className: 'fas fa-map-marker-alt' }),
                ' Track'
            )
        )
    );
};

export default UserShipmentCard;