import os
from openai import OpenAI
from dotenv import load_dotenv

from query import search_vector_db, build_context
import ollama

# Read the OpenAI API key from the environment.
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Initialize the OpenAI client.
client = OpenAI(api_key=API_KEY)

def ask_openai(question, context):
   #Using Ollama
   response = ollama.chat(
       model="llama3.2",
       messages=[
           {
               "role": "system",
               "content": """
   You are a helpful assistant.

   Rules:
   - Answer only using the provided context.
   - Do not use outside knowledge.
   - If the answer is not present in the context, say:
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
       ],
       options={
           "temperature": 0.5
       }
   )
   answer = response["message"]["content"]
   if not answer:
       return "No response generated."

   return answer

def rag_answer(question):
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