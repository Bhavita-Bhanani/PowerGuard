export default function BatteryCard({ battery }) {

  return (

    <div className="battery-card">

      <h2>Battery Information</h2>

      <p>
        🔌 Charging:
        {" "}
        {battery.charging
          ? "Connected"
          : "Disconnected"}
      </p>

      <p>
        🔋 Battery Level:
        {" "}
        {battery.percent}%
      </p>

      <p>
        ⏳ Time Remaining:
        {" "}
        {battery.time_remaining}
      </p>

    </div>

  );

}