from transformers import pipeline

print("Loading Summarizer...")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-6-6"
)

print("Summarizer Loaded")
def summarize_text(text):

    text = text[:3000]

    result = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return result[0]["summary_text"]