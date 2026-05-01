from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag.qa_engine import get_answer

app = FastAPI(title="Melositos Chatbot RAG")

# =========================
# 📦 REQUEST MODEL
# =========================
class Question(BaseModel):
    message: str


# =========================
# 🟢 HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/healthz")
def health():
    return {"status": "ok"}


# =========================
# 🤖 CHAT ENDPOINT (RAG)
# =========================
@app.post("/chat")
def chat(question: Question):

    try:
        # 🚀 llamada directa al RAG (sin prints para producción)
        response = get_answer(question.message)

        return {
            "response": response
        }

    except Exception as e:
        # 🧠 fallback seguro (evita 503 crash responses)
        return {
            "response": "Error interno del sistema RAG",
            "error": str(e)
        }