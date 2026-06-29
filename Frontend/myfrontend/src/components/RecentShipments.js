import { FaClipboardList, FaSyncAlt } from "react-icons/fa";

function RecentShipments({ shipments }) {

    const shipmentList = Array.isArray(shipments)
        ? shipments
        : (shipments?.shipments || shipments?.data || []);

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

                <colgroup>
                    <col style={{ width: "32%" }} />
                    <col style={{ width: "28%" }} />
                    <col style={{ width: "22%" }} />
                    <col style={{ width: "18%" }} />
                </colgroup>

                <thead>

                    <tr>

                        <th>AWB</th>
                        <th>Receiver</th>
                        <th>City</th>
                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {shipmentList.length === 0 ? (

                        <tr>

                            <td colSpan="4" className="empty-row">
                                No Shipments Found
                            </td>

                        </tr>

                    ) : (

                        shipmentList.map((shipment) => (

                            <tr key={shipment.id}>

                                <td>{shipment.awb_number}</td>

                                <td>{shipment.receiver_name}</td>

                                <td>{shipment.receiver_city}</td>

                                <td>

                                    <span
                                        className={`status ${shipment.status}`}
                                    >
                                        {shipment.status.replace("_", " ")}
                                    </span>

                                </td>

                            </tr>

                        ))

                    )}

                </tbody>

            </table>

        </div>

    );

}

export default RecentShipments;