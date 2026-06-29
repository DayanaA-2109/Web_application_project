import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const UserTrackingMap = ({ location, status }) => {
    const mapRef = useRef(null);
    const mapInstanceRef = useRef(null);
    const markerRef = useRef(null);

    const getCoordinates = (location) => {
        const coords = {
            'Mumbai': [19.0760, 72.8777],
            'Bangalore': [12.9716, 77.5946],
            'Hyderabad': [17.3850, 78.4867],
            'Pune': [18.5204, 73.8567],
            'Delhi': [28.6139, 77.2090],
            'Chennai': [13.0827, 80.2707],
            'Warehouse': [19.0760, 72.8777],
            'Mumbai Hub': [19.0760, 72.8777],
            'Bangalore Hub': [12.9716, 77.5946],
            'Pune Hub': [18.5204, 73.8567]
        };

        if (!location) return coords['Mumbai'];

        for (const [key, value] of Object.entries(coords)) {
            if (location.toLowerCase().includes(key.toLowerCase())) {
                return value;
            }
        }
        return coords['Mumbai'];
    };

    useEffect(() => {
        if (!mapRef.current) return;

        if (!mapInstanceRef.current) {
            const coord = getCoordinates(location);
            mapInstanceRef.current = L.map(mapRef.current).setView(coord, 12);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(mapInstanceRef.current);
        }

        const coord = getCoordinates(location);
        if (mapInstanceRef.current) {
            mapInstanceRef.current.setView(coord, 12);

            if (markerRef.current) {
                markerRef.current.setLatLng(coord);
            } else {
                markerRef.current = L.marker(coord).addTo(mapInstanceRef.current);
            }

            markerRef.current.bindPopup(`
                <b>${location || 'Current Location'}</b><br>
                Status: ${status || 'No data'}
            `).openPopup();

            // Add circle
            L.circle(coord, {
                radius: 500,
                color: '#2563eb',
                fillColor: '#3b82f6',
                fillOpacity: 0.1
            }).addTo(mapInstanceRef.current);
        }

        return () => {
            if (mapInstanceRef.current) {
                mapInstanceRef.current.remove();
                mapInstanceRef.current = null;
                markerRef.current = null;
            }
        };
    }, [location, status]);

    return <div ref={mapRef} style={{ width: '100%', height: '100%' }} />;
};

export default UserTrackingMap;