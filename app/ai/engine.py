from app.ai.prompts import PROMPTS
from app.ai.tasks import AITask
from app.services.ollama_client import OllamaClient


class AIEngine:

    def __init__(self):

        self.client = OllamaClient()

    def run(self, task, text, **kwargs):

        if task not in PROMPTS:
            raise ValueError(f"Unsupported task: {task}")

        prompt = PROMPTS[task].format(
            text=text,
            **kwargs
        )

        return self.client.generate(prompt)