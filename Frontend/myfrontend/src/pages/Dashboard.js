import { useState, useEffect } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import StatsCards from "../components/StatsCards";
import RecentActivity from "../components/RecentActivity";
import RecentShipments from "../components/RecentShipments";
import QuickActions from "../components/QuickActions";

import api from "../services/api";

import "../css/dashboard.css";

function Dashboard({ onLogout }) {

    const [merchant, setMerchant] = useState(null);
    const [stats, setStats] = useState({});
    const [activities, setActivities] = useState([]);
    const [shipments, setShipments] = useState([]);

    // NEW
    const [activeSection, setActiveSection] = useState("dashboard");

    useEffect(() => {

        // Fetch merchant
        api.get("/merchant/1/")
            .then((res) => {
                console.log("Merchant:", res.data);
                setMerchant(res.data);
            })
            .catch((err) => {
                console.log(err);
                setMerchant({ company_name: "Merchant" });
            });

        // Fetch stats
        api.get("/stats/?merchant_id=1")
            .then((res) => {
                console.log("Stats:", res.data);
                setStats(res.data);
            })
            .catch((err) => console.log(err));

        // Fetch activity
        api.get("/recent-activity/?merchant_id=1")
            .then((res) => {

                console.log("Activities:", res.data);

                const activityData = Array.isArray(res.data)
                    ? res.data
                    : res.data.activities || res.data.data || [];

                setActivities(activityData);

            })
            .catch((err) => console.log(err));

        // Fetch shipments
        api.get("/shipments/?merchant_id=1")
            .then((res) => {

                console.log("Shipments:", res.data);

                const shipmentData = Array.isArray(res.data)
                    ? res.data
                    : res.data.shipments || res.data.data || [];

                setShipments(shipmentData);

            })
            .catch((err) => console.log(err));

    }, []);

    return (

        <div className="dashboard-layout">

            <Sidebar
                onLogout={onLogout}
                setActiveSection={setActiveSection}
            />

            <div className="dashboard-main">

                {/* DASHBOARD */}

                {activeSection === "dashboard" && (

                    <div className="container dashboard-container">

                        <Navbar merchant={merchant} />

                        <StatsCards stats={stats} />

                        <div className="row mt-4">

                            <div className="col-lg-8">

                                <RecentActivity
                                    activities={activities}
                                />

                            </div>

                            <div className="col-lg-4">

                                <QuickActions />

                            </div>

                        </div>

                        <div className="mt-4">

                            <RecentShipments
                                shipments={shipments}
                            />

                        </div>

                    </div>

                )}

                {/* MY ACCOUNT */}

                {activeSection === "account" && (

                    <div className="container dashboard-container">

                        <h2>👤 My Account</h2>

                        <div className="shipment-card">

                            <h4>{merchant?.company_name}</h4>

                            <p>
                                Welcome to your ShipXpress account.
                            </p>

                            <hr />

                            <p>
                                <strong>Merchant Name:</strong>{" "}
                                {merchant?.company_name}
                            </p>

                            <p>
                                <strong>Merchant ID:</strong> 1
                            </p>

                            <p>
                                <strong>Status:</strong> Active
                            </p>

                        </div>

                    </div>

                )}

                {/* SETTINGS */}

                {activeSection === "settings" && (

                    <div className="container dashboard-container">

                        <h2>⚙ Settings</h2>

                        <div className="shipment-card">

                            <p>Settings page coming soon.</p>

                            <button className="track-btn">
                                Change Password
                            </button>

                            <br /><br />

                            <button className="track-btn">
                                Notification Settings
                            </button>

                            <br /><br />

                            <button className="track-btn">
                                Theme Settings
                            </button>

                        </div>

                    </div>

                )}

                {/* HELP */}

                {activeSection === "help" && (

                    <div className="container dashboard-container">

                        <h2>❓ Help</h2>

                        <div className="shipment-card">

                            <h4>Need Help?</h4>

                            <p>Email : support@shipxpress.com</p>

                            <p>Phone : +91 9876543210</p>

                            <p>
                                Working Hours:
                                Monday - Saturday
                                9:00 AM - 6:00 PM
                            </p>

                        </div>

                    </div>

                )}

            </div>

        </div>

    );

}

export default Dashboard;