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
    # 🔥 SAFE MODE: desactivamos RAG para probar deploy
    return {
        "response": "test-ok"
    }