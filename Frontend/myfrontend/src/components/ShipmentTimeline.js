import {
    FaCheckCircle,
    FaCircle,
    FaMapMarkerAlt,
    FaClock
} from "react-icons/fa";

import "../css/ShipmentTimeline.css";

function ShipmentTimeline({ tracking }) {

    if (!tracking || tracking.length === 0) {
        return null;
    }

    return (

        <div className="timeline-card">

            <h2>Shipment Journey</h2>

            {tracking.map((track, index) => (

                <div
                    key={track.id}
                    className="timeline-row"
                >

                    <div className="timeline-left">

                        <div className="timeline-circle">

                            {index === tracking.length - 1 ?

                                <FaCheckCircle />

                                :

                                <FaCircle />

                            }

                        </div>

                        {index !== tracking.length - 1 && (

                            <div className="timeline-line"></div>

                        )}

                    </div>

                    <div className="timeline-right">

                        <h3>{track.status}</h3>

                        <p>

                            <FaMapMarkerAlt />

                            {track.location}

                        </p>

                        <small>{track.remarks}</small>

                        <div className="timeline-date">

                            <FaClock />

                            {new Date(track.created_at).toLocaleString()}

                        </div>

                    </div>

                </div>

            ))}

        </div>

    );

}

export default ShipmentTimeline;