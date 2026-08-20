import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def main():
    llm = ChatOllama(model="llama3.2", temperature=0.1)


    #prompt = ChatPromptTemplate.from_template("Answer precisely. Langchain is ...")
    question="What is RAG?"
    prompt=ChatPromptTemplate.from_messages(
        [
            ("system","You are AI tutor. Respond in one sentence with precise information."),
            ("human",
             "Here are some examples: \n\n"
             "Question: What is RAG?"
             "Response: Good  question! RAG stands for Retrieval Augmented Generation"
             "Answer the questions starting with something like this:  "
             "Nice one or something that motive user to ask more questions"
             "Concept:\n\n {question}")
        ])
    # in lang chain, we wired from left instruction to right as below.
    chain=prompt | llm
  #  message = prompt.format_messages()
    #chain.invoke does everything including formatting prompt and then calling llm.
    result = chain.invoke({"question":question}).content

    print(result)



if __name__ == "__main__":
    main()