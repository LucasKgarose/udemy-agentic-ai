from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
from summarize import summarize_document

load_dotenv()

pdf_path = Path(__file__).parent / "sample.pdf"

# Load the PDF document
loader = PyPDFLoader(str(pdf_path))
pages = loader.load()

# print(f"Loaded {len(pages)} pages from the PDF document.")
# print("First page content preview:")
# print(pages[50].page_content[:500])  # Print first 500 characters of the first page

# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(pages)

print(f"Created {len(chunks)} chunks from the document.")

# Summarize the entire document after chunking
document_summary = summarize_document(chunks)

# Vector Embeddings
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Connect to Qdrant and create a vector store
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("indexing of documents completed...")