from pathlib import Path


class DocumentManager:

    def __init__(self, document_folder="documents"):

        self.document_folder = Path(document_folder)

    def list_documents(self):

        if not self.document_folder.exists():
            return []

        supported = {
            ".pdf",
            ".docx",
            ".txt",
            ".xlsx",
            ".pptx"
        }

        files = []

        for file in sorted(self.document_folder.iterdir()):

            if file.suffix.lower() in supported:

                files.append(
                    {
                        "name": file.name,
                        "path": str(file),
                        "extension": file.suffix.lower(),
                        "size": file.stat().st_size
                    }
                )

        return files