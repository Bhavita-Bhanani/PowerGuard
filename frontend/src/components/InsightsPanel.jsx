export default function InsightsPanel({ insights }) {
  return (
    <div className="insights-panel">

      <h2>AI Insights</h2>

      {insights.map((item, index) => (
        <div key={index} className="insight-item">
          {item}
        </div>
      ))}

    </div>
  );
}