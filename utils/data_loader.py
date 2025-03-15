import fitz  # PyMuPDF para leer PDF
import json
import os

PDF_PATH = "data/veterinaria.pdf"
JSON_PATH = "data/respuestas.json"

def extraer_texto_pdf(pdf_path):
    """Extrae el texto del PDF y lo devuelve como una lista de oraciones."""
    doc = fitz.open(pdf_path)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text("text") + "\n"

    oraciones = [oracion.strip() for oracion in texto.split(". ") if len(oracion) > 10]  # Separa en oraciones
    return oraciones

def convertir_pdf_a_json(pdf_path, json_path):
    """Convierte el texto del PDF en JSON para búsquedas rápidas."""
    if os.path.exists(json_path):  # Si ya existe, no lo vuelve a generar
        return
    
    oraciones = extraer_texto_pdf(pdf_path)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(oraciones, f, indent=4, ensure_ascii=False)  # Guarda como JSON

def cargar_datos_json(json_path):
    """Carga las respuestas desde el JSON."""
    if not os.path.exists(json_path):
        convertir_pdf_a_json(PDF_PATH, JSON_PATH)  # Si no existe, lo crea
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
