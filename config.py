import os

MONGO_URI = "mongodb://localhost:27017"
GCP_VISION_CREDENTIALS = "./creds.json"
PINECONE_API_KEY = "pcsk_4N4Cfj_3adLwq2CAmpANMRENopacSx7NwCoeMvyRh3DeNmg1EPf2uSGRQqGFDnJM6s6paw"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GCP_VISION_CREDENTIALS
