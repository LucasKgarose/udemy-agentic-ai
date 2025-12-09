from rag.qdrant_connection import qdrant_client

def main():
    collections = qdrant_client.get_collections()
    print("Available Collections:", collections)