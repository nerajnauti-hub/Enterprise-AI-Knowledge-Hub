from app.loaders.pdf_loader import PDFLoader
from app.processors.document_processor import DocumentProcessor


class Pipeline:

    def __init__(self):

        self.loader = PDFLoader()
        self.processor = DocumentProcessor()

    def summarize_pdf(self, filepath):

        print("=" * 60)
        print("Loading Document")
        print("=" * 60)

        document = self.loader.load(filepath)

        print("Document Loaded")
        print()

        print("=" * 60)
        print("Starting AI Processing")
        print("=" * 60)

        result = self.processor.summarize(document.content)

        return result