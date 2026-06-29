import { useState } from "react";
import api from "../services/api";
import { FaSearch, FaTimes, FaBox } from "react-icons/fa";
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

        const response = await api.get(`/track/${awb}/`);

        if (response.data.success === true) {

            setShipment(response.data.shipment);

        } else {

            setError(response.data.message);

        }

    }

    catch (err) {

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

                <div className="track-header">

                    <h2>
                        <FaBox /> Track Shipment
                    </h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        <FaTimes />
                    </button>

                </div>

                <div className="track-body">

                    <label>Enter AWB Number</label>

                    <input
                        type="text"
                        placeholder="Ex: AWB123456"
                        value={awb}
                        onChange={(e) => setAwb(e.target.value)}
                    />

                </div>

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
                        <FaSearch /> Track
                    </button>

                </div>

            </div>

        </div>

    );

}

export default TrackShipmentModal;