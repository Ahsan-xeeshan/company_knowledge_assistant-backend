from services.vector_store import add_documents


count = add_documents()

print(
    f"{count} new documents chunks added to ChormaDB."
)