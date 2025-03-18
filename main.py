from flask import Flask, request, jsonify
from utils.data_loader import cargar_datos_pdf
from utils.response_generator import generar_respuesta

app = Flask(__name__)

# Cargar datos al iniciar
datos = cargar_datos_pdf()

@app.route('/')
def home():
    return "Bienvenido al chatbot de Muni Mascotas!"

@app.route('/chat', methods=['POST'])
def chat():
    pregunta = request.json.get('pregunta')
    
    if not pregunta:
        return jsonify({"error": "No se recibió una pregunta."}), 400

    print(f"📩 Pregunta recibida: {pregunta}")
    
    respuesta = generar_respuesta(pregunta, datos)

    print(f"📤 Respuesta enviada: {respuesta}")
    
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
