from app.services.ollama_client import OllamaClient


class Summarizer:

    def __init__(self):
        self.client = OllamaClient()

    def summarize_chunks(self, chunks):

        summaries = []

        total = len(chunks)

        for i, chunk in enumerate(chunks, start=1):

            print(f"Summarizing chunk {i}/{total}...")

            summary = self.client.summarize(chunk)

            summaries.append(summary)

        return "\n\n".join(summaries)