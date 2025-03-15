import json

DATA_FILE = "data/data.json"

def cargar_datos():
    """Carga los datos del JSON en un diccionario."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠ El archivo {DATA_FILE} no existe.")
        return {}

def generar_respuesta(pregunta, datos):
    """Busca la respuesta en el JSON a partir de la pregunta."""
    pregunta = pregunta.lower()

    for titulo, contenido in datos.items():
        if pregunta in contenido.lower():
            return contenido

    return "Lo siento, no encontré información sobre eso en mi base de datos."
