# ☸️ Kubernetes

## 🧠 Descripción

Se incluye una configuración básica de Kubernetes para desplegar el sistema RAG en un entorno contenerizado.

## 📦 Componentes

- Deployment → Maneja los pods del backend
- Service → Expone el servicio al exterior

## 🚀 Funcionamiento

1. Se crea un Deployment con la imagen del chatbot.
2. Kubernetes levanta los pods necesarios.
3. El Service permite acceder al contenedor.

## 📌 Ventajas

- Escalabilidad horizontal
- Alta disponibilidad
- Gestión de contenedores automatizada