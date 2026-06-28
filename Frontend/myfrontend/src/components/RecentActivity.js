import { FaBolt } from "react-icons/fa";

function RecentActivity({ activities }) {

    return (

        <div className="activity-card">

            <h3 className="section-heading">

                <FaBolt className="heading-icon" />

                Recent Activity

            </h3>

            <div className="activity-scroll">

                {
                    activities.length === 0 ? (

                        <p>No recent activity found.</p>

                    ) : (

                        activities.map((activity) => (

                            <div className="activity-item" key={activity.id}>

                                <div className="activity-dot"></div>

                                <div>

                                    <h6>
                                        {activity.status}
                                    </h6>

                                    <small>
                                        {activity.awb_number} • {activity.location}
                                    </small>

                                    <br />

                                    <small>
                                        {activity.remarks}
                                    </small>

                                </div>

                            </div>

                        ))

                    )
                }

            </div>

        </div>

    );

}

export default RecentActivity;