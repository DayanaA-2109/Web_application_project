import { useState } from "react";
import api from "../services/api";
import {
    FaSearch,
    FaTimes,
    FaBox
} from "react-icons/fa";

import ShipmentTimeline from "./ShipmentTimeline";
import ShipmentMap from "./ShipmentMap";
import "../css/TrackShipmentModal.css";

function TrackShipmentModal({ show, onClose }) {

    const [awb, setAwb] = useState("");
    const [loading, setLoading] = useState(false);
    const [shipment, setShipment] = useState(null);
    const [error, setError] = useState("");

    if (!show) return null;

    const handleTrack = async () => {

        if (!awb.trim()) {
            setError("Please enter an AWB Number");
            return;
        }

        setLoading(true);
        setError("");
        setShipment(null);

        try {

            const response = await api.get(`/track/${awb.trim()}/`);

            if (response.data.success) {

                setShipment(response.data.shipment);

            } else {

                setError(response.data.message);

            }

        } catch (err) {

            setError(
                err.response?.data?.message ||
                "Shipment not found."
            );

        }

        setLoading(false);

    };

    return (

        <div className="track-modal-overlay">

            <div className="track-modal">

                {/* Header */}

                <div className="track-header">

                    <h2>

                        <FaBox />

                        Track Shipment

                    </h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        <FaTimes />
                    </button>

                </div>

                {/* Body */}

                <div className="track-body">

                    <label>Enter AWB Number</label>

                    <input
                        type="text"
                        placeholder="Ex: AWBF388C30A6E"
                        value={awb}
                        onChange={(e) => setAwb(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === "Enter") {
                                handleTrack();
                            }
                        }}
                    />

                    {loading && (

                        <p className="loading-text">

                            Searching shipment...

                        </p>

                    )}

                    {error && (

                        <p className="error-text">

                            {error}

                        </p>

                    )}

                    {shipment && (

                        <div className="shipment-card">

                            {/* Shipment Header */}

                            <div className="shipment-title">

                                <h3>

                                    {shipment.awb_number}

                                </h3>

                                <span
                                    className={`status-badge ${shipment.status}`}
                                >

                                    {shipment.status.replaceAll("_", " ")}

                                </span>

                            </div>

                            {/* Shipment Details */}

                            <div className="shipment-grid">

                                <div>

                                    <strong>Receiver</strong>

                                    <p>{shipment.receiver_name}</p>

                                </div>

                                <div>

                                    <strong>Phone</strong>

                                    <p>{shipment.receiver_phone}</p>

                                </div>

                                <div>

                                    <strong>Merchant</strong>

                                    <p>{shipment.merchant_name}</p>

                                </div>

                                <div>

                                    <strong>Weight</strong>

                                    <p>{shipment.weight} Kg</p>

                                </div>

                                <div>

                                    <strong>City</strong>

                                    <p>{shipment.receiver_city}</p>

                                </div>

                                <div>

                                    <strong>Expected Delivery</strong>

                                    <p>{shipment.expected_delivery}</p>

                                </div>

                            </div>

                            {/* Timeline */}

                            <ShipmentTimeline
                                tracking={shipment.tracking}

                            />
                            {shipment.tracking &&
shipment.tracking.length > 0 && (

    <ShipmentMap
        latitude={shipment.tracking[
            shipment.tracking.length - 1
        ].latitude}

        longitude={shipment.tracking[
            shipment.tracking.length - 1
        ].longitude}

        location={shipment.tracking[
            shipment.tracking.length - 1
        ].location}
    />

)}

                        </div>

                    )}

                </div>

                {/* Footer */}

                <div className="track-footer">

                    <button
                        className="cancel-btn"
                        onClick={onClose}
                    >

                        Cancel

                    </button>

                    <button
                        className="track-btn"
                        onClick={handleTrack}
                    >

                        <FaSearch />

                        Track

                    </button>

                </div>

            </div>

        </div>

    );

}

export default TrackShipmentModal;