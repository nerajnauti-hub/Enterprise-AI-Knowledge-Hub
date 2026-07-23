from PySide6.QtWidgets import QListWidget


class DocumentPanel(QListWidget):

    def __init__(self):
        super().__init__()

        self.addItem("📄 Sample.pdf")
        self.addItem("📄 Report.docx")
        self.addItem("📊 Budget.xlsx")