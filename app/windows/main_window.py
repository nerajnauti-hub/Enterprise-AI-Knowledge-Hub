from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QSplitter,
    QStatusBar,
    QToolBar,
)

from app.widgets.document_panel import DocumentPanel
from app.widgets.viewer_panel import ViewerPanel
from app.widgets.ai_panel import AIPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Enterprise AI Knowledge Hub v0.3")
        self.resize(1700, 950)

        # Create UI
        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()

        # Central Widget
        central = QWidget()
        self.setCentralWidget(central)

        # Main Layout
        layout = QHBoxLayout()
        central.setLayout(layout)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)

        # Panels
        self.document_panel = DocumentPanel()
        self.viewer_panel = ViewerPanel()
        self.ai_panel = AIPanel()

        splitter.addWidget(self.document_panel)
        splitter.addWidget(self.viewer_panel)
        splitter.addWidget(self.ai_panel)

        # Initial sizes
        splitter.setSizes([250, 950, 350])

        # Add splitter to layout
        layout.addWidget(splitter)

    def create_menu(self):

        menu = self.menuBar()

        menu.addMenu("File")
        menu.addMenu("Edit")
        menu.addMenu("View")
        menu.addMenu("AI")
        menu.addMenu("Tools")
        menu.addMenu("Settings")
        menu.addMenu("Help")

    def create_toolbar(self):

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(Qt.TopToolBarArea, toolbar)

    def create_statusbar(self):

        status = QStatusBar()

        status.showMessage(
            "Ready | Ollama: Connected | Model: qwen2.5:3b"
        )

        self.setStatusBar(status)