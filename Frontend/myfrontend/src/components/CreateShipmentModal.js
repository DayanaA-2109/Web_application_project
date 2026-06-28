import { useState } from "react";
import api from "../services/api";

function CreateShipmentModal({ show, onClose, onSuccess }) {
     console.log("Modal show =", show);
    const [form, setForm] = useState({

        merchant_id: 1,
        order_id: "",
        receiver_name: "",
        receiver_phone: "",
        receiver_address: "",
        receiver_city: "",
        receiver_pincode: "",
        weight: "",
        cod_amount: "",
        expected_delivery: ""

    });

    const handleChange = (e) => {

        setForm({

            ...form,
            [e.target.name]: e.target.value

        });

    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            await api.post("/shipments/create/", form);

            alert("Shipment Created Successfully!");

            onSuccess();

            onClose();

        }

        catch (err) {

            console.log(err);

            alert("Failed to create shipment");

        }

    };

    if (!show) return null;

    return (

        <div className="modal-overlay">

            <div className="shipment-modal">

                <h3>Create Shipment</h3>

                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        name="order_id"
                        placeholder="Order ID"
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="text"
                        name="receiver_name"
                        placeholder="Receiver Name"
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="text"
                        name="receiver_phone"
                        placeholder="Phone Number"
                        onChange={handleChange}
                        required
                    />

                    <textarea
                        name="receiver_address"
                        placeholder="Address"
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="text"
                        name="receiver_city"
                        placeholder="City"
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="text"
                        name="receiver_pincode"
                        placeholder="Pincode"
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="number"
                        name="weight"
                        placeholder="Weight"
                        onChange={handleChange}
                    />

                    <input
                        type="number"
                        name="cod_amount"
                        placeholder="COD Amount"
                        onChange={handleChange}
                    />

                    <input
                        type="date"
                        name="expected_delivery"
                        onChange={handleChange}
                    />

                    <div className="modal-buttons">

                        <button
                            type="button"
                            className="cancel-btn"
                            onClick={onClose}
                        >
                            Cancel
                        </button>

                        <button
                            type="submit"
                            className="create-btn"
                        >
                            Create Shipment
                        </button>

                    </div>

                </form>

            </div>

        </div>

    );

}

export default CreateShipmentModal;

