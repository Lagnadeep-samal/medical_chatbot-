from src.router import route_query

from src.retrieval import hybrid_retrieve

from src.memory import memory

from src.chain import chain

from src.utils import format_chat_history


def adaptive_medical_chat(query):

    route = route_query(query)

    # LOAD RAW MEMORY
    raw_history = memory.load_memory_variables({})[
        "chat_history"
    ]

    # FORMAT MEMORY CLEANLY
    chat_history = format_chat_history(
        raw_history
    )

    # GREETING ROUTE
    if route == "greeting":

        response = """
Hello! 👋

I am your AI Medical Assistant.

You can ask me about:
- diseases
- symptoms
- treatments
- medicines
- medical concepts
"""

        return response

    # MEMORY ROUTE
    elif route == "memory":

        response = chain.invoke({

            "context": "",

            "question": query,

            "chat_history": chat_history
        })

        # SAVE MEMORY
        memory.save_context(
            {"input": query},
            {"output": response}
        )

        return response

    # RETRIEVAL ROUTE
    else:

        docs = hybrid_retrieve(query)

        context = "\n\n".join([
            doc.page_content[:1000]
            for doc in docs
        ])

        response = chain.invoke({

            "context": context,

            "question": query,

            "chat_history": chat_history
        })

        # SAVE MEMORY
        memory.save_context(
            {"input": query},
            {"output": response}
        )

        return response