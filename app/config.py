import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # LLM provider
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "mock")

    # DeepSeek config
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_BASE_URL: str = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    DEEPSEEK_MODEL: str = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    # Embeddings
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    # Project paths
    DATA_DIR: str = "data"
    STORAGE_DIR: str = "storage"


settings = Settings()