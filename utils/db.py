from pymongo import MongoClient
from config import MONGO_URI

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["legal_doc_summarizer"]
summaries_collection = db["summaries"]


def save_to_db(file_name, transcription, summary_en, summary_ka, timestamp):
    doc = {
        "file_name": file_name,
        "transcription": transcription,
        "summary_english": summary_en,
        "summary_kannada": summary_ka,
        "timestamp": timestamp,
    }
    summaries_collection.insert_one(doc)
    return timestamp
