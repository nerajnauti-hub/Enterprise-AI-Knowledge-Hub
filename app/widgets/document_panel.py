
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
)

from app.document.document_manager import DocumentManager


class DocumentPanel(QWidget):

    # Signal emitted when a document is selected
    document_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.manager = DocumentManager()

        layout = QVBoxLayout(self)

        title = QLabel("📂 Documents")
        title.setStyleSheet("font-size:16px;font-weight:bold;")

        self.list_widget = QListWidget()

        layout.addWidget(title)
        layout.addWidget(self.list_widget)

        self.refresh()

        self.list_widget.itemDoubleClicked.connect(
            self.open_document
        )

    def refresh(self):

        self.list_widget.clear()

        for doc in self.manager.list_documents():

            item = QListWidgetItem(doc["name"])

            item.setData(1, doc["path"])

            self.list_widget.addItem(item)

    def open_document(self, item):

        filepath = item.data(1)

        self.document_selected.emit(filepath)