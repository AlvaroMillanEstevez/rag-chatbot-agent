from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    question: str


class SourceNode(BaseModel):
    file_name: Optional[str] = None
    page_label: Optional[str] = None
    score: Optional[float] = None
    text: Optional[str] = None


class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceNode] = []


class IngestResponse(BaseModel):
    status: str
    documents_loaded: int
    message: str