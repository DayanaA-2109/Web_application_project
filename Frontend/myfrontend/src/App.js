import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [shipments, setShipments] = useState([]);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:3000/shipments/")
      .then((response) => {

        console.log(response.data);

        setShipments(response.data);

      })
      .catch((error) => {

        console.log(error);

      });

  }, []);

  return (

    <div style={{ padding: "20px" }}>

      <h1>Shipment List</h1>

      <table border="1" cellPadding="10">

        <thead>

          <tr>

            <th>AWB Number</th>
            <th>Receiver</th>
            <th>City</th>
            <th>Status</th>

          </tr>

        </thead>

        <tbody>

          {shipments.map((shipment) => (

            <tr key={shipment.awb_number}>

              <td>{shipment.awb_number}</td>

              <td>{shipment.receiver_name}</td>

              <td>{shipment.receiver_city}</td>

              <td>{shipment.status}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );

}

export default App;