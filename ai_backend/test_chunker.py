from pdf_utils import extract_text
from chunker import chunk_text

text = extract_text("sample.pdf")

chunks = chunk_text(text)

print(f"\nTotal Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks[:3]):
    print("=" * 60)
    print(f"Chunk {i+1}")
    print("=" * 60)
    print(chunk[:300])
    print()