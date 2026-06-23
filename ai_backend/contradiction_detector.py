from transformers import pipeline

print("Loading NLI Model...")

classifier = pipeline(
    "text-classification",
    model="valhalla/distilbart-mnli-12-3"
)

print("NLI Model Loaded")


def detect_contradiction(text1, text2):

    result = classifier(
        f"{text1}</s></s>{text2}"
    )

    prediction = result[0]

    return {
        "label": prediction["label"],
        "score": prediction["score"]
    }