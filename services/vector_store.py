import chromadb

from services.document_loader import load_documents


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name = "company_knowledge"
)

def add_documents():
    documents = load_documents()

    if not documents:
        return 0;

    existing = collection.get()

    existing_ids = set(existing["ids"])

    new_documents = []

    for document in documents:
        if document["id"] not in existing_ids:
            new_documents.append(document)


    if not new_documents:
        return 0

    collection.add(
        ids=[
            document["id"]
            for document in new_documents
        ],
        documents=[
            document["text"]
            for document in new_documents
        ],
        metadatas=[
            {
                "source": document["source"]
            }
            for document in new_documents
        ]
    )
    return len(new_documents)