import chromadb
import re
import os
import threading
from chromadb.utils import embedding_functions

# =========================
# 🚀 CONFIG SEGURA CLOUD RUN
# =========================

DB_PATH = os.path.join(os.getcwd(), "chroma_db")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name="melositos",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction()
)

# 🔒 lock para evitar problemas en concurrencia
_lock = threading.Lock()

# =========================
# 📥 INGESTA CHUNKS
# =========================

def add_chunks(chunks):
    with _lock:
        for i, chunk in enumerate(chunks):

            # 🚫 evitar basura
            if len(chunk.strip()) < 20:
                continue

            collection.add(
                documents=[chunk],
                ids=[f"chunk_{i}"]
            )

# =========================
# 🔍 SEARCH OPTIMIZADO
# =========================

def search(query):

    # 🚀 boost ligero (optimizado, no pesado)
    boosted_query = f"{query} matricula fechas calendario"

    results = collection.query(
        query_texts=[boosted_query],
        n_results=5   # 🔥 reducido para evitar 503
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        return []

    def normalize(text):
        return text.lower() \
            .replace("á", "a") \
            .replace("é", "e") \
            .replace("í", "i") \
            .replace("ó", "o") \
            .replace("ú", "u")

    q = normalize(query.lower())

    # 🧠 detectar intención de fecha
    is_date_question = (
        "fecha" in q or
        "fechas" in q or
        "cuando" in q or
        "horario" in q or
        "matricula" in q
    )

    scored = []

    for doc in docs:
        d = normalize(doc)

        score = 0

        # =========================
        # 📅 PRIORIDAD FECHAS
        # =========================
        if is_date_question:

            if "02 de julio" in d:
                score += 2000

            if "03 de julio" in d:
                score += 2000

            # ❌ penalizar precios en fechas
            if "$" in d:
                score -= 500

        # =========================
        # 🎯 GRADOS
        # =========================
        if "transicion" in q and "transicion" in d:
            score += 120

        if "parvulos" in q and "parvulos" in d:
            score += 120

        if "jardin" in q and "jardin" in d:
            score += 120

        # =========================
        # 💰 VALORES EXACTOS
        # =========================
        if "transicion" in q and "507.957" in d:
            score += 300

        if "parvulos" in q and "580.000" in d:
            score += 300

        if "jardin" in q and "524.273" in d:
            score += 300

        if "pension" in q and "377.000" in d:
            score += 200

        # =========================
        # 📉 PENALIZAR TEXTOS GRANDES
        # =========================
        if len(doc) > 1200:
            score -= 50

        scored.append((score, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [doc for _, doc in scored[:3]]