import json

def generar_respuesta(pregunta, datos):
    """Busca una respuesta en el JSON basado en la pregunta del usuario"""
    pregunta = pregunta.lower()

    for archivo, secciones in datos.items():
        for titulo, contenido in secciones.items():
            if pregunta in titulo.lower() or pregunta in contenido.lower():
                return f"📌 {titulo}: {contenido[:500]}..."  # Limita a 500 caracteres

    return "Lo siento, no encontré información sobre eso en mi base de datos."
