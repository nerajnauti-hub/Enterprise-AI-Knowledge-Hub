from pathlib import Path

from app.loaders.pdf_loader import PDFLoader


class DocumentService:

    def __init__(self):
        self.pdf_loader = PDFLoader()

    def open_document(self, filepath):

        extension = Path(filepath).suffix.lower()

        if extension == ".pdf":
            return self.pdf_loader.load(filepath)

        raise ValueError(f"Unsupported file type: {extension}")