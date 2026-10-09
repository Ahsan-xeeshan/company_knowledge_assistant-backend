from services.vector_store import collection


def retrieve_documents(question:str, top_k:int=3):
    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )

    documents = results['documents'][0]

    metadatas = results['metadatas'][0]

    return documents,metadatas