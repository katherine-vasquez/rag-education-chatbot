from PyPDF2 import PdfReader
import re


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            # limpieza básica
            page_text = page_text.replace("\n", " ")
            page_text = " ".join(page_text.split())

            text += page_text + " "

    return text


# 🚀 CHUNKING INTELIGENTE (VERSIÓN FINAL CORREGIDA)
def split_text(text):
    """
    Divide el PDF en bloques más coherentes para mejorar RAG.
    Evita mezclar fechas, precios y RIE en el mismo chunk.
    """

    # 🔥 normalizar texto primero
    text = text.replace("•", "\n•")
    text = re.sub(r"\s+", " ", text)

    # 🔥 separadores clave del documento
    separators = [
        "FECHAS DE MATRICULAS",
        "GRADO",
        "SERVICIO",
        "IMPORTANTE",
        "A QUIEN PUEDA INTERESAR",
        "•"
    ]

    chunks = [text]

    # 🔥 dividir por secciones
    for sep in separators:
        new_chunks = []

        for c in chunks:
            parts = c.split(sep)

            for p in parts:
                clean = " ".join(p.split())

                # evitar basura muy corta
                if len(clean) > 40:
                    new_chunks.append(clean)

        chunks = new_chunks

    # 🔥 limpieza final + evitar chunks gigantes
    final_chunks = []

    for c in chunks:
        if len(c) > 800:
            # dividir chunks grandes
            subparts = [c[i:i+800] for i in range(0, len(c), 600)]
            final_chunks.extend(subparts)
        else:
            final_chunks.append(c)

    return final_chunks