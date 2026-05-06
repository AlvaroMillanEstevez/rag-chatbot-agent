from fastapi import APIRouter, HTTPException

from app.schemas import ChatRequest, ChatResponse
from app.services.rag_service import ask_question

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    try:
        answer, sources = ask_question(request.question)

        return ChatResponse(
            answer=answer,
            sources=sources
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Chat service error: {str(error)}"
        )