from app.vectorstore.embedding_service import EmbeddingService

model = EmbeddingService()

vector = model.embed_text(
    "Enterprise AI Knowledge Hub"
)

print(type(vector))
print(len(vector))
print(vector[:10])