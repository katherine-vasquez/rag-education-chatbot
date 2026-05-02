# ☁️ Despliegue en la Nube

## 🧠 Descripción general

El sistema está desplegado en Google Cloud Run, permitiendo escalabilidad automática y alta disponibilidad.

---

## 🧩 Componentes

- Cloud Run → API FastAPI
- GitHub → Control de versiones
- GitHub Actions → CI/CD
- ChromaDB → Base vectorial

---

## 🔄 Flujo de despliegue

```text
Developer (git push)
        ↓
GitHub Repository
        ↓
GitHub Actions (CI/CD)
        ↓
Google Cloud Run (deploy automático)
        ↓
Usuario final (consume API)