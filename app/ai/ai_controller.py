from app.pipeline.pipeline import Pipeline


class AIController:

    def __init__(self):
        self.pipeline = Pipeline()

    def summarize(self, document):
        return self.pipeline.summarize(document)