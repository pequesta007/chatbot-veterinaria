from flask import Flask, request, jsonify
from utils.response_generator import buscar_respuesta
from utils.data_loader import convertir_pdf_a_json

app = Flask(__name__)
PDF_PATH = "data/veterinaria.pdf"
JSON_PATH = "data/respuestas.json"

# Convertir el PDF a JSON antes de iniciar el bot
convertir_pdf_a_json(PDF_PATH, JSON_PATH)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    datos = request.get_json()
    pregunta = datos.get("pregunta", "").lower()

    if not pregunta:
        return jsonify({"respuesta": "No entendí tu pregunta."})

    respuesta = buscar_respuesta(pregunta, JSON_PATH)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
