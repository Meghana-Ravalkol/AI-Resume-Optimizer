import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables
load_dotenv()


# OpenRouter Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "openai/gpt-4o-mini"
)


# Project Configuration
MAX_QUESTIONS = int(
    os.getenv("MAX_QUESTIONS", 5)
)


# Qdrant Configuration
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")


# Initialize LLM
llm = ChatOpenAI(
    model=MODEL_NAME,
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY
)