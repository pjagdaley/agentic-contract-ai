from app.agents.retrieval_agent import RetrievalAgent
from app.agents.analysis_agent import AnalysisAgent
from app.agents.risk_agent import RiskAgent
from app.logger import setup_logger

logger = setup_logger()


class Orchestrator:

    def __init__(self):
        self.retrieval_agent = RetrievalAgent()
        self.analysis_agent = AnalysisAgent()
        self.risk_agent = RiskAgent()

    def run(self, question):

        logger.info(f"Question: {question}")
        
        # Step 1: Retrieve context
        context = self.retrieval_agent.retrieve(question)

        if not context or context.strip() == "":
            return "No relevant contract information found."

        if context == "No contract has been uploaded yet.":
            return context

        # Decide task type
        if "risk" in question.lower() or "issue" in question.lower():
            return self.risk_agent.analyze_risk(context)
        
        # Default: normal analysis
        answer = self.analysis_agent.analyze(question, context)
        
        logger.info(f"Response: {answer}")

        return answer