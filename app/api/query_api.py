from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.orchestrator import Orchestrator

router = APIRouter()

orchestrator = Orchestrator()

class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def query_contract(request: QueryRequest):

    answer = orchestrator.run(request.question)

    return {"answer": answer}