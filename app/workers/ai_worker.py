from PySide6.QtCore import QObject, Signal

from app.ai.ai_controller import AIController


class AIWorker(QObject):

    finished = Signal(str)
    error = Signal(str)

    def __init__(self, task, document=None, question=None):
        super().__init__()

        self.task = task
        self.document = document
        self.question = question

        self.ai = AIController()

    def run(self):

        try:

            if self.task == "Summarize":

                result = self.ai.summarize(
                    self.document
                )

            elif self.task == "Ask AI":

                result = self.ai.ask(
                    self.question
                )

            else:

                result = f"Unsupported task: {self.task}"

            self.finished.emit(result)

        except Exception as e:

            self.error.emit(str(e))