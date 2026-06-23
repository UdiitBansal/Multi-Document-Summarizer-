function SummaryCard({ summary }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">
      <h2 className="text-xl font-bold mb-3">
        Summary
      </h2>

      <p>
        {summary ||
          "Generated summary will appear here..."}
      </p>
    </div>
  );
}

export default SummaryCard;