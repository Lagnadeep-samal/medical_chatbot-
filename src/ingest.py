from src.load import load_pdf

from src.splitter import split_documents

from src.vectorstore import upload_to_pinecone


documents = load_pdf(
    "data/medical_book.pdf"
)

chunks = split_documents(documents)

upload_to_pinecone(chunks)

print("Vector Database Created Successfully")