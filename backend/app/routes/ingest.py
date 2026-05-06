from fastapi import APIRouter, Query

from app.schemas import IngestResponse
from app.services.ingest_service import ingest_documents, reset_vector_store

router = APIRouter(prefix="/ingest", tags=["Ingest"])


@router.post("", response_model=IngestResponse)
def ingest(reset: bool = Query(default=False)):
    if reset:
        reset_vector_store()

    documents_loaded = ingest_documents()

    if documents_loaded == 0:
        return IngestResponse(
            status="empty",
            documents_loaded=0,
            message="No documents found. Add .md, .txt, .pdf or .docx files to the data folder."
        )

    return IngestResponse(
        status="success",
        documents_loaded=documents_loaded,
        message="Documents ingested successfully."
    )


@router.delete("/reset")
def reset_ingestion():
    reset_vector_store()

    return {
        "status": "success",
        "message": "Vector store reset successfully."
    }