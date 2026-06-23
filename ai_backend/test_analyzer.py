from analyzer import analyze_summary

summary = """
We focus on a fractional differential equation
in Riesz form discretized by a polynomial
B-Spline collocation method.
"""

result = analyze_summary(summary)

print(result)