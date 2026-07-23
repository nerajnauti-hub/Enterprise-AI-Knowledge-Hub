from app.ai.engine import AIEngine
from app.ai.tasks import AITask
from app.processors.chunk_processor import ChunkProcessor


class DocumentProcessor:

    def __init__(self):

        self.chunker = ChunkProcessor()

        self.ai = AIEngine()

    def summarize(self, text):

        chunks = self.chunker.split(text)

        print("=" * 60)
        print("Document Processing Started")
        print("=" * 60)

        print(f"Total Chunks : {len(chunks)}")
        print()

        summaries = []

        for index, chunk in enumerate(chunks):

            print(f"Processing Chunk {index+1}/{len(chunks)}")

            summary = self.ai.run(
                task=AITask.SUMMARIZE,
                text=chunk
            )

            summaries.append(summary)

        print()
        print("Combining Results...")

        final_summary = "\n\n".join(summaries)

        return final_summary