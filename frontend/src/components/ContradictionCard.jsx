function ContradictionCard({
  contradictions
}) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">

      <h2 className="text-xl font-bold text-red-600">
        Contradictions
      </h2>

      <ul className="mt-4 list-disc pl-5">

        {contradictions?.length ? (
          contradictions.map(
            (item, index) => (
              <li key={index}>{item}</li>
            )
          )
        ) : (
          <li>No contradictions detected.</li>
        )}

      </ul>

    </div>
  );
}

export default ContradictionCard;