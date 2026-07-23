class ChunkProcessor:
    """
    Intelligent paragraph-based chunking.
    """

    def __init__(self, chunk_size=4000):
        self.chunk_size = chunk_size

    def split(self, text):

        paragraphs = [
            p.strip()
            for p in text.split("\n")
            if p.strip()
        ]

        chunks = []
        current = ""

        for para in paragraphs:

            # Paragraph larger than chunk size
            if len(para) > self.chunk_size:

                if current:
                    chunks.append(current)
                    current = ""

                for i in range(0, len(para), self.chunk_size):
                    chunks.append(para[i:i+self.chunk_size])

                continue

            # Add paragraph if it still fits
            if len(current) + len(para) + 1 <= self.chunk_size:
                current += para + "\n"

            else:
                chunks.append(current.strip())
                current = para + "\n"

        if current.strip():
            chunks.append(current.strip())

        return chunks