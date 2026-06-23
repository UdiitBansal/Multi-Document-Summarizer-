print("Starting...")

from contradiction_detector import detect_contradiction

print("Imported...")

result = detect_contradiction(
    "Transformers outperform CNNs",
    "CNNs outperform Transformers"
)

print("Finished")

print(result)

