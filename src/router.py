def route_query(query):

    query = query.lower()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    memory_keywords = [
        "previous",
        "earlier",
        "last question",
        "what did i ask",
        "remember"
    ]

    # Greeting Route
    if any(word in query for word in greetings):

        return "greeting"

    # Memory Route
    if any(word in query for word in memory_keywords):

        return "memory"

    # Retrieval Route
    return "retrieval"