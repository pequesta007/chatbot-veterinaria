import os
import json
import re
from PyPDF2 import PdfReader

pdf_folder = 'pdfs/'
data_file = 'data/data.json'

# 🔹 Función para limpiar el texto
def clean_text(text):
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', ' ', text)  # Elimina caracteres raros
    text = re.sub(r'\s+', ' ', text).strip()  # Elimina espacios dobles
    return text

# 🔹 Extraer y organizar texto del PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    
    return clean_text(text)

# 🔹 Guardar en JSON
def save_data_to_json(data):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 🔹 Procesar PDFs
def cargar_datos_pdf():
    data = {}

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        print("No se encontraron PDFs en la carpeta.")
        return data

    print(f"Procesando {len(pdf_files)} PDFs...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        print(f"🔹 Extrayendo texto de: {pdf_file}")

        extracted_text = extract_text_from_pdf(pdf_path)
        sections = extracted_text.split("\n\n")  # 🔹 Separa el contenido en secciones
        
        pdf_dict = {}
        for i in range(0, len(sections) - 1, 2):
            title = sections[i].strip()
            content = sections[i+1].strip() if i+1 < len(sections) else ""
            pdf_dict[title] = content  # 🔹 Guarda como {Título: Contenido}

        data[pdf_file.replace(".pdf", "")] = pdf_dict  # 🔹 Guarda en el JSON
    
    save_data_to_json(data)
    print(f"✅ Datos guardados correctamente en {data_file}")
    return data