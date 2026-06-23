function ConclusionCard({ conclusion }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">
      <h2 className="text-xl font-bold text-blue-600">
        Conclusion
      </h2>

      <p className="mt-4">
        {conclusion || "No conclusion yet"}
      </p>
    </div>
  );
}

export default ConclusionCard;