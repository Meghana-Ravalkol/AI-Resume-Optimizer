import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from qdrant_client.models import Filter, FieldCondition, MatchValue

from vector_db.qdrant_config import client


load_dotenv()


COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def retrieve_knowledge(query, limit=3, sources=None):

    query_embedding = embedding_model.embed_query(query)

    search_filter = None

    if sources:
        search_filter = Filter(
            should=[
                FieldCondition(
                    key="source",
                    match=MatchValue(value=source)
                )
                for source in sources
            ]
        )

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        query_filter=search_filter,
        limit=limit
    ).points

    context = "\n\n".join(
        point.payload["text"]
        for point in results
    )

    return context