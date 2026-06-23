from pdf_utils import extract_text
from chunker import chunk_text
from embedding import generate_embeddings

text = extract_text("sample.pdf")

chunks = chunk_text(text)

chunks = chunks[:5]

embeddings = generate_embeddings(chunks)

print("\nEmbedding Shape:")
print(embeddings.shape)

print("\nFirst Vector (First 10 Values):")
print(embeddings[0][:10])