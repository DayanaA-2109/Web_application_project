import { useState } from "react";
import api from "../services/api";
import { FaPlus, FaSearch, FaKey } from "react-icons/fa";
import CreateShipmentModal from "./CreateShipmentModal";

function QuickActions() {

    const [showModal, setShowModal] = useState(false);

    const generateApiKey = async () => {

        try {

            const response = await api.post("/api-key/generate/", {
                merchant_id: 1,
                key_name: "Dashboard API Key"
            });

            // FIXED: Check if success is true
            if (response.data.success === true) {
                alert(
                    "API Key Generated Successfully!\n\n" +
                    response.data.api_key.api_key
                );
            } else {
                alert(response.data.message || "Failed to generate API Key");
            }

        }

        catch (error) {

            console.error(error);
            alert(error.response?.data?.message || "Failed to generate API Key");

        }

    };

    return (

        <>

            <div className="quick-card">

                <h3 className="section-heading">

                    <FaPlus className="heading-icon" />

                    Quick Actions

                </h3>

                <button
                    className="action-btn create-btn"
                    onClick={() => {
                        console.log("Create Shipment button clicked");
                        setShowModal(true);
                    }}
                >

                    <FaPlus />

                    <span>Create Shipment</span>

                </button>

                <button
                    className="action-btn track-btn"
                >

                    <FaSearch />

                    <span>Track Shipment</span>

                </button>

                <button
                    className="action-btn api-btn"
                    onClick={generateApiKey}
                >

                    <FaKey />

                    <span>Generate API Key</span>

                </button>

            </div>

            <CreateShipmentModal
                show={showModal}
                onClose={() => setShowModal(false)}
                onSuccess={() => window.location.reload()}
            />

        </>

    );

}

export default QuickActions;