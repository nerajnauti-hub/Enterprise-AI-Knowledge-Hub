from PySide6.QtWidgets import QTextEdit


class ViewerPanel(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setPlaceholderText(
            "Document Viewer\n\n"
            "PDF, DOCX and Excel documents will appear here."
        )