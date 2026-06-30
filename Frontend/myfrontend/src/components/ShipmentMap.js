import {
    MapContainer,
    TileLayer,
    Marker,
    Popup
} from "react-leaflet";

import L from "leaflet";

import "leaflet/dist/leaflet.css";
import "../css/ShipmentMap.css";
import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({

    iconRetinaUrl: markerIcon2x,

    iconUrl: markerIcon,

    shadowUrl: markerShadow,

});

function ShipmentMap({ latitude, longitude, location }) {

    if (!latitude || !longitude) {
        return (
            <p>No location available.</p>
        );
    }

    return (

        <div className="shipment-map">

            <h3>Current Shipment Location</h3>

            <MapContainer
                center={[latitude, longitude]}
                zoom={13}
                style={{
                    height: "350px",
                    width: "100%",
                    borderRadius: "12px"
                }}
            >

                <TileLayer
                    attribution='&copy; OpenStreetMap contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />

                <Marker position={[latitude, longitude]}>

                    <Popup>
                        {location}
                    </Popup>

                </Marker>

            </MapContainer>

        </div>

    );

}

export default ShipmentMap;