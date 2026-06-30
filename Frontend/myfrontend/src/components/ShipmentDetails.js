import "../css/ShipmentDetails.css";

function ShipmentDetails({ shipment }) {

    if (!shipment) return null;

    return (

        <div className="details-card">

            <div className="details-header">

                <h2>{shipment.awb_number}</h2>

                <span className={`status-badge ${shipment.status}`}>
                    {shipment.status.replaceAll("_", " ")}
                </span>

            </div>

            <div className="details-grid">

                <div>
                    <label>Receiver</label>
                    <p>{shipment.receiver_name}</p>
                </div>

                <div>
                    <label>Merchant</label>
                    <p>{shipment.merchant_name}</p>
                </div>

                <div>
                    <label>Phone</label>
                    <p>{shipment.receiver_phone}</p>
                </div>

                <div>
                    <label>Weight</label>
                    <p>{shipment.weight} Kg</p>
                </div>

                <div>
                    <label>City</label>
                    <p>{shipment.receiver_city}</p>
                </div>

                <div>
                    <label>COD Amount</label>
                    <p>₹ {shipment.cod_amount}</p>
                </div>

                <div>
                    <label>Order ID</label>
                    <p>{shipment.order_id}</p>
                </div>

                <div>
                    <label>Expected Delivery</label>
                    <p>{shipment.expected_delivery}</p>
                </div>

            </div>

        </div>

    );

}

export default ShipmentDetails;