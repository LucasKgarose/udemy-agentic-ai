# Udemy Agentic AI - RAG System with LangChain

A Retrieval-Augmented Generation (RAG) system built with LangChain, Qdrant vector database, and Ollama for local LLM inference. This project enables semantic search and question-answering over PDF documents.

## What This Project Does

This is a complete RAG (Retrieval-Augmented Generation) pipeline that:

1. **Ingests PDF Documents** - Loads and processes PDF files
2. **Chunks Text** - Splits documents into manageable pieces with overlap for context preservation
3. **Generates Embeddings** - Creates vector embeddings using Ollama's `nomic-embed-text` model
4. **Stores in Vector Database** - Indexes embeddings in Qdrant for efficient similarity search
5. **Enables Semantic Search** - Allows users to query documents using natural language
6. **Generates Contextual Answers** - Uses Llama 3.2 (via Ollama) to answer questions based on retrieved context

## Architecture

### Components

- **LangChain**: Framework for building LLM applications
    - `langchain-community`: Document loaders (PyPDF)
    - `langchain-qdrant`: Qdrant vector store integration
    - `langchain-text-splitters`: Text chunking utilities
    - `langchain-ollama`: Ollama embeddings and LLM integration

- **Qdrant**: Vector database for storing and searching document embeddings
    - Cloud-hosted instance
    - Handles similarity search with high performance

- **Ollama**: Local LLM runtime
    - `nomic-embed-text`: Embedding model for vector generation
    - `llama3.2`: Language model for generating answers

- **Python Libraries**:
    - `pypdf`: PDF parsing
    - `python-dotenv`: Environment variable management
    - `qdrant-client`: Direct Qdrant API access

## Project Structure

```
udemy-agentic-ai/
├── rag/
│   ├── index.py              # Document indexing pipeline
│   ├── chat.py               # Interactive query interface
│   ├── qdrant_connection.py  # Database connection utilities
│   └── sample.pdf            # Source document
├── app.py                    # Main application entry point
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables (not in repo)
```

## Setup Instructions

### Prerequisites

1. **Python 3.13+** installed
2. **Ollama** installed and running ([ollama.com](https://ollama.com))
3. **Qdrant Cloud** account or local instance

### Installation

1. **Clone the repository**
     ```bash
     git clone https://github.com/LucasKgarose/udemy-agentic-ai.git
     cd udemy-agentic-ai
     ```

2. **Create virtual environment**
     ```bash
     python -m venv venv
     
     # Windows (Git Bash)
     source venv/Scripts/activate
     
     # Linux/Mac
     source venv/bin/activate
     ```

3. **Install dependencies**
     ```bash
     pip install -r requirements.txt
     ```

4. **Pull Ollama models**
     ```bash
     ollama pull nomic-embed-text
     ollama pull llama3.2
     ```

5. **Configure environment variables**
     
     Create a `.env` file in the project root:
     ```env
     QDRANT_URL=https://your-qdrant-instance.qdrant.io
     QDRANT_API_KEY=your_api_key_here
     QDRANT_PORT=6333
     ```

## Usage

### 1. Index Documents

Process and store PDF documents in the vector database:

```bash
python rag/index.py
```

This will:
- Load `rag/sample.pdf`
- Split into 1000-character chunks with 200-character overlap
- Generate embeddings using `nomic-embed-text`
- Store in Qdrant collection `learning_rag`

### 2. Query Documents

Ask questions about your documents:

```bash
python rag/chat.py
```

The system will:
- Prompt for your question
- Perform similarity search in Qdrant
- Retrieve relevant document chunks
- Generate an answer using Llama 3.2 with context
- Provide page numbers for further reference

### 3. Test Database Connection

Verify Qdrant connectivity:

```bash
python app.py
```

## How It Works

### Indexing Pipeline (`rag/index.py`)

1. **Document Loading**: PyPDFLoader reads the PDF file
2. **Text Splitting**: RecursiveCharacterTextSplitter breaks text into chunks
3. **Embedding Generation**: Ollama creates vector embeddings for each chunk
4. **Vector Storage**: QdrantVectorStore indexes embeddings with metadata

### Query Pipeline (`rag/chat.py`)

1. **User Input**: Accepts natural language question
2. **Vector Search**: Finds similar document chunks in Qdrant
3. **Context Assembly**: Combines relevant chunks with metadata
4. **LLM Prompting**: Sends context and question to Llama 3.2
5. **Answer Generation**: Returns contextual answer with page references

## Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| langchain | 1.1.3 | Core framework |
| langchain-community | 0.4.1 | PDF loader |
| langchain-qdrant | 1.1.0 | Vector store |
| langchain-ollama | 1.0.0 | Embeddings & LLM |
| qdrant-client | 1.16.1 | Vector database client |
| ollama | 0.6.1 | Ollama Python client |
| pypdf | 6.4.1 | PDF parsing |
| python-dotenv | 1.2.1 | Environment config |

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'pypdf'`
- **Solution**: `pip install pypdf`

**Issue**: `ImportError: cannot import name 'QdrantClient' from 'qdrant_client'`
- **Solution**: File naming conflict. Ensure no local file is named `qdrant_client.py`

**Issue**: `bash: ollama: command not found`
- **Solution**: Install Ollama from [ollama.com](https://ollama.com) and restart terminal

**Issue**: Dependency conflicts with `langchain-core`
- **Solution**: Upgrade all LangChain packages to latest versions compatible with `langchain-core>=1.1.0`

**Issue**: `sed: command not found` on Windows Git Bash
- **Solution**: Add Git utilities to PATH: `export PATH="/c/Program Files/Git/usr/bin:$PATH"`

## Development Notes

- Uses Python 3.13.5
- Virtual environment recommended to avoid dependency conflicts
- Qdrant cloud instance for production, local Docker instance for development
- Ollama runs models locally for privacy and cost efficiency

## Future Enhancements

- [ ] Support for multiple document formats (DOCX, TXT, Markdown)
- [ ] Web interface with Streamlit or Gradio
- [ ] Conversation history tracking
- [ ] Multi-collection support
- [ ] Advanced retrieval strategies (hybrid search, re-ranking)
- [ ] OpenAI embeddings as alternative to Ollama

## Acknowledgments

This project was built as part of [Hitesh Choudhary's Complete AI & LLM Engineering Bootcamp](https://www.udemy.com/course/full-stack-ai-with-python/).

## Author

Lucas Kgarose - [GitHub](https://github.com/LucasKgarose)