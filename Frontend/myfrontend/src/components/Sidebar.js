import {
    FaUserCircle,
    FaCog,
    FaQuestionCircle,
    FaSignOutAlt
} from "react-icons/fa";

import "../css/Sidebar.css";

function Sidebar({ onLogout, setActiveSection }) {

    return (

        <div className="sidebar">

            {/* Logo */}
            <div>

                <div className="sidebar-logo">
                    ShipXpress
                </div>

                {/* Menu */}
                <div className="sidebar-menu">

                    <button
                        className="sidebar-item"
                        onClick={() => setActiveSection("account")}
                    >
                        <FaUserCircle />
                        <span>My Account</span>
                    </button>

                    <button
                        className="sidebar-item"
                        onClick={() => setActiveSection("settings")}
                    >
                        <FaCog />
                        <span>Settings</span>
                    </button>

                    <button
                        className="sidebar-item"
                        onClick={() => setActiveSection("help")}
                    >
                        <FaQuestionCircle />
                        <span>Help</span>
                    </button>

                </div>

            </div>

            {/* Logout */}
            <div className="sidebar-footer">

                <button
                    className="sidebar-logout-btn"
                    onClick={onLogout}
                >
                    <FaSignOutAlt />
                    <span>Logout</span>
                </button>

            </div>

        </div>

    );

}

export default Sidebar;