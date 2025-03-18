import os
import json
import fitz  # PyMuPDF
import re

# Ruta de las carpetas
pdf_folder = 'pdfs/'
data_file = 'data/data.json'

# Función para limpiar texto
def clean_text(text):
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)  # Eliminar caracteres no imprimibles
    text = re.sub(r'\s+', ' ', text).strip()  # Normalizar espacios
    return text

# Función para extraer texto y dividirlo en secciones
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"

    cleaned_text = clean_text(text)

    # Separar por títulos detectados (Ejemplo: "1. REGISTRO Y GESTIÓN DE MASCOTAS")
    sections = {}
    current_title = "Introducción"
    sections[current_title] = ""

    for line in cleaned_text.split("\n"):
        line = line.strip()
        if re.match(r'^\d+\.\s+', line):  # Detecta títulos numerados
            current_title = line
            sections[current_title] = ""
        else:
            sections[current_title] += line + " "

    return sections

# Guardar datos en JSON
def save_data_to_json(data):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Función principal para cargar datos
def cargar_datos_pdf():
    if not os.path.exists(data_file):
        print("📂 Creando un nuevo archivo JSON...")
        data = {}
    else:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    if pdf_files:
        print(f"📄 Procesando {len(pdf_files)} PDFs...")
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"🔹 Extrayendo texto de: {pdf_file}")
            extracted_data = extract_text_from_pdf(pdf_path)
            data[pdf_file] = extracted_data
        
        save_data_to_json(data)
        print("✅ Datos guardados correctamente en data/data.json")
    else:
        print("⚠ No se encontraron archivos PDF en la carpeta.")

    return data