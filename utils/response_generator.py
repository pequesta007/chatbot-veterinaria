import json

# Cargar datos desde el archivo JSON
def cargar_datos():
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Generar una respuesta basada en la pregunta
def generar_respuesta(pregunta, datos):
    pregunta = pregunta.lower()
    
    for pdf, secciones in datos.items():  # Iterar sobre cada PDF en el JSON
        if isinstance(secciones, dict):  
            for titulo, contenido in secciones.items():
                if pregunta in titulo.lower() or pregunta in contenido.lower():
                    return contenido
    
    return "Lo siento, no encontré información sobre eso en mi base de datos."
