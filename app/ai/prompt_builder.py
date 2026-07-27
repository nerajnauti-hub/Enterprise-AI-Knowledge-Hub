class PromptBuilder:

    def build(self, question, retrieved_chunks):

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are an AI assistant.

Answer ONLY using the information contained in the context.

If the answer cannot be found in the context, reply:

"I could not find that information in the indexed documents."

-----------------------
CONTEXT

{context}

-----------------------

QUESTION

{question}

ANSWER:
"""

        return prompt