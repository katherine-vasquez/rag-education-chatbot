from fastapi import FastAPI
from pydantic import BaseModel

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
# 🤖 CHAT ENDPOINT (RAG SAFE PRODUCTION)
# =========================
@app.post("/chat")
def chat(question: Question):

    try:
        # 🔥 IMPORT LOCAL (evita problemas en startup Cloud Run)
        from backend.rag.qa_engine import get_answer

        return {
            "response": get_answer(question.message)
        }

    except Exception as e:
        print("ERROR:", str(e))

        # 🧠 fallback seguro (NUNCA rompe Cloud Run)
        return {
            "response": "Error interno del sistema RAG"
        }