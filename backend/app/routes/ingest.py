from fastapi import APIRouter

from app.schemas import IngestResponse
from app.services.ingest_service import ingest_documents

router = APIRouter(prefix="/ingest", tags=["Ingest"])


@router.post("", response_model=IngestResponse)
def ingest():
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