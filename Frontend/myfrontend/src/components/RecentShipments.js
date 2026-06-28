import { FaClipboardList, FaSyncAlt } from "react-icons/fa";

function RecentShipments({ shipments }) {
    // Fixed: Handle both array and object response
    const shipmentList = Array.isArray(shipments) ? shipments :
                        (shipments?.shipments || shipments?.data || []);

    return (
        <div className="shipment-card">
            <div className="shipment-header">
                <h3 className="section-heading">
                    <FaClipboardList className="heading-icon" />
                    Recent Shipments
                </h3>
                <button className="refresh-btn">
                    <FaSyncAlt />
                    Refresh
                </button>
            </div>
            <table className="shipment-table">
                <thead>
                    <tr>
                        <th>AWB</th>
                        <th>Receiver</th>
                        <th>City</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        shipmentList.length === 0 ?
                        (
                            <tr>
                                <td colSpan="4" style={{ textAlign: 'center', padding: '20px' }}>
                                    No Shipments Found
                                </td>
                            </tr>
                        )
                        :
                        (
                            shipmentList.map((shipment) => (
                                <tr key={shipment.id || shipment.awb_number}>
                                    <td>
                                        {shipment.awb_number || shipment.awb}
                                    </td>
                                    <td>
                                        {shipment.receiver_name || shipment.receiver}
                                    </td>
                                    <td>
                                        {shipment.receiver_city || shipment.city}
                                    </td>
                                    <td>
                                        <span
                                            className={`status ${shipment.status}`}
                                        >
                                            {shipment.status}
                                        </span>
                                    </td>
                                </tr>
                            ))
                        )
                    }
                </tbody>
            </table>
        </div>
    );
}

export default RecentShipments;