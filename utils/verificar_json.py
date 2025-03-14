import json
import os

# Ruta del archivo JSON que contiene los datos extraídos
DATA_FILE = "chatbot/data/data.json"

def verificar_datos():
    """Lee y muestra el contenido de data.json."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as archivo_json:
            datos_pdf = json.load(archivo_json)
            # Imprime el contenido del archivo
            print("Contenido de data.json:")
            print(json.dumps(datos_pdf, indent=4, ensure_ascii=False))
    else:
        print(f"El archivo {DATA_FILE} no existe.")

if __name__ == "__main__":
    verificar_datos()

