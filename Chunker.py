# constitution_chunker.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from data_cleaner import load_and_clean_constitution
from langchain_core.documents import Document

def create_rag_chunks():
    """
    Splits cleaned constitution documents into Nepali-aware chunks
    suitable for FAISS + RAG.
    """
    pdf_path = "Data/Nepalko Sambidhan 2072 नेपालको संविधान २०७२.pdf"

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "।", "\n"],
        chunk_size=800,
        chunk_overlap=100
    )

    cleaned_documents = load_and_clean_constitution()
    all_chunks = []

    for doc in cleaned_documents:
        chunks = text_splitter.split_text(doc.page_content)

        for i, chunk in enumerate(chunks):
            all_chunks.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "source": pdf_path,
                        "page": doc.metadata.get("page_label"),
                        "chunk_index": i
                    }
                )
            )

    return all_chunks


# if __name__ == "__main__":
#     chunks = create_rag_chunks()
#     for i, doc in enumerate(chunks[:5], 1):
#         print(f"\n--- Chunk {i} ---")
#         print(doc.page_content[:800])
#         print("Metadata:", doc.metadata)