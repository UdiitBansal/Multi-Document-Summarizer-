from keybert import KeyBERT

print("Loading KeyBERT Model...")

kw_model = KeyBERT()

print("KeyBERT Loaded")


def extract_themes(text):

    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )

    themes = [
        keyword[0]
        for keyword in keywords
    ]

    return themes