import json

def generar_respuesta(pregunta, datos):
    """Busca la mejor respuesta en el contenido extraído del PDF."""
    if not datos or "contenido" not in datos:
        return "Lo siento, no tengo información en mi base de datos."

    contenido = datos["contenido"].lower()

    if pregunta.lower() in contenido:
        return "Sí, tengo información sobre eso. Aquí está lo que encontré: \n" + contenido[:500]  # Resumen

    return "Lo siento, no encontré información sobre eso en mi base de datos."
