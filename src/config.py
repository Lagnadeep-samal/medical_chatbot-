import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

PINECONE_INDEX = os.getenv("PINECONE_INDEX")

MODEL_NAME = "llama-3.1-8b-instant"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"