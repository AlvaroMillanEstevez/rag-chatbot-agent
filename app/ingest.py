from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext
from app.config import settings


def ingest_documents() -> None:
    """
    Loads documents from the data directory and creates a local vector index.
    """
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
