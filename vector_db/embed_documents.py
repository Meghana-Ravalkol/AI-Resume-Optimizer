import os
import uuid

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance,
    PayloadSchemaType
)
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from vector_db.qdrant_config import client


load_dotenv()


COLLECTION_NAME = os.getenv(
    "QDRANT_COLLECTION_NAME"
)


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def load_knowledge():

    chunks = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=50
    )

    knowledge_path = "knowledge"

    for filename in os.listdir(knowledge_path):

        file_path = os.path.join(
            knowledge_path,
            filename
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

            text_chunks = splitter.split_text(
                text
            )

            for chunk in text_chunks:

                chunks.append(
                    {
                        "text": chunk,
                        "source": filename
                    }
                )

            print(
                f"{filename} -> {len(text_chunks)} chunks"
            )

    return chunks


def embed_documents():

    documents = load_knowledge()

    print(
        f"Loaded {len(documents)} chunks"
    )

    texts = [
        doc["text"]
        for doc in documents
    ]

    embeddings = embedding_model.embed_documents(
        texts
    )


    # Create collection
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=len(embeddings[0]),
            distance=Distance.COSINE
        )
    )


    # Create index for source filtering
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="source",
        field_schema=PayloadSchemaType.KEYWORD
    )


    points = []

    for doc, vector in zip(
        documents,
        embeddings
    ):

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": doc["text"],
                    "source": doc["source"]
                }
            )
        )


    # Upload in batches to avoid timeout
    batch_size = 50

    for i in range(
        0,
        len(points),
        batch_size
    ):

        batch = points[
            i:i + batch_size
        ]

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )

        print(
            f"Uploaded {i + len(batch)}/{len(points)} chunks"
        )


    print(
        f"\nSuccessfully stored {len(points)} chunks in Qdrant!"
    )


if __name__ == "__main__":

    print(
        "Starting embedding..."
    )

    embed_documents()