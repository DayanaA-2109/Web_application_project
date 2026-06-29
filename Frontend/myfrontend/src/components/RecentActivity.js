import { FaBolt } from "react-icons/fa";

function RecentActivity({ activities }) {
    // Handle both array and object response
    const activityList = Array.isArray(activities) ? activities :
                        (activities?.activities || activities?.data || []);

    return (
        <div className="activity-card">
            <h3 className="section-heading">
                <FaBolt className="heading-icon" />
                Recent Activity
            </h3>
            <div className="activity-scroll">
                {
                    activityList.length === 0 ? (
                        <p>No recent activity found.</p>
                    ) : (
                        activityList.map((activity) => (
                            <div className="activity-item" key={activity.id}>
                                <div className="activity-dot"></div>
                                <div>
                                    <h6>
                                        {activity.status || activity.action}
                                    </h6>
                                    <small>
                                        {activity.awb_number || activity.awb || ''}
                                        {activity.location ? ` • ${activity.location}` : ''}
                                    </small>
                                    <br />
                                    <small>
                                        {activity.remarks || activity.message || ''}
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