from ollama import Client
from typing import List
from langchain_core.documents import Document

def summarize_chunk(ollama: Client, chunk_content: str, chunk_index: int) -> str:
    """
    Summarize a single chunk of the document.
    
    Args:
        ollama: Ollama client instance
        chunk_content: Content of the chunk to summarize
        chunk_index: Index of the chunk for tracking
        
    Returns:
        str: Summary of the chunk
    """
    CHUNK_SUMMARIZATION_PROMPT = """
Provide a concise summary of the following text chunk. Focus on key information, main points, and important details:

{chunk_content}
"""
    
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": CHUNK_SUMMARIZATION_PROMPT.format(chunk_content=chunk_content)
            }
        ]
    )
    
    return response["message"]["content"]


def summarize_document(chunks: List[Document]) -> str:
    """
    Summarize the entire document using a two-stage approach:
    1. Summarize each chunk individually
    2. Summarize all chunk summaries into a final comprehensive summary
    
    Args:
        chunks: List of document chunks
        
    Returns:
        str: The final comprehensive summary
    """
    ollama = Client()
    
    print(f"\nStep 1: Summarizing {len(chunks)} individual chunks...")
    chunk_summaries = []
    
    for i, chunk in enumerate(chunks):
        print(f"  Summarizing chunk {i+1}/{len(chunks)}...", end="\r")
        chunk_summary = summarize_chunk(ollama, chunk.page_content, i)
        chunk_summaries.append(chunk_summary)
    
    print(f"\n✓ Completed summarizing all {len(chunks)} chunks")
    
    # Combine all chunk summaries
    print("\nStep 2: Creating final summary from chunk summaries...")
    combined_summaries = "\n\n".join([f"Chunk {i+1} Summary:\n{summary}" 
                                      for i, summary in enumerate(chunk_summaries)])
    
    FINAL_SUMMARIZATION_PROMPT = """
Based on the following summaries of different sections of a document, provide a comprehensive final summary. Include:
1. Main topics and themes across the entire document
2. Key points and important information
3. Overall structure and organization
4. Any patterns or connections between sections

Section Summaries:
{combined_summaries}
"""
    
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": FINAL_SUMMARIZATION_PROMPT.format(combined_summaries=combined_summaries)
            }
        ]
    )
    
    final_summary = response["message"]["content"]
    print("\n" + "="*80)
    print("FINAL DOCUMENT SUMMARY")
    print("="*80)
    print(final_summary)
    print("="*80 + "\n")
    
    return final_summary
