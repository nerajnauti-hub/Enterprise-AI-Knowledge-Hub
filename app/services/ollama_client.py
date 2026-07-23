import ollama


class OllamaClient:

    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def generate(self, prompt):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def summarize(self, text):

        prompt = f"""
You are an expert document analyst.

Summarize the following text.

Text:

{text}
"""

        return self.generate(prompt)