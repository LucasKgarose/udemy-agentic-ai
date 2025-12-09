from rag.qdrant_client import qdrant_client

def main():
    collections = qdrant_client.get_collections()
    print("Available Collections:", collections)