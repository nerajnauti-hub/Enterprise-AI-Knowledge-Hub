from app.ai.engine import AIEngine
from app.ai.tasks import AITask

engine = AIEngine()

text = """
Artificial Intelligence is transforming cybersecurity.
Machine learning helps identify threats faster than traditional systems.
"""

result = engine.run(
    task=AITask.SUMMARIZE,
    text=text
)

print("\n")
print("=" * 60)
print(result)
print("=" * 60)