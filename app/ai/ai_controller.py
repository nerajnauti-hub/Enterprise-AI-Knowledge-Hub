from app.ai.engine import AIEngine
from app.ai.tasks import AITask

from app.retrieval.retriever import Retriever
from app.ai.prompt_builder import PromptBuilder


class AIController:

    def __init__(self):

        self.engine = AIEngine()

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

    # -----------------------------
    # Existing Summary
    # -----------------------------
    def summarize(self, document):

        return self.engine.run(

            task=AITask.SUMMARIZE,

            text=document.content

        )

    # -----------------------------
    # New RAG
    # -----------------------------
    def ask(self, question):

        results = self.retriever.search(question)

        chunks = results["documents"][0]

        prompt = self.prompt_builder.build(

            question,

            chunks

        )

        return self.engine.generate(prompt)