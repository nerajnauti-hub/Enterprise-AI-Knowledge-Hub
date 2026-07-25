from uuid import uuid4

from app.chunking.chunk_engine import ChunkEngine
from app.vectorstore.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


class Indexer:

    def __init__(self):

        self.chunk_engine = ChunkEngine()
        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaStore()

    def index_document(self, document):

        chunks = self.chunk_engine.create_chunks(
            document.content
        )

        print(f"Created {len(chunks)} chunks")

        for i, chunk in enumerate(chunks):

            embedding = self.embedding_service.embed_text(
                chunk
            )

            self.vector_store.add_document(

                chunk_id=str(uuid4()),

                text=chunk,

                embedding=embedding,

                metadata={
                    "filename": document.filename,
                    "chunk": i + 1
                }
            )

        print("Document indexed successfully.")