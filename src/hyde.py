from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from src.config import (
    GROQ_API_KEY,
    MODEL_NAME
)


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)


def hyde_generation(query):

    prompt = ChatPromptTemplate.from_template(
    """
    Generate a concise hypothetical answer
    for retrieval purposes only.

    Question:
    {question}
    """
)

    chain = prompt | llm

    response = chain.invoke({
        "question": query
    })

    return response.content