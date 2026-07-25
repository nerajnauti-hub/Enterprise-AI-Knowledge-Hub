from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QComboBox,
    QProgressBar,
)


class AIPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # -----------------------------
        # Task Selection
        # -----------------------------
        layout.addWidget(QLabel("Task"))

        self.task = QComboBox()
        self.task.addItems([
            "Summarize",
            "Improve English",
            "Translate",
            "Merge Documents",
            "Ask AI",
        ])

        layout.addWidget(self.task)

        # -----------------------------
        # Model Selection
        # -----------------------------
        layout.addWidget(QLabel("Model"))

        self.model = QComboBox()
        self.model.addItems([
            "qwen2.5:3b",
        ])

        layout.addWidget(self.model)

        # -----------------------------
        # Page Selection
        # -----------------------------
        layout.addWidget(QLabel("Pages"))

        self.pages = QTextEdit()
        self.pages.setMaximumHeight(70)
        self.pages.setPlaceholderText(
            "Examples:\n"
            "All\n"
            "1-5\n"
            "3"
        )

        layout.addWidget(self.pages)

        # -----------------------------
        # Run Button
        # -----------------------------
        self.process = QPushButton("▶ Run AI")
        layout.addWidget(self.process)

        # -----------------------------
        # Progress Bar
        # -----------------------------
        layout.addWidget(QLabel("Progress"))

        self.progress = QProgressBar()
        self.progress.setValue(0)

        layout.addWidget(self.progress)

        # -----------------------------
        # AI Output
        # -----------------------------
        layout.addWidget(QLabel("AI Output"))

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        layout.addWidget(self.result)

        layout.addStretch()