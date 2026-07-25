from PySide6.QtWidgets import QTextEdit


class ViewerPanel(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.current_file = None

        self.setPlaceholderText(
            "Select a document from the left panel."
        )

    def load_text(self, filepath, text):

        self.current_file = filepath

        self.setPlainText(text)

    def clear_document(self):

        self.current_file = None

        self.clear()