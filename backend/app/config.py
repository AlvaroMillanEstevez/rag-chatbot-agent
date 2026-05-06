import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")

    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    DATA_DIR: str = os.getenv("DATA_DIR", "backend/data")
    STORAGE_DIR: str = os.getenv("STORAGE_DIR", "backend/storage")
    CHROMA_COLLECTION: str = os.getenv("CHROMA_COLLECTION", "rag_documents")

    SIMILARITY_TOP_K: int = int(os.getenv("SIMILARITY_TOP_K", "4"))

    SOURCE_SCORE_THRESHOLD: float = float(os.getenv("SOURCE_SCORE_THRESHOLD", "0.35"))


settings = Settings()