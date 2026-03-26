from fastapi import FastAPI
from app.api.upload_api import router as upload_router
from app.api.query_api import router as query_router


app = FastAPI(title="Agentic Contract AI")


@app.get("/")
def root():
    return {"message": "Agentic AI System Running"}

app.include_router(upload_router)
app.include_router(query_router)