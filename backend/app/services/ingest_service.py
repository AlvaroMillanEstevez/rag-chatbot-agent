import chromadb

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from app.config import settings


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