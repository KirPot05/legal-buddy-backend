import config
from fastapi import FastAPI, File, UploadFile, HTTPException
import uuid
import os
from dotenv import load_dotenv
import uvicorn
from utils.vector_store import save_to_pinecone
from models.summary import SummaryResponse
from services.translation import translate_text
from utils.db import save_to_db, summaries_collection
from services.summary import generate_summary
from services.document import extract_text_from_document


app = FastAPI()


@app.post("/upload", response_model=SummaryResponse)
async def upload_document(file: UploadFile = File(...)):

    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file format")

    file_id = str(uuid.uuid4())
    file_path = f"temp/{file_id}_{file.filename}"
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    try:
        transcription = extract_text_from_document(
            file_path, mime_type=file.content_type)

    except Exception as e:
        os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"OCR failed: {str(e)}")

    summary_english = await generate_summary(transcription)
    summary_kannada = await translate_text(summary_english, target_language="kn")

    save_to_pinecone(summary_english, file.filename, file_id)

    timestamp = save_to_db(
        file.filename, transcription, summary_english, summary_kannada, file_id)

    os.remove(file_path)

    return {
        "summary_english": summary_english,
        "summary_kannada": summary_kannada,
        "timestamp": timestamp,
    }


@app.get("/summaries/{timestamp}", response_model=SummaryResponse)
async def get_summary(timestamp: str):
    doc = summaries_collection.find_one({"timestamp": timestamp})
    if not doc:
        raise HTTPException(status_code=404, detail="Summary not found")
    return {
        "summary_english": doc["summary_english"],
        "summary_kannada": doc["summary_kannada"]
    }


@app.get("/summaries")
async def list_summaries():
    summaries = list(summaries_collection.find(
        {}, {"_id": 0, "file_name": 1, "timestamp": 1}))
    return summaries


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)
