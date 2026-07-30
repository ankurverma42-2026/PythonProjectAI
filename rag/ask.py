from openai import OpenAI
import os

from query import search_vector_db, build_context


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)


def ask_openai(question, context):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """
You are a helpful assistant.
Answer only using the provided context.
If the answer is not in the context, say:
"I don't know based on the provided information."
"""
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{question}
"""
            }
        ]
    )

    return response.choices[0].message.content


def rag_answer(question):

    results = search_vector_db(question)

    context = build_context(results)

    print("\n--- Retrieved Context ---")
    print(context)
    print("-------------------------")

    return ask_openai(question, context)


if __name__ == "__main__":
    print(os.getenv("OPENAI_API_KEY"))
    question = "Which car has the best fuel economy?"

    answer = rag_answer(question)

    print("\nAnswer:")
    print(answer)