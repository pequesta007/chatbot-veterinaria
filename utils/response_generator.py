def generar_respuesta(pregunta, datos):
    """Busca la respuesta en la base de datos JSON."""
    pregunta = pregunta.lower()

    for titulo, contenido in datos.items():
        if pregunta in contenido.lower():
            return contenido

    return "Lo siento, no encontré información sobre eso en mi base de datos."
