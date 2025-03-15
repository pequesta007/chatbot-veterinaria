import os
import json
import re
import fitz  # PyMuPDF

# Ruta de las carpetas
pdf_folder = 'pdfs/'
data_file = 'data/data.json'

# Función para limpiar texto y corregir errores comunes
def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)  # Eliminar caracteres no imprimibles
    text = text.replace('gesón', 'gestión')  
    text = text.replace('ges\u0015n', 'gestión')  
    text = re.sub(r'\s+', ' ', text).strip()  # Normalizar espacios y saltos de línea
    return text

# Función para extraer texto de un PDF y estructurarlo
def extract_text_from_pdf(pdf_path):
    text_data = {}
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text("text") + "\n"
        
        full_text = clean_text(full_text)

        # Dividir en secciones basadas en títulos en MAYÚSCULAS
        secciones = re.split(r'\n(?=[A-ZÁÉÍÓÚÑ ]+\n)', full_text)
        
        for seccion in secciones:
            lineas = seccion.strip().split("\n", 1)
            if len(lineas) == 2:
                titulo, contenido = lineas
                text_data[titulo.strip()] = contenido.strip()
        
    except Exception as e:
        print(f"Error al procesar el PDF {pdf_path}: {e}")
    
    return text_data

# Función para guardar los datos en un archivo JSON
def save_data_to_json(data):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Función principal para cargar datos de PDFs y guardarlos en el archivo JSON
def cargar_datos_pdf():
    data = {}

    # Buscar los archivos PDF en la carpeta
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"No se encontraron archivos PDF en {pdf_folder}.")
        return data

    print(f"Procesando {len(pdf_files)} PDFs...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        print(f"🔹 Extrayendo texto de: {pdf_file}")
        data[pdf_file] = extract_text_from_pdf(pdf_path)

    # Guardar los datos estructurados en el JSON
    save_data_to_json(data)
    print(f"✅ Datos guardados correctamente en {data_file}")

    return data
