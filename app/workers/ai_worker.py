from PySide6.QtCore import QObject, Signal

from app.ai.ai_controller import AIController


class AIWorker(QObject):

    finished = Signal(str)
    error = Signal(str)

    def __init__(self, document):
        super().__init__()
        self.document = document
        self.ai = AIController()

    def run(self):
        try:
            result = self.ai.summarize(self.document)
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))