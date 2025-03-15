import os
import json
import PyPDF2

def extraer_texto_pdf(pdf_path):
    """Extrae el texto de un archivo PDF."""
    texto = ""
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                texto += page.extract_text() or ""
    except Exception as e:
        print(f"Error al extraer texto del PDF {pdf_path}: {e}")
    return texto

def cargar_datos_pdf(pdf_folder='pdfs/', data_file='data/data.json'):
    """Carga textos de archivos PDF y los guarda en un archivo JSON."""
    data = {}
    if not os.path.exists(pdf_folder):
        print(f"La carpeta {pdf_folder} no existe.")
        return data

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"No se encontraron archivos PDF en la carpeta {pdf_folder}.")
        return data

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        texto = extraer_texto_pdf(pdf_path)
        if texto:
            data[pdf_file] = texto
        else:
            print(f"No se pudo extraer texto del archivo {pdf_file}.")

    if data:
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Datos guardados en {data_file}.")
    else:
        print("No se extrajo texto de ningún PDF.")

    return data
