from pathlib import Path

from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DOCXLoader


class DocumentService:

    def __init__(self):

        self.pdf_loader = PDFLoader()
        self.docx_loader = DOCXLoader()

    def open_document(self, filepath):

        extension = Path(filepath).suffix.lower()

        if extension == ".pdf":
            return self.pdf_loader.load(filepath)

        elif extension == ".docx":
            return self.docx_loader.load(filepath)

        else:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )