import os
from dotenv import load_dotenv

load_dotenv()


DB_URI = os.getenv("DB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME")

GCP_VISION_CREDENTIALS = os.getenv("GCP_VISION_CREDENTIALS", "./creds.json")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_LOCATION = os.getenv("GCP_LOCATION")
GCP_DOCUMENT_AI_PROCESSOR_ID = os.getenv("GCP_DOCUMENT_AI_PROCESSOR_ID")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GCP_VISION_CREDENTIALS
