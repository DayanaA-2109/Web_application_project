import { FaClipboardList, FaSyncAlt } from "react-icons/fa";

function RecentShipments({ shipments }) {

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

                        shipments.length === 0 ?

                        (

                            <tr>

                                <td colSpan="4">

                                    No Shipments Found

                                </td>

                            </tr>

                        )

                        :

                        (

                            shipments.map((shipment) => (

                                <tr key={shipment.id}>

                                    <td>

                                        {shipment.awb_number}

                                    </td>

                                    <td>

                                        {shipment.receiver_name}

                                    </td>

                                    <td>

                                        {shipment.receiver_city}

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