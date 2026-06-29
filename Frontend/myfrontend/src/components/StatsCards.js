import {
    FaTruck,
    FaCheckCircle,
    FaShippingFast,
    FaExclamationCircle
} from "react-icons/fa";

function StatsCards({ stats }) {

    const cards = [

        {
            title: "Total Shipments",
            value: stats.total ?? "-",
            subtitle: "All Shipments",
            icon: <FaTruck />,
            color: "#D6EAF8"
        },

        {
            title: "Delivered",
            value: stats.delivered ?? "-",
            subtitle: "Successfully Delivered",
            icon: <FaCheckCircle />,
            color: "#D5F5E3"
        },

        {
            title: "In Transit",
            value: stats.in_transit ?? "-",
            subtitle: "Currently Moving",
            icon: <FaShippingFast />,
            color: "#EBF5FB"
        },

        {
            title: "Pending / Failed",
            value: (stats.pending || 0) + (stats.failed || 0),
            subtitle: "Need Attention",
            icon: <FaExclamationCircle />,
            color: "#FADBD8"
        }

    ];

    return (

        <div className="row g-4">

            {cards.map((card, index) => (

                <div className="col-lg-3 col-md-6" key={index}>

                    <div className="stats-card">

                        <div className="stats-top">

                            <div>

                                <p className="stats-title">
                                    {card.title}
                                </p>

                                <h2 className="stats-number">
                                    {card.value}
                                </h2>

                                <small className="stats-subtitle">
                                    {card.subtitle}
                                </small>

                            </div>

                            <div
                                className="stats-icon"
                                style={{
                                    backgroundColor: card.color
                                }}
                            >
                                {card.icon}
                            </div>

                        </div>

                    </div>

                </div>

            ))}

        </div>

    );

}

export default StatsCards;