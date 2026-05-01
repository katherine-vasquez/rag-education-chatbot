📘 Melositos Chatbot RAG

Sistema de chatbot inteligente basado en documentos PDF del jardín infantil Melositos.

🚀 Tecnologías utilizadas
FastAPI
ChromaDB
Sentence Transformers
Python
🧠 Descripción

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) que permite realizar consultas en lenguaje natural sobre documentos institucionales.

El sistema:

Carga documentos PDF
Los divide en fragmentos (chunks)
Genera embeddings
Almacena la información en una base vectorial
Responde preguntas basadas en contexto relevante
⚙️ Instalación
pip install -r requirements.txt
📥 Cargar documentos
python backend/load_pdfs.py
▶️ Ejecutar el servidor
uvicorn backend.main:app --reload --port 5000
🌐 Uso

Abrir en el navegador:

http://127.0.0.1:5000/docs
🤖 Endpoint principal

POST /chat

Ejemplo:

{
  "message": "¿Cuánto cuesta la matrícula?"
}
🧩 Arquitectura

El sistema sigue una arquitectura modular con componentes de procesamiento de documentos, base vectorial y API REST.

Ver historias de usuario en /docs/historias_usuario.md

📌 Autor

Proyecto académico - Inteligencia Artificial