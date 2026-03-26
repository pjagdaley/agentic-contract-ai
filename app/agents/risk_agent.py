from langchain_openai import ChatOpenAI


class RiskAgent:

    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

    def analyze_risk(self, context):

        prompt = f"""
You are a legal risk analysis expert.

Analyze the contract and return STRICT JSON format:

{{
  "risks": [],
  "missing_clauses": [],
  "recommendations": []
}}

Context:
{context}
"""

        response = self.llm.invoke(prompt)

        return response.content