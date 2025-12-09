from dotenv import load_dotenv
import os
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from ollama import Client

load_dotenv()

ollama = Client()

# Vector Embeddings
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    collection_name="learning_rag",
)

# Take user input
user_query = input("Enter your question: ")

# Perform similarity search
search_results = vector_db.similarity_search(query = user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
for result in search_results])

SYSTEM_PROMPT = f"""
You are a helpfull AI Assistant who answeres user query based on the available
context retrieved from a PDF file along with page_contents and page number.

You should only ans the user based on the following context and navigate the
user to open the right page number to know more.

Context:
{context}
"""
response = ollama.chat(
    model="llama3.2",     # or "llama3", "mistral", etc.
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": user_query }
    ]
)

print(response["message"]["content"])