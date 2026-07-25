from app.vectorstore.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


class Retriever:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaStore()

    def search(self, question, top_k=5):

        embedding = self.embedding_service.embed_text(question)

        results = self.vector_store.search(
            embedding=embedding,
            top_k=top_k
        )

        return results