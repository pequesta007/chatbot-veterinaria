import os
import json
import re
from PyPDF2 import PdfReader

# Rutas de las carpetas
pdf_folder = 'pdfs/'
data_file = 'data/data.json'

# Expresión regular mejorada para detectar títulos de secciones
TITULO_REGEX = r"^(?:\d+\.\s*)?[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑ\s]+"

def clean_text(text):
    """Limpia el texto eliminando caracteres raros y espacios extras"""
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)  # Elimina caracteres no imprimibles
    text = re.sub(r'\s+', ' ', text).strip()  # Normaliza espacios
    return text

def extract_text_from_pdf(pdf_path):
    """Extrae el texto del PDF página por página"""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"⚠️ Error al procesar el PDF {pdf_path}: {e}")
    return text

def segmentar_por_titulos(texto):
    """Segmenta el contenido en un diccionario basado en títulos"""
    secciones = {}
    lineas = texto.split("\n")
    titulo_actual = "Introducción"  # Título por defecto si no encuentra uno
    contenido_actual = ""

    for linea in lineas:
        linea = linea.strip()
        if re.match(TITULO_REGEX, linea):  # Si encuentra un título
            if contenido_actual:  # Guarda la sección anterior
                secciones[titulo_actual] = contenido_actual.strip()
            titulo_actual = linea  # Nuevo título detectado
            contenido_actual = ""  # Reinicia el contenido
        else:
            contenido_actual += linea + " "

    # Guardar la última sección procesada
    if contenido_actual:
        secciones[titulo_actual] = contenido_actual.strip()

    return secciones

def save_data_to_json(data):
    """Guarda los datos estructurados en JSON"""
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def cargar_datos_pdf():
    """Carga los PDFs, los segmenta por títulos y los guarda en JSON"""
    if not os.path.exists(data_file):
        print("📂 El archivo data.json no existe. Creando uno nuevo.")
        data = {}
    else:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if pdf_files:
        print(f"📑 Se encontraron {len(pdf_files)} PDFs en {pdf_folder}, procesando...")

        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"🔍 Procesando el PDF: {pdf_file}")

            texto_extraido = extract_text_from_pdf(pdf_path)
            texto_limpio = clean_text(texto_extraido)

            # Segmentar el texto en secciones
            secciones = segmentar_por_titulos(texto_limpio)

            # Guardar el PDF en el diccionario
            data[pdf_file.replace(".pdf", "")] = secciones
        
        save_data_to_json(data)
        print(f"✅ Datos guardados correctamente en: {data_file}")
    else:
        print("⚠️ No se encontraron archivos PDF en la carpeta.")
    
    return data
