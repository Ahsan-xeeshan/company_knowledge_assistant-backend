from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.rag import RAGRequest,RAGResponse
from services.vector_store import add_documents
from services.retrieval import retrieve_documents
from services.llm import generate_answer


app = FastAPI(
    title="Company Knowledge Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message" : "Company Knowledge Assistant API"
    }

@app.post("/api/rag/ask",response_model=RAGResponse)
def ask_question(data: RAGRequest):
    
    documents, metadatas = retrieve_documents(
        data.question,
        top_k=3
    )

    context = "\n\n".join(documents)

    answer = generate_answer(
        data.question,
        context
    )

    sources = list({
        metadata["source"]
        for metadata in metadatas
    })

    return {
        "answer" : answer,
        "sources": sources
    }


