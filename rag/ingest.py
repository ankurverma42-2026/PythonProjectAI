#load Doc
from fileinput import filename

from sentence_transformers import SentenceTransformer
import chromadb
import os

#Load embedding model
DOCS_DIR = './docs/'
CHROMADB_DIR = './chromadb/'
COLLECTION_NAME = 'car_collection'
COLLECTION_PATH = DOCS_DIR + COLLECTION_NAME

def load_text_files():
    documents = []
    for file_name in os.listdir(DOCS_DIR):
        if file_name.endswith(".txt"):
            full_path = os.path.join(DOCS_DIR,file_name)
            with open(full_path, 'r',encoding="utf-8") as f:
                text = f.read()
                documents.append({"filename":file_name,"text":text})

    return documents

def chunk_text(text, chunk_size=500,overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end= start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end-overlap
    return chunks

def create_embeddings_store():
    documents = load_text_files()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chroma_client=chromadb.PersistentClient(path=CHROMADB_DIR)
    collection=chroma_client.get_or_create_collection(COLLECTION_NAME)
    chunk_id=1
    for doc in documents:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            embedding = model.encode(chunk, convert_to_tensor=True).tolist()
            collection.add(ids=str(chunk_id), embeddings=[embedding], documents=[chunk],metadatas=[{"source": doc["filename"]}])
            chunk_id += 1
    print("Ingestion Completed")
    print(f"Saving Embeddings {len(documents)}")
    print(f"Chunks stored: {chunk_id -1}")

