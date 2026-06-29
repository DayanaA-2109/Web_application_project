import { useState, useEffect } from "react";

import Navbar from "../components/Navbar";
import StatsCards from "../components/StatsCards";
import RecentActivity from "../components/RecentActivity";
import RecentShipments from "../components/RecentShipments";
import QuickActions from "../components/QuickActions";

import api from "../services/api";

import "../css/dashboard.css";

function Dashboard() {

    const [merchant, setMerchant] = useState(null);
    const [stats, setStats] = useState({});
    const [activities, setActivities] = useState([]);
    const [shipments, setShipments] = useState([]);

    useEffect(() => {

        // Fetch merchant
        api.get("/merchant/1/")
            .then((res) => {
                console.log("Merchant:", res.data);
                setMerchant(res.data);
            })
            .catch((err) => {
                console.log(err);
                // Set default merchant if API fails
                setMerchant({ company_name: "Merchant" });
            });

        // Fetch stats
        api.get("/stats/?merchant_id=1")
            .then((res) => {
                console.log("Stats:", res.data);
                setStats(res.data);
            })
            .catch((err) => console.log(err));

        // Fetch recent activity
        api.get("/recent-activity/?merchant_id=1")
            .then((res) => {
                console.log("Activities:", res.data);
                // Handle both array and object response
                const activityData = Array.isArray(res.data) ?
                                    res.data :
                                    res.data.activities || res.data.data || [];
                setActivities(activityData);
            })
            .catch((err) => console.log(err));

        // Fetch shipments
        api.get("/shipments/?merchant_id=1")
            .then((res) => {
                console.log("Shipments:", res.data);
                // Handle both array and object response
                const shipmentData = Array.isArray(res.data) ?
                                    res.data :
                                    res.data.shipments || res.data.data || [];
                setShipments(shipmentData);
            })
            .catch((err) => console.log(err));

    }, []);

    return (

        <div className="container dashboard-container">

            <Navbar merchant={merchant} />

            <StatsCards stats={stats} />

            <div className="row mt-4">

                <div className="col-lg-8">

                    <RecentActivity activities={activities} />

                </div>

                <div className="col-lg-4">

                    <QuickActions />

                </div>

            </div>

            <div className="mt-4">

                <RecentShipments shipments={shipments} />

            </div>

        </div>

    );

}

export default Dashboard;