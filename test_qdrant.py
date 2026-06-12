from vector_db.qdrant_config import client


collections = client.get_collections()


print("Qdrant Connected Successfully!")
print(collections)