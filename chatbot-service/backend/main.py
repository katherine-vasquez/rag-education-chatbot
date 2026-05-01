from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Melositos Chatbot RAG")

class Question(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/healthz")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(question: Question):
    try:
        from backend.rag.qa_engine import get_answer

        response = get_answer(question.message)

        return {"response": response}

    except Exception as e:
        return {
            "response": "Lo siento, el sistema RAG aún no está disponible.",
            "error": str(e)
        }