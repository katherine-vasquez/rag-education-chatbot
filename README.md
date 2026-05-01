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

## 🏗️ Arquitectura

El sistema está diseñado siguiendo principios de arquitectura de microservicios, donde cada componente cumple una responsabilidad específica:

- 📄 Servicio de Ingesta de Documentos (pdf_loader): procesa y divide los PDFs
- 🧠 Servicio de Procesamiento (qa_engine): interpreta la intención del usuario
- 🔎 Servicio de Búsqueda (vector_db): consulta la base vectorial (ChromaDB)
- 🌐 API Gateway (FastAPI): expone los endpoints al usuario

Aunque el sistema se despliega como una sola aplicación por simplicidad, los componentes están desacoplados y pueden escalarse como microservicios independientes en un entorno productivo.

Esta arquitectura permite:
- Escalabilidad
- Separación de responsabilidades
- Evolución hacia sistemas distribuidos (ej. Kafka, colas de eventos)

Ver historias de usuario en /docs/historias_usuario.md

📌 Autor

Proyecto académico - Inteligencia Artificial