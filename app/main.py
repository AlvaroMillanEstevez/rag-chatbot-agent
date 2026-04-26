from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="RAG Chatbot Agent",
    description="API para chatbot RAG con LlamaIndex y DeepSeek",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "RAG Chatbot Agent API is running",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        answer=f"Has preguntado: {request.question}"
    )
