import { FaCube, FaStore } from "react-icons/fa";

function Navbar({ merchant }) {
    return (

        <div className="navbar-container">

            <div className="logo">

                <FaCube className="logo-icon" />

                <h2>
                    Ship<span>Xpress</span>
                </h2>

            </div>

            <button className="merchant-btn">

                <FaStore />

                <span>{merchant?.company_name || "Merchant"}</span>

            </button>

        </div>

    );
}

export default Navbar;