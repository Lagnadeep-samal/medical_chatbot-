from rank_bm25 import BM25Okapi

from src.vectorstore import load_vectorstore




def hybrid_retrieve(query):

    vectorstore = load_vectorstore()
    # Dense similarity search
    dense_docs = vectorstore.similarity_search(
        query,
        k=3
    )

    # Sparse BM25 reranking
    corpus = [
        doc.page_content
        for doc in dense_docs
    ]

    tokenized = [
        doc.split()
        for doc in corpus
    ]

    bm25 = BM25Okapi(tokenized)

    scores = bm25.get_scores(
        query.lower().split()
    )

    ranked_docs = sorted(
        zip(scores, dense_docs),
        reverse=True,
        key=lambda x: x[0]
    )

    final_docs = [
        doc
        for _, doc in ranked_docs
    ]

    return final_docs[:3]