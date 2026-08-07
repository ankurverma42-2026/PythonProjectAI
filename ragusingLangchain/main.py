import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def main():
    llm = OllamaLLM(model="llama3.2")
    result = llm.invoke("What is RAG")

    print(result)



if __name__ == "__main__":
    main()