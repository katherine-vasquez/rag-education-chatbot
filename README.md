# 📘 Melositos Chatbot RAG

Sistema de chatbot inteligente basado en documentos institucionales del jardín infantil Melositos.

---

## 🚀 Tecnologías utilizadas

- FastAPI
- ChromaDB
- Sentence Transformers
- Python
- Google Cloud Run
- Docker
- GitHub Actions (CI/CD)

---

## 🧠 Descripción

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) que permite realizar consultas en lenguaje natural sobre documentos institucionales.

El sistema:

- Carga documentos PDF
- Los divide en fragmentos (chunks)
- Genera embeddings semánticos
- Almacena la información en una base vectorial
- Responde preguntas basadas en el contexto más relevante

---

## 🧠 Machine Learning y Deep Learning

El sistema utiliza modelos de **Sentence Transformers**, basados en redes neuronales (Deep Learning), para generar embeddings semánticos de los documentos.

Esto permite realizar búsquedas inteligentes y contextualizadas dentro de la base de conocimiento.

---

## 🏗️ Arquitectura del Sistema

### 🔄 Flujo general

```text
Usuario
   ↓
POST /chat (FastAPI)
   ↓
qa_engine (lógica RAG)
   ↓
vector_db (ChromaDB)
   ↓
Embeddings + búsqueda semántica
   ↓
Respuesta generada
   ↓
Usuario
📌 Explicación
El usuario envía una pregunta al endpoint /chat.
FastAPI recibe la solicitud.
La pregunta se envía al motor RAG (qa_engine).
El sistema consulta la base vectorial (ChromaDB).
Se realiza una búsqueda semántica usando embeddings.
Se selecciona el fragmento más relevante.
Se construye la respuesta final y se devuelve al usuario.
🧩 Componentes
📄 Ingesta de documentos: carga y fragmentación de PDFs
🧠 qa_engine: lógica de interpretación y respuesta
🔎 vector_db: búsqueda semántica con embeddings
🌐 FastAPI: API REST
⚠️ Nota sobre microservicios

El repositorio incluye múltiples servicios (inventory, order, shipment, etc.) como parte de una arquitectura escalable futura.

Actualmente, el flujo activo corresponde únicamente al chatbot RAG.

⚙️ Instalación
pip install -r requirements.txt
📥 Cargar documentos
python backend/load_pdfs.py
▶️ Ejecutar el servidor
uvicorn backend.main:app --reload --port 5000
🌐 Uso

Abrir en el navegador:

http://127.0.0.1:5000/docs
🔌 Endpoints
GET /
{
  "status": "ok"
}
POST /chat
Request:
{
  "message": "¿Cuánto cuesta la matrícula de párvulos?"
}
Response:
{
  "response": "La matrícula de párvulos es $580.000"
}
☁️ Despliegue

El sistema está desplegado en Google Cloud Run:

👉 https://rag-education-chatbot-272872704725.europe-west1.run.app

☸️ Kubernetes

Configuración básica incluida en:

k8s/

Incluye:

Deployment
Service
🔄 CI/CD

El proyecto usa GitHub Actions para despliegue automático:

.github/workflows/deploy.yml
📄 Documentación

Disponible en:

docs/

Incluye:

Historias de usuario
Endpoints
Arquitectura
Despliegue
Kubernetes
📌 Autor

Proyecto académico - Inteligencia Artificial
Jesus Martinez Izurieta
Katherine Vasquez
Andrea Perdomo