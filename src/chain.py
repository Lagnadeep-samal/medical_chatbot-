from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from src.config import (
    GROQ_API_KEY,
    MODEL_NAME
)


llm = ChatGroq(

    groq_api_key=GROQ_API_KEY,

    model_name=MODEL_NAME,

    temperature=0.3
)


prompt = ChatPromptTemplate.from_template(
    """
You are an intelligent medical AI assistant.

Use the conversation history internally
to understand follow-up questions.

DO NOT display:
- Chat History
- Previous Conversation
- User:
- Assistant:

Answer ONLY the user's current question.

Use ONLY the provided medical context.

Keep responses:
- clean
- professional
- easy to understand
- concise

Do NOT use markdown symbols like:
**
##
__

Medical Context:
{context}

Conversation Memory:
{chat_history}

Current User Question:
{question}
"""
)


parser = StrOutputParser()

chain = prompt | llm | parser