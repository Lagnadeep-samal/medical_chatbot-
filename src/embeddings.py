import os

from langchain_huggingface import HuggingFaceEndpointEmbeddings

from src.config import EMBEDDING_MODEL


def download_embeddings():

    embeddings = HuggingFaceEndpointEmbeddings(
        model=EMBEDDING_MODEL,
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )

    return embeddings