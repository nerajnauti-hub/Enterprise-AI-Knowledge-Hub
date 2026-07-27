from PySide6.QtCore import QObject, Signal

from app.indexing.indexer import Indexer


class IndexingWorker(QObject):

    finished = Signal(str)
    error = Signal(str)
    progress = Signal(str)

    def __init__(self, document):
        super().__init__()

        self.document = document
        self.indexer = Indexer()

    def run(self):

        try:

            self.progress.emit(f"Starting indexing of {self.document.filename}...")

            self.indexer.index_document(self.document)

            self.progress.emit("Indexing completed successfully!")

            self.finished.emit(
                f"Document '{self.document.filename}' indexed successfully. "
                f"You can now ask questions about it."
            )

        except Exception as e:

            error_msg = f"Error indexing document: {str(e)}"

            self.error.emit(error_msg)
