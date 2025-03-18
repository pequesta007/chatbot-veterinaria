import json
import fitz  # PyMuPDF

def extraer_texto_pdf(pdf_path):
    """Extrae el texto de un PDF y lo devuelve como un diccionario estructurado."""
    doc = fitz.open(pdf_path)
    texto = ""

    for pagina in doc:
        texto += pagina.get_text("text") + "\n"

    return {"contenido": texto}

def cargar_datos_pdf(pdf_path):
    """Carga los datos del PDF, extrayendo el texto y guardándolo en un JSON."""
    json_path = "data/data.json"

    try:
        datos = extraer_texto_pdf(pdf_path)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        return datos

    except Exception as e:
        print(f"Error al procesar el PDF: {e}")
        return {}