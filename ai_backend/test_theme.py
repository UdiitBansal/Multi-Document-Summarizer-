from theme_extractor import extract_themes

text = """
Machine learning and deep learning are widely used
for disease prediction and healthcare analytics.
"""

themes = extract_themes(text)

print(themes)