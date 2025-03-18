import re

def generar_respuesta(pregunta, datos):
    pregunta = pregunta.lower()
    
    mejores_coincidencias = []

    for pdf, secciones in datos.items():
        for titulo, contenido in secciones.items():
            if re.search(r'\b' + re.escape(pregunta) + r'\b', titulo.lower()):
                return contenido  # Devuelve el contenido de la sección encontrada
            
            if re.search(r'\b' + re.escape(pregunta) + r'\b', contenido.lower()):
                mejores_coincidencias.append((titulo, contenido))

    if mejores_coincidencias:
        mejor_titulo, mejor_contenido = mejores_coincidencias[0]
        return f"{mejor_titulo}: {mejor_contenido}"

    return "Lo siento, no encontré información sobre eso en mi base de datos."
