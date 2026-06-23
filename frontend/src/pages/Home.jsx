import { useState } from "react";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import UploadSection from "../components/UploadSection";
import SummaryCard from "../components/SummaryCard";
import ThemeCard from "../components/ThemeCard";
import ContradictionCard from "../components/ContradictionCard";
import InsightsCard from "../components/InsightsCard";
import FindingsCard from "../components/FindingsCard";
import ConclusionCard from "../components/ConclusionCard";
function Home() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <Hero />

      <div className="max-w-6xl mx-auto p-8">

        <UploadSection onAnalyze={setResult} />

        <SummaryCard summary={result?.summary} />

        <ThemeCard themes={result?.themes} />

        <InsightsCard insights={result?.insights} />
        <FindingsCard findings={result?.findings} />

        <ConclusionCard conclusion={result?.conclusion} />
        <ContradictionCard
          contradictions={result?.contradictions}
        />

      </div>

    </div>
  );
}

export default Home;