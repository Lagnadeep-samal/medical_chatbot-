def format_chat_history(chat_history):

    formatted = []

    for msg in chat_history:

        role = msg.__class__.__name__

        if role == "HumanMessage":

            formatted.append(
                f"User: {msg.content}"
            )

        elif role == "AIMessage":

            formatted.append(
                f"Assistant: {msg.content}"
            )

    return "\n".join(formatted)