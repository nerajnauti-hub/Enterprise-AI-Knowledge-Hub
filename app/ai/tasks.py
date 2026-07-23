from enum import Enum


class AITask(str, Enum):
    SUMMARIZE = "summarize"
    IMPROVE_ENGLISH = "improve_english"
    REWRITE = "rewrite"
    MERGE = "merge"
    TRANSLATE = "translate"
    QUESTION_ANSWER = "question_answer"
    EXTRACT_ACTIONS = "extract_actions"