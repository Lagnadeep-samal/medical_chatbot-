from src.retrieval import hybrid_retrieve

from src.hyde import hyde_generation

from src.decomposition import decompose_query

from src.memory import memory

from src.chain import chain


def medical_chat(query):

    sub_queries = decompose_query(query)

    all_docs = []
    queries = sub_queries.split("\n")[:2]

    for q in queries:

        if q.strip() == "":
            continue

        

        docs = hybrid_retrieve(q)

        all_docs.extend(docs)

    context = "\n\n".join([
    doc.page_content[:1000]
    for doc in docs
])

    chat_history = memory.load_memory_variables({})[
        "chat_history"
    ]

    response = chain.invoke({
        "context": context,
        "question": query,
        "chat_history": chat_history
    })

    memory.save_context(
        {"input": query},
        {"output": response}
    )

    return response