from app.retrieval.retriever import Retriever

retriever = Retriever()

results = retriever.search(
    "What is the story about?"
)

print(results)