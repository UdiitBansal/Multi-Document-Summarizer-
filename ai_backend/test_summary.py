from pdf_utils import extract_text
from chunker import chunk_text

from embedding import (
    generate_embeddings,
    store_chunks
)

from hybrid_search import HybridRetriever
from summarizer import summarize_text


text = extract_text("sample.pdf")

chunks = chunk_text(text)

embeddings = generate_embeddings(
    chunks[:20]
)

store_chunks(
    chunks[:20],
    embeddings
)

retriever = HybridRetriever(
    chunks[:20]
)

results = retriever.search(
    "Riesz fractional equation"
)

combined_text = "\n".join(results)

summary = summarize_text(
    combined_text
)

print("\nSUMMARY:\n")
print(summary)