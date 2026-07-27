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
from app.workers.indexing_worker import IndexingWorker


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
        self.indexing_thread = None
        self.indexing_worker = None

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

            # Automatically index the document
            self.index_document(document)

        except Exception as e:

            self.statusBar().showMessage(str(e))

    # =====================================================

    def index_document(self, document):
        """Automatically index the document in the background"""

        self.statusBar().showMessage(
            f"Indexing: {document.filename}..."
        )

        self.indexing_worker = IndexingWorker(document)

        self.indexing_thread = QThread()

        self.indexing_worker.moveToThread(self.indexing_thread)

        self.indexing_thread.started.connect(
            self.indexing_worker.run
        )

        self.indexing_worker.finished.connect(
            self.on_indexing_finished
        )

        self.indexing_worker.error.connect(
            self.on_indexing_error
        )

        self.indexing_worker.progress.connect(
            self.on_indexing_progress
        )

        self.indexing_worker.finished.connect(
            self.indexing_thread.quit
        )

        self.indexing_thread.finished.connect(
            self.indexing_thread.deleteLater
        )

        self.indexing_thread.start()

    # =====================================================

    def on_indexing_progress(self, message):
        """Handle indexing progress updates"""

        self.statusBar().showMessage(message)

    # =====================================================

    def on_indexing_finished(self, message):
        """Handle successful indexing completion"""

        self.statusBar().showMessage(message)

    # =====================================================

    def on_indexing_error(self, error):
        """Handle indexing errors"""

        error_msg = f"Indexing failed: {error}"

        self.statusBar().showMessage(error_msg)

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
