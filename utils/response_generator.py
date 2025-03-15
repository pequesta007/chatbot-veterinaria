import json

def generar_respuesta(pregunta, datos):
    pregunta = pregunta.lower()
    
    # Recorrer cada PDF en el JSON
    for pdf_nombre, secciones in datos.items():
        for titulo, contenido in secciones.items():
            if pregunta in titulo.lower() or pregunta in contenido.lower():
                return contenido  # Devuelve la sección donde se encontró la respuesta

    return "Lo siento, no encontré información sobre eso en mi base de datos."
