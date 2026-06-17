export default function MetricCard({ title, value }) {
  return (
    <div className="metric-card">
      <p>{title}</p>
      <h1>{value}</h1>
    </div>
  );
}