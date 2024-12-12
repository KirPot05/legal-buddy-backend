from pymongo import MongoClient
from config import DB_URI, DB_NAME

mongo_client = MongoClient(DB_URI)
db = mongo_client.get_database(DB_NAME)
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
