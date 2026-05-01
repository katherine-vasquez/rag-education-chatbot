import os
from rag.pdf_loader import load_pdf, split_text
from rag.vector_db import add_chunks


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.join(BASE_DIR, "data", "pdfs")

all_chunks = []

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        path = os.path.join(pdf_folder, file)

        print(f"Cargando: {file}")

        text = load_pdf(path)
        chunks = split_text(text)

        all_chunks.extend(chunks)

add_chunks(all_chunks)

print("TODOS los PDFs fueron cargados en ChromaDB")