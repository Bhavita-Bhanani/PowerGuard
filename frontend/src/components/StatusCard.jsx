function StatusCard({ score, status }) {

  return (
    <div
      style={{
        background: "linear-gradient(135deg,#2563eb,#7c3aed)",
        borderRadius: "24px",
        padding: "30px",
        color: "white"
      }}
    >
      <p>System Health</p>

      <h1>{score}/100</h1>

      <h2>{status}</h2>
    </div>
  );

}

export default StatusCard;