import React, { useState, useEffect } from 'react';
import { shipmentAPI } from '../services/api';
import UserDashboard from '../components/user/UserDashboard';

const UserDashboardPage = () => {
    const [shipments, setShipments] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchShipments();
    }, []);

    const fetchShipments = async () => {
        try {
            setLoading(true);
            // Replace with your actual API call
            // const response = await shipmentAPI.getUserShipments();
            // setShipments(response.data);

            // Sample data - REPLACE WITH API CALL
            const sampleShipments = [
                {
                    id: 1,
                    awb_number: "AWB-2024-001",
                    receiver_name: "Rahul Kumar",
                    receiver_city: "Mumbai",
                    weight: "2.5 kg",
                    cod_amount: "₹1,500",
                    status: "Delivered",
                    expected_delivery: "2024-12-20"
                },
                {
                    id: 2,
                    awb_number: "AWB-2024-002",
                    receiver_name: "Sneha Patel",
                    receiver_city: "Bangalore",
                    weight: "1.2 kg",
                    cod_amount: "₹800",
                    status: "In Transit",
                    expected_delivery: "2024-12-28"
                },
                {
                    id: 3,
                    awb_number: "AWB-2024-003",
                    receiver_name: "Amit Singh",
                    receiver_city: "Hyderabad",
                    weight: "3.0 kg",
                    cod_amount: "₹2,200",
                    status: "Pending",
                    expected_delivery: "2024-12-30"
                }
            ];
            setShipments(sampleShipments);
        } catch (error) {
            console.error('Error fetching shipments:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <UserDashboard
            shipments={shipments}
            loading={loading}
            onRefresh={fetchShipments}
        />
    );
};

export default UserDashboardPage;