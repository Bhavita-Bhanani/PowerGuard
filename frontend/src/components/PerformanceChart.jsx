import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function PerformanceChart({ cpu, ram }) {

  const data = [
    { name: "Now", cpu, ram }
  ];

  return (
    <div className="chart-card">

      <h2>Performance Monitor</h2>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>

          <XAxis dataKey="name" />
          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="cpu"
            stroke="#4f46e5"
          />

          <Line
            type="monotone"
            dataKey="ram"
            stroke="#a855f7"
          />

        </LineChart>
      </ResponsiveContainer>

    </div>
  );
}