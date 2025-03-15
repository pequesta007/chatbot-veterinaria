import os
import json
import fitz  # PyMuPDF

# Definir rutas
PDF_FOLDER = "pdfs/"
DATA_FILE = "data/data.json"

def extract_text_from_pdf(pdf_path):
    """Extrae el texto de un PDF y lo estructura por secciones."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error al procesar el PDF {pdf_path}: {e}")
    return text.strip()

def save_data_to_json(data):
    """Guarda los datos en un archivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def cargar_datos_pdf():
    """Carga y estructura los datos de los PDFs en JSON."""
    data = {}

    # Verificar si la carpeta de PDFs existe
    if not os.path.exists(PDF_FOLDER):
        print(f"La carpeta {PDF_FOLDER} no existe.")
        return data

    # Procesar cada PDF en la carpeta
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    if pdf_files:
        print(f"Procesando {len(pdf_files)} PDFs...")
        for pdf_file in pdf_files:
            pdf_path = os.path.join(PDF_FOLDER, pdf_file)
            print(f"🔹 Extrayendo texto de: {pdf_file}")
            extracted_text = extract_text_from_pdf(pdf_path)

            # Almacenar los datos con el nombre del PDF como clave
            data[pdf_file.replace(".pdf", "")] = extracted_text

        # Guardar en JSON
        save_data_to_json(data)
        print(f"✅ Datos guardados correctamente en {DATA_FILE}")
    else:
        print("⚠ No se encontraron archivos PDF para procesar.")

    return data
