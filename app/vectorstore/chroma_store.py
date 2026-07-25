import chromadb


class ChromaStore:

    def __init__(self, path="data/chroma"):

        self.client = chromadb.PersistentClient(path=path)

        self.collection = self.client.get_or_create_collection(
            name="enterprise_documents"
        )

    def add_document(
        self,
        chunk_id,
        text,
        embedding,
        metadata,
    ):

        self.collection.add(
            ids=[chunk_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata],
        )

    def search(self, embedding, top_k=5):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )