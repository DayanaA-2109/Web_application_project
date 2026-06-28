import { useState, useEffect } from "react";

import Navbar from "../components/Navbar";
import StatsCards from "../components/StatsCards";
import RecentActivity from "../components/RecentActivity";
import RecentShipments from "../components/RecentShipments";
import QuickActions from "../components/QuickActions";

import api from "../services/api";

import "../css/dashboard.css";

function Dashboard() {

    const [merchant, setMerchant] = useState({});
    const [stats, setStats] = useState({});
    const [activities, setActivities] = useState([]);
    const [shipments, setShipments] = useState([]);

    useEffect(() => {

    api.get("/merchant/1/")
        .then((res) => {
            console.log("Merchant:", res.data);
            setMerchant(res.data);
        })
        .catch((err) => console.log(err));

    api.get("/stats/?merchant_id=1")
        .then((res) => {
            console.log("Stats:", res.data);
            setStats(res.data);
        })
        .catch((err) => console.log(err));
    api.get("/recent-activity/?merchant_id=1")
        .then((res) => {
            console.log("Activities:", res.data);
            setActivities(res.data);
        })
        .catch((err) => console.log(err));
    api.get("/shipments/")
        .then((res) => {
            console.log("Shipments:", res.data);
            setShipments(res.data);
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