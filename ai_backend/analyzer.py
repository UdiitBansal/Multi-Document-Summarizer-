from theme_extractor import extract_themes
from contradiction_detector import detect_contradiction


def analyze_summary(summary):

    themes = extract_themes(summary)

    findings = [
        sentence.strip()
        for sentence in summary.split(".")
        if len(sentence.strip()) > 20
    ][:3]

    insights = []

    if themes:
        insights.append(
            f"The research primarily focuses on {themes[0]}."
        )

    if len(themes) > 1:
        insights.append(
            f"Important concepts include {themes[1]}."
        )

    contradictions = []

    try:
        contradiction_result = detect_contradiction(
            "Transformers outperform CNNs",
            "CNNs outperform Transformers"
        )

        if contradiction_result["label"].lower() == "contradiction":
            contradictions.append(
                f"Contradiction Score: {round(contradiction_result['score'], 2)}"
            )

    except Exception as e:
        print("Contradiction Error:", e)

    conclusion = (
        findings[-1]
        if findings
        else summary[:150]
    )

    return {
        "themes": themes,
        "findings": findings,
        "insights": insights,
        "contradictions": contradictions,
        "conclusion": conclusion
    }