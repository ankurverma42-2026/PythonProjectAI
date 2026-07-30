"""
RAG Application

1. Retrieve relevant documents from ChromaDB.
2. Build context from retrieved documents.
3. Send the context and question to OpenAI.
4. Return the generated answer.
"""

import os
from openai import OpenAI
from query import search_vector_db, build_context


# Read the OpenAI API key from the environment.
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Initialize the OpenAI client.
client = OpenAI(api_key=API_KEY)


def ask_openai(question: str, context: str) -> str:
    """
    Generate an answer using OpenAI based on the retrieved context.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Answer only using the provided context. "
                    "If the answer is not present in the context, "
                    "respond with: 'I don't know based on the provided information.'"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n{context}\n\n"
                    f"Question:\n{question}"
                ),
            },
        ],
    )
    return response.choices[0].message.content

def rag_answer(question: str) -> str:
    """
    Execute the complete RAG pipeline.
    """
    search_results = search_vector_db(question)

    # Build the context that will be sent to the LLM.
    context = build_context(search_results)

    # Display retrieved context (useful for debugging).
    print("\n========== Retrieved Context ==========")
    print(context)
    print("=======================================\n")

    # Generate the final answer.
    return ask_openai(question, context)


def main():
    """Application entry point."""

    question = "Which car has the best fuel economy?"
    answer = rag_answer(question)

    print("Question:")
    print(question)

    print("\nAnswer:")
    print(answer)

if __name__ == "__main__":
    main()