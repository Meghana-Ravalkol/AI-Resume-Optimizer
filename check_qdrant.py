import os
from dotenv import load_dotenv

from vector_db.qdrant_config import client


load_dotenv()

collection_name = os.getenv(
    "QDRANT_COLLECTION_NAME"
)


info = client.get_collection(
    collection_name=collection_name
)

print(info)