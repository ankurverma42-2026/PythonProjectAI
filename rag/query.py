#search and ask LLM
import chromadbdir
from sentence_transformers import SentenceTransformer

from rag.ingest import CHROMADB_DIR

CHROMADB_DIR = 'chromadbdir/'
COLLECTION_NAME = 'car_collection'

def search_vector_db(questions,top_n=3):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    questions_embeddings = model.encode(questions).tolist()
    chroma_client = chromadbdir.PersistentClient(CHROMADB_DIR)
    collection = chroma_client.get_collection(COLLECTION_NAME)
    results = collection.query(query_embeddings=[questions_embeddings],n_results=top_n)
    return results

def build_context(results):
    documents=results["documents"][0]
    metadata=results["metadatas"][0]
    context_parts=[]
    for doc, meta in zip(documents, metadata):
        context_parts.append(f"Source: {meta['source']}\n Content: {doc}")
    return "\n\n".join(context_parts)





