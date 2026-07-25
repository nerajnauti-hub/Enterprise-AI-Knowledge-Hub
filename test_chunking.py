from app.chunking.chunk_engine import ChunkEngine

engine = ChunkEngine()

text = "Hello " * 1500

chunks = engine.create_chunks(text)

print(len(chunks))

for i, chunk in enumerate(chunks):

    print(i + 1, len(chunk.split()))