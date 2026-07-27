from PySide6.QtCore import Qt, QThread
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

from app.document.document_controller import DocumentController
from app.workers.ai_worker import AIWorker


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Enterprise AI Knowledge Hub v0.5")
        self.resize(1700, 950)

        # -----------------------------------
        # Controllers
        # -----------------------------------
        self.document_controller = DocumentController()

        self.current_document = None
        self.thread = None
        self.worker = None

        # -----------------------------------
        # UI
        # -----------------------------------
        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        splitter = QSplitter(Qt.Horizontal)

        self.document_panel = DocumentPanel()
        self.viewer_panel = ViewerPanel()
        self.ai_panel = AIPanel()

        splitter.addWidget(self.document_panel)
        splitter.addWidget(self.viewer_panel)
        splitter.addWidget(self.ai_panel)

        splitter.setSizes([260, 950, 380])

        layout.addWidget(splitter)

        # -----------------------------------
        # Signals
        # -----------------------------------

        self.document_panel.document_selected.connect(
            self.open_document
        )

        self.ai_panel.process.clicked.connect(
            self.run_ai
        )

    # =====================================================

    def open_document(self, filepath):

        try:

            document = self.document_controller.open_document(
                filepath
            )

            self.current_document = document

            self.viewer_panel.load_text(
                filepath,
                document.content
            )

            self.statusBar().showMessage(
                f"Opened : {document.filename}"
            )

        except Exception as e:

            self.statusBar().showMessage(str(e))

    # =====================================================

    def run_ai(self):

        task = self.ai_panel.task.currentText()

        if task == "Summarize":

            if self.current_document is None:

                self.ai_panel.result.setPlainText(
                    "Please open a document first."
                )

                return

            self.worker = AIWorker(
                task="Summarize",
                document=self.current_document
            )

        elif task == "Ask AI":

            question = self.ai_panel.question.text().strip()

            if question == "":

                self.ai_panel.result.setPlainText(
                    "Please enter a question."
                )

                return

            self.worker = AIWorker(
                task="Ask AI",
                question=question
            )

        else:

            self.ai_panel.result.setPlainText(
                f"{task} not implemented yet."
            )

            return

        self.ai_panel.progress.setValue(0)
        self.ai_panel.process.setEnabled(False)

        self.thread = QThread()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(
            self.worker.run
        )

        self.worker.finished.connect(
            self.ai_finished
        )

        self.worker.error.connect(
            self.ai_error
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    # =====================================================

    def ai_finished(self, result):

        self.ai_panel.progress.setValue(100)

        self.ai_panel.result.setPlainText(result)

        self.ai_panel.process.setEnabled(True)

        self.statusBar().showMessage(
            "AI task completed."
        )

    # =====================================================

    def ai_error(self, error):

        self.ai_panel.progress.setValue(0)

        self.ai_panel.result.setPlainText(error)

        self.ai_panel.process.setEnabled(True)

        self.statusBar().showMessage(error)

    # =====================================================

    def create_menu(self):

        menu = self.menuBar()

        menu.addMenu("File")
        menu.addMenu("Edit")
        menu.addMenu("View")
        menu.addMenu("AI")
        menu.addMenu("Tools")
        menu.addMenu("Settings")
        menu.addMenu("Help")

    # =====================================================

    def create_toolbar(self):

        toolbar = QToolBar("Main Toolbar")

        self.addToolBar(
            Qt.TopToolBarArea,
            toolbar
        )

    # =====================================================

    def create_statusbar(self):

        status = QStatusBar()

        status.showMessage(
            "Ready | Enterprise AI Knowledge Hub v0.5"
        )

        self.setStatusBar(status)