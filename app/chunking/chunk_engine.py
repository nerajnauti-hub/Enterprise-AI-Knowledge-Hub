class ChunkEngine:

    def __init__(self, chunk_size=500, overlap=100):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def create_chunks(self, text):

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + self.chunk_size

            chunk = " ".join(words[start:end])

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks