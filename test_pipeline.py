from pathlib import Path

from app.pipeline.pipeline import Pipeline

pipeline = Pipeline()

pdf = Path("documents/Sample.pdf")

result = pipeline.summarize_pdf(str(pdf))

print()

print("=" * 80)
print("FINAL SUMMARY")
print("=" * 80)

print(result)