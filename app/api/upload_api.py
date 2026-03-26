from fastapi import APIRouter, UploadFile, File
import os
from app.services.rag_instance import rag_service 

router = APIRouter()

@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):

    file_path = f"data/{file.filename}"

    # Save file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Index document
    chunks = rag_service.load_and_index(file_path)

    return {
        "message": "Contract uploaded and indexed",
        "chunks": chunks
    }