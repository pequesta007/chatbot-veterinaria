import json

# Cargar el archivo JSON con los datos de la mascota
def cargar_datos():
    with open('data/data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Obtener la respuesta en función de la consulta del usuario
def obtener_respuesta(query):
    datos = cargar_datos()
    
    # Iterar sobre los títulos y contenidos del JSON para encontrar la respuesta más relevante
    for item in datos['Informacion General']:
        if query.lower() in item['contenido'].lower():
            return item['contenido']
    
    return "Lo siento, no pude encontrar información relacionada con esa consulta."

# Función que inicia la interacción con el usuario
def iniciar_chat():
    print("¡Hola! Soy el asistente virtual para la gestión de mascotas. ¿En qué puedo ayudarte hoy?")
    while True:
        # Obtener la pregunta del usuario
        query = input("Tú: ")
        
        # Si el usuario escribe "salir", terminamos el chat
        if query.lower() == "salir":
            print("¡Gracias por usar el servicio! Hasta pronto.")
            break
        
        # Buscar la respuesta y mostrarla
        respuesta = obtener_respuesta(query)
        print(f"Bot: {respuesta}")
