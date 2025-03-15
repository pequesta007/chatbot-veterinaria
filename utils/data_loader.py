import os
import json
import re
from PyPDF2 import PdfReader

# Ruta de las carpetas
pdf_folder = 'pdfs/'
data_file = 'data/data.json'

# Función para limpiar texto y corregir errores
def clean_text(text):
    """Elimina caracteres extraños y limpia el texto extraído del PDF."""
    if text is None:
        return ""
    
    # Eliminar caracteres no imprimibles y de control
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', ' ', text)
    
    # Normalizar espacios y saltos de línea
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Función para extraer texto de un PDF
def extract_text_from_pdf(pdf_path):
    """Extrae y limpia el texto de un PDF."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    except Exception as e:
        print(f"Error al procesar el PDF {pdf_path}: {e}")
    
    return clean_text(text)

# Función para guardar los datos en un archivo JSON
def save_data_to_json(data):
    """Guarda el contenido en un archivo JSON bien estructurado."""
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Función principal para cargar datos de PDFs y guardarlos en JSON
def cargar_datos_pdf():
    """Lee los PDFs, extrae el texto y lo guarda en formato JSON estructurado."""
    if not os.path.exists(data_file):
        print("El archivo data/data.json no existe. Creando uno nuevo.")
        data = {}
    else:
        with open(data_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if pdf_files:
        print(f"Se encontraron {len(pdf_files)} PDFs en {pdf_folder}, procesando...")

        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"Procesando el PDF: {pdf_file}")
            extracted_text = extract_text_from_pdf(pdf_path)

            if extracted_text:
                data[pdf_file.replace(".pdf", "")] = extracted_text

        save_data_to_json(data)
        print(f"Datos guardados correctamente en: {data_file}")
    else:
        print(f"No se encontraron archivos PDF en {pdf_folder}.")

    return data
