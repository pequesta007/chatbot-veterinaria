from flask import Flask, request, jsonify
from utils.data_loader import cargar_datos_pdf
from utils.response_generator import generar_respuesta

app = Flask(__name__)

# Cargar datos desde el PDF
datos = cargar_datos_pdf("data/MUNI MASCOTAS ATENCIÓN (1).pdf")

@app.route("/")
def home():
    return "Chatbot de Veterinaria en ejecución."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        pregunta = data.get("pregunta", "").strip()

        if not pregunta:
            return jsonify({"respuesta": "Por favor, ingresa una pregunta válida."})

        respuesta = generar_respuesta(pregunta, datos)
        return jsonify({"respuesta": respuesta})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)