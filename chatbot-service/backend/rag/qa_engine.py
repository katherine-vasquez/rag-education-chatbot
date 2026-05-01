from .vector_db import search


def get_answer(question):
    print("DEBUG QUESTION:", question)
    q = question.lower()

    # =========================
    # 🧠 PDF 1 - COLEGIO (GRADOS)
    # =========================
    grades = {
        "parvulos": {"matricula": "580.000", "pension": "377.000"},
        "pre-jardin": {"matricula": "580.000", "pension": "377.000"},
        "jardin": {"matricula": "524.273", "pension": "377.000"},
        "transicion": {"matricula": "507.957", "pension": "350.000"}
    }

    extras = {
        "seguro estudiantil": "30.000",
        "agenda opcional": "32.000",
        "otros": "35.000",
        "modulos": "71.000",
        "actividad extracurricular": "170.000",
        "navidad": "170.000",
        "dia de la familia": "170.000",
        "dia de navidad": "170.000"
    }

    # =========================
    # 🧠 PDF 2 - RIE
    # =========================
    rie_servicios = {
        "servicio permanente": [
            "7:00 AM a 1:00 PM → $431.000",
            "7:00 AM a 3:00 PM → $482.000",
            "7:00 AM a 5:00 PM → $530.000"
        ],
        "servicio circunstancial": [
            "Costo por hora → $11.000"
        ]
    }

    rie_info = [
        "Programa educativo con apoyo integral (RIE)",
        "Incluye jornada de cuidado y acompañamiento",
        "Requiere almuerzo enviado por la familia",
        "Atención según disponibilidad del programa"
    ]

    # =========================
    # 🧠 DETECTAR INTENCIÓN DE FECHAS
    # =========================
    is_date_question = (
        "fecha" in q or
        "fechas" in q or
        "cuando" in q or
        "horario" in q
    )

    # =========================
    # 🔵 PDF 1 LOGIC (GRADOS)
    # =========================
    for grade, values in grades.items():
        if grade in q:

            if is_date_question:
                continue

            if "pension" in q:
                return f"La pensión de {grade} es ${values['pension']}."

            if "matricula" in q or "costo" in q or "cuesta" in q:
                return f"La matrícula de {grade} es ${values['matricula']}."

    # =========================
    # 🔵 EXTRAS
    # =========================
    for key, value in extras.items():
        if key in q:
            return f"El costo de {key} es ${value}."

    # =========================
    # 🔵 PDF 2 LOGIC (RIE)
    # =========================
    if "rie" in q and ("que ofrece" in q or "que incluye" in q or "informacion" in q):
        return (
            "El programa RIE (Ruta Integral Educativa) ofrece:\n\n"
            "- Apoyo integral con acompañamiento durante la jornada\n"
            "- Cuidado del estudiante en horarios extendidos\n"
            "- Atención según disponibilidad del programa\n"
            "- Requiere que la familia envíe el almuerzo\n"
        )

    if "servicio circunstancial" in q:
        if "costo" in q or "cuesta" in q or "valor" in q:
            return "El servicio circunstancial tiene un costo de $11.000 por hora."

        return "El servicio circunstancial es un servicio ocasional con previa notificación."

    if "servicio permanente" in q:
        return (
            "El servicio permanente:\n"
            "- 7:00 AM a 1:00 PM → $431.000\n"
            "- 7:00 AM a 3:00 PM → $482.000\n"
            "- 7:00 AM a 5:00 PM → $530.000"
        )

    if "rie" in q and ("costo" in q or "cuesta" in q or "valor" in q):
        return (
            "RIE costos:\n"
            "- 7:00 AM a 1:00 PM → $431.000\n"
            "- 7:00 AM a 3:00 PM → $482.000\n"
            "- 7:00 AM a 5:00 PM → $530.000\n"
            "- $11.000 por hora circunstancial"
        )

    if "rie" in q or "programa rie" in q:
        response = "El programa RIE ofrece:\n\n"

        response += "📌 Servicios:\n"
        for item in rie_info:
            response += f"- {item}\n"

        response += "\n📌 Modalidades:\n"

        for key, items in rie_servicios.items():
            response += f"\n{key.upper()}:\n"
            for i in items:
                response += f"- {i}\n"

        return response

    # =========================
    # 🔵 RAG FALLBACK (CHROMA) - FIXED
    # =========================
    try:
        context = search(question)
    except Exception as e:
        print("RAG ERROR:", str(e))
        context = []

    if not context:
        return "No encontré información en los documentos (RAG no disponible en este momento)."

    best_chunk = context[0]

    if not best_chunk or len(best_chunk.strip()) < 20:
        return "No encontré información en los documentos."

    # 🔥 extracción inteligente de fechas (CON FILTRO POR GRADO)
    if "fecha" in q or "fechas" in q:

        response = ""

        ask_parvulos = "parvulos" in q
        ask_prejardin = "prejardin" in q or "pre-jardin" in q
        ask_jardin = "jardin" in q
        ask_transicion = "transicion" in q

        if ask_parvulos or ask_prejardin:
            if "02 de julio" in best_chunk:
                response += "Parvulos y Prejardín:\n- 02 de julio de 2025\n- 7:00 AM a 9:00 AM\n\n"

        if ask_jardin or ask_transicion:
            if "03 de julio" in best_chunk:
                response += "Jardín y Transición:\n- 03 de julio de 2025\n- 9:30 AM a 12:30 PM\n"

        if not response:
            if "02 de julio" in best_chunk:
                response += "Parvulos y Prejardín:\n- 02 de julio de 2025\n- 7:00 AM a 9:00 AM\n\n"

            if "03 de julio" in best_chunk:
                response += "Jardín y Transición:\n- 03 de julio de 2025\n- 9:30 AM a 12:30 PM\n"

        if response:
            return response.strip()

    return f"Según los documentos oficiales de Melositos:\n\n{best_chunk}"