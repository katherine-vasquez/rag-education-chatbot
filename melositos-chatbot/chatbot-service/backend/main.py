from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag.qa_engine import get_answer

app = FastAPI(title="Melositos Chatbot RAG")

class Question(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/chat")
def chat(question: Question):
    response = get_answer(question.message)
    return {"response": response}