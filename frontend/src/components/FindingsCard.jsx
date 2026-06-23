function FindingsCard({ findings }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">
      <h2 className="text-xl font-bold text-purple-600">
        Key Findings
      </h2>

      <ul className="mt-4 list-disc pl-5">
        {findings?.length ? (
          findings.map((item, index) => (
            <li key={index}>{item}</li>
          ))
        ) : (
          <li>No findings yet</li>
        )}
      </ul>
    </div>
  );
}

export default FindingsCard;