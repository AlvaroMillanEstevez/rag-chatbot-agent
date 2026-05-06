from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.ingest import router as ingest_router

from app.config import settings

app = FastAPI(
    title="RAG Chatbot Agent",
    description="Website AI Assistant using FastAPI, LlamaIndex, Ollama and Chroma",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(ingest_router)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "RAG Chatbot Agent API is running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "rag-chatbot-agent"
    }

@app.get("/info")
def project_info():
    return {
        "project": "RAG Chatbot Agent",
        "description": "AI Website Assistant using FastAPI, LlamaIndex, Ollama, Chroma and Vue",
        "features": [
            "Document ingestion",
            "Vector search",
            "Local LLM with Ollama",
            "RAG responses",
            "Source citations",
            "Vue chat interface"
        ],
        "llm_provider": settings.LLM_PROVIDER,
        "ollama_model": settings.OLLAMA_MODEL,
        "vector_database": "Chroma",
        "embedding_model": settings.EMBEDDING_MODEL
    }