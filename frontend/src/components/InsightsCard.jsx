function InsightsCard({ insights }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">

      <h2 className="text-xl font-bold text-green-600">
        Key Insights
      </h2>

      <ul className="mt-4 list-disc pl-5">

        {insights?.length ? (
          insights.map((item, index) => (
            <li key={index}>{item}</li>
          ))
        ) : (
          <li>No insights yet</li>
        )}

      </ul>

    </div>
  );
}

export default InsightsCard;