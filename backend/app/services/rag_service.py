import chromadb

from llama_index.core import VectorStoreIndex, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore

from app.config import settings
from app.schemas import SourceNode


SYSTEM_PROMPT = """
You are a helpful AI assistant for a website or internal documentation system.

Rules:
- Answer only using the provided context.
- If the information is not in the documents, say that you do not have enough information.
- Be clear, concise and practical.
- Always answer in the same language as the user's question when possible.
"""


def configure_llama_index() -> None:
    Settings.embed_model = HuggingFaceEmbedding(
        model_name=settings.EMBEDDING_MODEL
    )

    Settings.llm = Ollama(
        model=settings.OLLAMA_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
        request_timeout=120.0,
        system_prompt=SYSTEM_PROMPT
    )


def get_index() -> VectorStoreIndex:
    configure_llama_index()

    chroma_client = chromadb.PersistentClient(
        path=f"{settings.STORAGE_DIR}/chroma"
    )

    chroma_collection = chroma_client.get_or_create_collection(
        settings.CHROMA_COLLECTION
    )

    vector_store = ChromaVectorStore(
        chroma_collection=chroma_collection
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    return VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context
    )


def ask_question(question: str):
    index = get_index()

    query_engine = index.as_query_engine(
        similarity_top_k=settings.SIMILARITY_TOP_K
    )

    response = query_engine.query(question)

    sources = []

    for source_node in response.source_nodes:
        metadata = source_node.node.metadata or {}

        sources.append(
            SourceNode(
                file_name=metadata.get("file_name"),
                page_label=metadata.get("page_label"),
                score=source_node.score,
                text=source_node.node.get_content()[:500]
            )
        )

    return str(response), sources