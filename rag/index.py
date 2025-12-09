from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "sample.pdf"

loader = PyPDFLoader(str(pdf_path))
pages = loader.load()

print(f"Loaded {len(pages)} pages from the PDF document.")
print("First page content preview:")
print(pages[50].page_content[:500])  # Print first 500 characters of the first page