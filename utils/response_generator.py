def generar_respuesta(pregunta, datos):
    """Busca la mejor respuesta en el JSON estructurado."""

    pregunta = pregunta.lower().strip()
    
    mejor_respuesta = None
    mejor_puntaje = 0

    # Recorremos los documentos PDF procesados
    for documento, secciones in datos.items():
        for titulo, contenido in secciones.items():
            titulo_lower = titulo.lower()
            contenido_lower = contenido.lower()

            # Si la pregunta coincide con un título, devolver esa sección
            if pregunta in titulo_lower:
                return f"{titulo}: {contenido[:500]}..."

            # Si la pregunta aparece en el contenido, contar coincidencias
            coincidencias = contenido_lower.count(pregunta)
            if coincidencias > mejor_puntaje:
                mejor_puntaje = coincidencias
                mejor_respuesta = f"{titulo}: {contenido[:500]}..."  # Limitar la respuesta

    # Si encontramos algo, lo devolvemos
    if mejor_respuesta:
        return mejor_respuesta

    return "Lo siento, no encontré información sobre eso en mi base de datos."
