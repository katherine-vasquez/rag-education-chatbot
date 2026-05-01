import chromadb
import re
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="melositos",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction()
)


def add_chunks(chunks):
    for i, chunk in enumerate(chunks):

        # 🔥 evitar basura
        if len(chunk.strip()) < 20:
            continue

        collection.add(
            documents=[chunk],
            ids=[f"chunk_{i}"]
        )


def search(query):

    # 🚀 BOOST de consulta (MUY IMPORTANTE)
    boosted_query = query + " fechas matricula 02 de julio 03 de julio"

    results = collection.query(
        query_texts=[boosted_query],
        n_results=20
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
        # 📅 PRIORIDAD FECHAS (MÁXIMA)
        # =========================
        if is_date_question:

            if "02 de julio" in d:
                score += 2000

            if "03 de julio" in d:
                score += 2000

            # ❌ penalizar precios en preguntas de fechas
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
        # 📉 PENALIZAR TEXTO MUY GRANDE
        # =========================
        if len(doc) > 1200:
            score -= 50

        scored.append((score, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [doc for _, doc in scored[:3]]