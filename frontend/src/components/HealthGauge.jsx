export default function HealthGauge({ score, status }) {

  return (
    <div className="health-gauge">

      <h3 className="health-title">
        System Health
      </h3>

      <div className="score-circle">
        {score}
      </div>

      <div className="score-max">
        /100
      </div>

      <div className="health-status">
        {status}
      </div>

    </div>
  );

}