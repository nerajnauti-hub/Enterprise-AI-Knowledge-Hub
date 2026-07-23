from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QComboBox,
)


class AIPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Task"))

        self.task = QComboBox()

        self.task.addItems([
            "Summarize",
            "Improve English",
            "Merge Documents",
            "Translate",
            "Ask AI"
        ])

        layout.addWidget(self.task)

        layout.addWidget(QLabel("Pages"))

        self.pages = QTextEdit()

        self.pages.setMaximumHeight(60)

        layout.addWidget(self.pages)

        self.process = QPushButton("Process")

        layout.addWidget(self.process)

        layout.addStretch()