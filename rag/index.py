from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

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