from flask import Flask, request, jsonify
from utils.data_loader import cargar_datos_pdf
from utils.response_generator import generar_respuesta

app = Flask(__name__)

# Cargar los datos al iniciar
datos = cargar_datos_pdf()

@app.route('/')
def home():
    return "Bienvenido al chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    pregunta = request.json.get('pregunta')
    if pregunta:
        respuesta = generar_respuesta(pregunta, datos)
        return jsonify({"respuesta": respuesta})
    return jsonify({"error": "No se recibió una pregunta."}), 400

if __name__ == '__main__':
    app.run(debug=True)
