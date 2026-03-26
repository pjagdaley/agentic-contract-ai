from langchain_openai import ChatOpenAI


class AnalysisAgent:

    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

    def analyze(self, question, context):

        prompt = f"""
You are a legal expert.

Analyze the contract context and answer the question clearly.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        return response.content