from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

FAISS_PATH = "faiss_budget_index3"


def load_vector_store():

    embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base",
    encode_kwargs={"normalize_embeddings": True}
)

    vector_store = FAISS.load_local(
        FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store


def search_constitution(query, k=5):
    vector_store = load_vector_store()

    # retriever = vector_store.as_retriever(
    #     search_type="mmr",
    #     search_kwargs={
    #         "k": k,          # final documents returned
    #         "fetch_k": 20,   # initial candidates
    #         "lambda_mult": 0.6  # balance relevance/diversity
    #     }
    # )
    reteriver = vector_store.similarity_search(query, k=k)


    
    return reteriver


# if __name__ == "__main__":
#     query = "नेपालको नागरिकको मौलिक अधिकारहरू के-के छन्?"
#     docs = search_constitution(query, k=3)

#     for i, doc in enumerate(docs, 1):
#         print(f"\n--- Result {i} ---")
#         print(doc.page_content[:400])
#         print("Metadata:", doc.metadata)
