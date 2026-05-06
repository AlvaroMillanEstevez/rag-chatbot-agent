import chromadb
import shutil

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from app.config import settings

from pathlib import Path


def configure_embeddings() -> None:
    Settings.embed_model = HuggingFaceEmbedding(
        model_name=settings.EMBEDDING_MODEL
    )


def get_chroma_vector_store() -> ChromaVectorStore:
    chroma_client = chromadb.PersistentClient(
        path=f"{settings.STORAGE_DIR}/chroma"
    )

    chroma_collection = chroma_client.get_or_create_collection(
        settings.CHROMA_COLLECTION
    )

    return ChromaVectorStore(
        chroma_collection=chroma_collection
    )


def ingest_documents() -> int:
    configure_embeddings()

    documents = SimpleDirectoryReader(
        input_dir=settings.DATA_DIR,
        recursive=True,
        required_exts=[".txt", ".md", ".pdf", ".docx"]
    ).load_data()

    if not documents:
        return 0

    vector_store = get_chroma_vector_store()

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        show_progress=True
    )

    return len(documents)

def reset_vector_store() -> None:
    """
    Deletes the local Chroma vector store so documents can be re-ingested from scratch.
    Useful during development when source documents change.
    """
    chroma_path = Path(settings.STORAGE_DIR) / "chroma"

    if chroma_path.exists():
        shutil.rmtree(chroma_path)