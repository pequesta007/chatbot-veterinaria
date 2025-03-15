import os
import json
import fitz  # PyMuPDF

# Rutas
pdf_folder = "pdfs/"
data_file = "data/data.json"

def extract_text_from_pdf(pdf_path):
    """Extrae el texto del PDF dividiéndolo por títulos y contenido"""
    doc = fitz.open(pdf_path)
    data = {}
    current_title = "Introducción"  # Nombre inicial por defecto
    content = ""

    for page in doc:
        text = page.get_text("text")
        lines = text.split("\n")

        for line in lines:
            line = line.strip()
            if line.isupper():  # Detectar títulos en MAYÚSCULAS
                if content:
                    data[current_title] = content.strip()
                current_title = line
                content = ""
            else:
                content += line + " "

    if content:
        data[current_title] = content.strip()

    return data

def cargar_datos_pdf():
    """Carga los PDFs, los extrae y guarda en JSON"""
    if not os.path.exists(data_file):
        print("Creando archivo JSON vacío...")
        data = {}
    else:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    if pdf_files:
        print(f"Procesando {len(pdf_files)} PDFs...")
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"🔹 Extrayendo texto de: {pdf_file}")
            extracted_data = extract_text_from_pdf(pdf_path)
            data[pdf_file] = extracted_data

        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("✅ Datos guardados correctamente en data/data.json")
    else:
        print("No se encontraron PDFs en la carpeta.")

    return data
