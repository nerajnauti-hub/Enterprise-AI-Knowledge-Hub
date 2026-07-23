from app.ai.tasks import AITask


PROMPTS = {

    AITask.SUMMARIZE: """
You are an expert document analyst.

Summarize the following document.

Requirements:
- Preserve important facts.
- Use bullet points.
- Mention important names.
- Mention dates.
- Mention conclusions.
- Do not invent information.

Document:

{text}
""",

    AITask.IMPROVE_ENGLISH: """
You are an expert English editor.

Improve the English while preserving the original meaning.

Document:

{text}
""",

    AITask.REWRITE: """
Rewrite the following document professionally.

Document:

{text}
""",

    AITask.MERGE: """
Merge the following documents into one structured document.

{text}
""",

    AITask.TRANSLATE: """
Translate the following document into English.

{text}
""",

    AITask.QUESTION_ANSWER: """
Answer the question using ONLY the supplied document.

Document:

{text}

Question:

{question}
""",

    AITask.EXTRACT_ACTIONS: """
Extract all action items from the document.

Document:

{text}
"""
}