function ThemeCard({ themes }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">

      <h2 className="text-xl font-bold mb-3">
        Key Themes
      </h2>

      <ul className="list-disc pl-5">

        {themes?.length ? (
          themes.map((theme, index) => (
            <li key={index}>{theme}</li>
          ))
        ) : (
          <li>No themes yet</li>
        )}

      </ul>

    </div>
  );
}

export default ThemeCard;