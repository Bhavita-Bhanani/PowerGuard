import StatusCard from "../components/StatusCard";
import axios from "axios";
import { useEffect, useState } from "react";

import MetricCard from "../components/MetricCard";
import HealthGauge from "../components/HealthGauge";
import BatteryCard from "../components/BatteryCard";
import InsightsPanel from "../components/InsightsPanel";
import PerformanceChart from "../components/PerformanceChart";

import "../App.css";

export default function Dashboard() {

  const [data, setData] = useState(null);

  useEffect(() => {

    const fetchData = async () => {

      try {

        const response = await axios.get(
          "http://127.0.0.1:8000/metrics"
        );

        setData(response.data);

      } catch (err) {

        console.log(err);

      }

    };

    fetchData();

    const interval = setInterval(
      fetchData,
      5000
    );

    return () => clearInterval(interval);

  }, []);

  const downloadHTMLReport = () => {

    const html = `
    <html>
    <head>
      <title>PowerGuard Report</title>

      <style>
      body{
        font-family:Arial;
        padding:40px;
      }

      h1{
        color:#2563eb;
      }
      </style>

    </head>

    <body>

      <h1>PowerGuard AI Report</h1>

      <h2>Battery</h2>
      <p>${data.battery.percent}%</p>

      <h2>Charging</h2>
      <p>
      ${
        data.battery.charging
          ? "Connected"
          : "Disconnected"
      }
      </p>

      <h2>CPU</h2>
      <p>${data.system.cpu}%</p>

      <h2>RAM</h2>
      <p>${data.system.ram}%</p>

      <h2>Disk</h2>
      <p>${data.system.disk}%</p>

      <h2>Health Score</h2>
      <p>${data.status.score}</p>

      <h2>Status</h2>
      <p>${data.status.status}</p>

    </body>
    </html>
    `;

    const blob = new Blob(
      [html],
      { type: "text/html" }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download =
      "PowerGuard_Report.html";

    a.click();

  };

  if (!data) {
    return <h1>Loading PowerGuard...</h1>;
  }

  return (

    <div className="dashboard">

      <div className="hero">

        <h1>PowerGuard</h1>

        <p>
          AI Powered Laptop Health Monitor
        </p>

      </div>

      <div className="metrics-grid">

        <MetricCard
          title="Battery"
          value={`${data.battery.percent}%`}
        />

        <MetricCard
          title="CPU Usage"
          value={`${data.system.cpu}%`}
        />

        <MetricCard
          title="RAM Usage"
          value={`${data.system.ram}%`}
        />

        <MetricCard
          title="Disk Usage"
          value={`${data.system.disk}%`}
        />

      </div>

     <StatusCard
        score={data.status.score}
        status={data.status.status}
      />

      <BatteryCard
        battery={data.battery}
      />

      <PerformanceChart
        cpu={data.system.cpu}
        ram={data.system.ram}
      />

      <InsightsPanel
        insights={data.insights}
      />

      <div className="report-section">

        <button
          className="download-btn"
          onClick={downloadHTMLReport}
        >
          Download Full System Report
        </button>

      </div>

    </div>

  );

}