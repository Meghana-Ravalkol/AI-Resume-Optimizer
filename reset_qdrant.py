from vector_db.qdrant_config import client
import os
from dotenv import load_dotenv


load_dotenv()

collection_name = os.getenv(
    "QDRANT_COLLECTION_NAME"
)

client.delete_collection(
    collection_name=collection_name
)

print("Old collection deleted.")