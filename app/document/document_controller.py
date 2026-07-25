from app.services.document_service import DocumentService


class DocumentController:

    def __init__(self):

        self.service = DocumentService()

    def open_document(self, filepath):

        return self.service.open_document(filepath)