from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from app.config import settings


def configure_embeddings() -> None:
    """
    Configures a local Hugging Face embedding model.
    This avoids requiring an OpenAI API key for embeddings.
    """
    print(f"Using embedding model: {settings.EMBEDDING_MODEL}")

    Settings.embed_model = HuggingFaceEmbedding(
        model_name=settings.EMBEDDING_MODEL
    )


def ingest_documents() -> None:
    """
    Loads documents from the data directory and creates a local vector index.
    """
    configure_embeddings()

    print(f"Loading documents from: {settings.DATA_DIR}")

    documents = SimpleDirectoryReader(settings.DATA_DIR).load_data()

    if not documents:
        print("No documents found. Add files to the data/ folder first.")
        return

    print(f"Loaded {len(documents)} document(s). Creating index...")

    index = VectorStoreIndex.from_documents(documents)

    index.storage_context.persist(persist_dir=settings.STORAGE_DIR)

    print(f"Index created and saved in: {settings.STORAGE_DIR}")


if __name__ == "__main__":
    ingest_documents()