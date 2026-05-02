import sys
import os

# 🔥 agregar ruta del backend
sys.path.append(os.path.abspath("chatbot-service"))

from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_chat():
    response = client.post("/chat", json={"message": "¿Qué es el programa RIE?"})
    assert response.status_code == 200
    assert "response" in response.json()