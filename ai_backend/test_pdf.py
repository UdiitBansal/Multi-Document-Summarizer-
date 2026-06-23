from pdf_utils import extract_text

pdf_path = "sample.pdf"

text = extract_text(pdf_path)

print("\nFirst 1000 Characters:\n")
print(text[:1000])