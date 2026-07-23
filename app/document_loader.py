from pathlib import Path
import fitz  # PyMuPDF


class DocumentLoader:
    def __init__(self, documents_folder="documents"):
        self.documents_folder = Path(documents_folder)

    def load_pdfs(self):
        documents = []

        pdf_files = list(self.documents_folder.glob("*.pdf"))

        if not pdf_files:
            return documents

        for pdf in pdf_files:

            print(f"Reading {pdf.name}")

            doc = fitz.open(pdf)

            for page_number, page in enumerate(doc, start=1):

                text = page.get_text()

                documents.append({
                    "file": pdf.name,
                    "page": page_number,
                    "text": text
                })

            doc.close()

        return documents