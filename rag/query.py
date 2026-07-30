#search and ask LLM
import chromadb
from chromadb.experimental.density_relevance import chroma_client
from sentence_transformers import SentenceTransformer

from rag.ingest import CHROMADB_DIR

CHROMADB_DIR = './chromadb/'
COLLECTION_NAME = 'car_collection'

def search_vector_db(questions,top_n=3):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    questions_embeddings = model.encode(questions).tolist()
    chroma_client = chromadb.PersistentClient(CHROMADB_DIR)
    collection = chroma_client.get_collection(COLLECTION_NAME)
    results = collection.query(query_embeddings=[questions_embeddings],n_results=top_n)
    return results


