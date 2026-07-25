from app.processors.document_processor import DocumentProcessor


class Pipeline:

    def __init__(self):
        self.processor = DocumentProcessor()

    def summarize(self, document):
        return self.processor.summarize(document.content)