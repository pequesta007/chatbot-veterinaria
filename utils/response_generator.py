import spacy
from utils.data_loader import cargar_datos_json

nlp = spacy.load("es_core_news_md")

def buscar_respuesta(pregunta, json_path):
    """Busca la mejor respuesta dentro del JSON."""
    oraciones = cargar_datos_json(json_path)  # Cargamos el JSON
    doc_pregunta = nlp(pregunta)

    mejor_respuesta = ""
    mayor_similitud = 0.0

    for oracion in oraciones:
        doc_oracion = nlp(oracion)
        similitud = doc_pregunta.similarity(doc_oracion)  # Comparamos con cada oración

        if similitud > mayor_similitud:
            mayor_similitud = similitud
            mejor_respuesta = oracion

    if mayor_similitud > 0.6:  # Si la similitud es aceptable, devolvemos la mejor respuesta
        return mejor_respuesta
    else:
        return "Lo siento, no encontré una respuesta exacta."
