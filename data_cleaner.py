# constitution_cleaner.py

from langchain_community.document_loaders import PyPDFLoader
import ftfy
import re
from langchain_core.documents import Document

def load_and_clean_constitution():
    """
    Loads the constitution PDF, fixes Unicode + broken lines,
    and returns cleaned LangChain Document objects.
    """
    pdf_path="Data/Nepalko Sambidhan 2072 नेपालको संविधान २०७२.pdf"
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()  

    cleaned_documents = []

    for doc in documents:
        text = doc.page_content

        
        text = ftfy.fix_text(text)

        
        text = re.sub(r'(?<!।)\n', ' ', text)   
        text = re.sub(r'\n{2,}', '\n\n', text)  
        text = re.sub(r'\s+', ' ', text).strip()

        doc.page_content = text
        cleaned_documents.append(doc)

    return cleaned_documents

if __name__ == "__main__":
    cleaned_docs = load_and_clean_constitution()
    for i, doc in enumerate(cleaned_docs[:3], 1):
        print(f"\n--- Cleaned Document {i} ---")
        print(doc.page_content[:800])
        print("Metadata:", doc.metadata)