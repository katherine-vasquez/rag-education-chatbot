# 🏗️ Arquitectura del Sistema

## Descripción General

El sistema está basado en una arquitectura tipo microservicios ligera desplegada en la nube.

## Componentes

- Cliente (Swagger UI / Frontend futuro)
- API Backend (FastAPI)
- Motor RAG (qa_engine)
- Base de datos vectorial (ChromaDB)
- Infraestructura en la nube (Google Cloud Run)

## Flujo de la solicitud

1. El usuario envía una pregunta al endpoint `/chat`
2. FastAPI recibe la solicitud
3. El sistema evalúa:
   - lógica directa (precios, servicios)
   - o consulta RAG
4. RAG busca en ChromaDB
5. Se selecciona el mejor fragmento
6. Se devuelve la respuesta al usuario

## Diagrama (texto)

Usuario  
↓  
FastAPI (/chat)  
↓  
qa_engine  
↓  
vector_db (ChromaDB)  
↓  
Respuesta  

## Tipo de arquitectura

- Microservicio serverless
- RAG (Retrieval-Augmented Generation)
- API REST