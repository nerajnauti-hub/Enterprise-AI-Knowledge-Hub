import fitz
from app.models.document import Document
from app.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):

    def load(self, filepath: str) -> Document:

        pdf = fitz.open(filepath)

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return Document(
            filename=filepath,
            filetype="pdf",
            content=text
        )