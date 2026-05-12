from langchain_pinecone import PineconeVectorStore

from src.config import PINECONE_INDEX

from src.embeddings import download_embeddings


embedding = download_embeddings()


def upload_to_pinecone(chunks):

    vectorstore = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embedding,
        index_name=PINECONE_INDEX,
        batch_size=20
    )

    return vectorstore


def load_vectorstore():

    vectorstore = PineconeVectorStore(
        index_name=PINECONE_INDEX,
        embedding=embedding
    )

    return vectorstore