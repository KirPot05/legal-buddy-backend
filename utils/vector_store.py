from sentence_transformers import SentenceTransformer
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from config import PINECONE_API_KEY


vector_model = SentenceTransformer('all-MiniLM-L6-v2')
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "document-summaries"


if index_name not in pc.list_indexes().names():
    pc.create_index(index_name, dimension=384, spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    ))

pinecone_index = pc.Index(index_name)


def save_to_pinecone(summary, file_name, timestamp):
    vector = vector_model.encode(
        summary, output_value="sentence_embedding").tolist()
    metadata = {
        "file_name": file_name,
        "timestamp": timestamp,
        "summary": summary
    }

    formatted_vectors = []
    formatted_vectors.append({
        'id': timestamp,
        'values': vector,
        'metadata': metadata
    })

    pinecone_index.upsert(vectors=formatted_vectors, namespace='ns1')
    return vector
