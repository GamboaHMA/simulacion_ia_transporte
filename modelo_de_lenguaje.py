import os
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path
import fitz
import re
import json
from variable import Vehicle
from py_code_to_string import vehicle_class

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"⚠️ Error al procesar PDF {pdf_path}: {str(e)}")
        return None

def load_documents(directory="pdf_documents"):
    """Carga todos los documentos de texto en un directorio especificado"""
    documents = []
    try:
        for file_path in Path(directory).glob("*.pdf"):
            text = extract_text_from_pdf(file_path)
            text = ' '.join(text.replace('\n', ' ').replace('_', ' ').split())
            if text:
                documents.append({
                    "name": file_path.name,
                    "content": text 
                })
        print(f"\n {len(documents)} documentos cargados desde '{directory}'\n")
    except Exception as e:
        print(f"⚠️ Error al cargar documentos: {str(e)}")
    return documents

def generate_prompt_with_context_vehicle_g(user_input, documents, use_web=False):
    """Genera un prompt contextualizado con documentos locales y opción de web"""
    context = ""
    
    # Agregar contexto de documentos locales
    if documents:
        context += "CONTEXTO DE DOCUMENTOS LOCALES:\n"
        for doc in documents:
            context += f"\nDOCUMENTO: {doc['name']}\n{doc['content']}\n"
    
    # Instrucciones para la búsqueda web si es necesario
    if use_web:
        context += "\nINSTRUCCIÓN: Si la información necesaria no se encuentra en los documentos locales, " \
                  "por favor realiza una búsqueda web confiable para complementar la respuesta."
    
    # Combinar todo en el prompt final por ahora no tiene en cuenta lo que pone el usuario
    full_prompt = f"{context}\n\nPREGUNTA DEL USUARIO: \nRESPUESTA:"
    return full_prompt

def chat_with_gemini():
    print("Chat con Gemini (escribe 'salir' para terminar)\n")
    print("Opciones especiales:")
    print("  '/web' al inicio para forzar búsqueda web")
    print("  '/local' al inicio para usar solo documentos locales\n")
    
    # Cargar documentos al iniciar
    documents = load_documents()
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("Tú: ") 
        if user_input.lower() in ['salir', 'exit', 'q']:
            break
        
        # Determinar si se debe usar web
        use_web = False
        if user_input.startswith('/web'):
            use_web = True
            user_input = user_input[4:].strip()
        elif user_input.startswith('/local'):
            use_web = False
            user_input = user_input[6:].strip()
        use_web = True
        print(f"Uso de web: {use_web}")
        
        try:
            # Generar prompt contextualizado
            prompt = generate_prompt_with_context_vehicle_g(user_input, documents, use_web)
            prompt += vehicle_class
            
            # Enviar al modelo
            response = chat.send_message(prompt)
            
            # Mostrar respuesta
            print(f"\nGemini: {response.text}\n")
            if use_web:
                print(" Respuesta complementada con búsqueda web]\n")
            elif documents:
                print(" Respuesta basada en documentos locales]\n")
            
        except Exception as e:
            print(f" Error: {str(e)}")

def conteo_de_palabras(text) -> int:
    return len(re.findall(r'\b[\w-]+\b', text["content"]))

def obtain_json_str(string:str):
    result = re.search(r'```json(.*?)```', string, re.DOTALL).string
    result = result.replace("```", '').replace('\n', '').replace('json', '')
    return result

def obtain_vehicles():
    vehicles = []
    documents = load_documents()
    chat = model.start_chat(history=[])

    user_input = input("especificaciones de vehiculos ")
    user_input = user_input.split()
    use_web = False

    try:
        #generar promt para generar vehiculos
        prompt = generate_prompt_with_context_vehicle_g(user_input, documents, use_web)
        prompt = prompt + f"Genera {user_input[0]} vehiculos en json siguiendo la estructura de la clase: {vehicle_class}"

        response = chat.send_message(prompt)
        vehicles_json = obtain_json_str(response.text)
        print(vehicles_json)

        if vehicles_json:
            vehicles_data = json.loads(vehicles_json)
            for vehicle_data in vehicles_data:
                vehicle = Vehicle(
                    id=vehicle_data["id"],
                    altura=vehicle_data["altura"],
                    capacidad=vehicle_data["capacidad"],
                    tipo_de_combustible=vehicle_data["tipo_de_combustible"]
                )
                vehicles.append(vehicle)
    except Exception as e:
        print(f" Error: {str(e)}")
    
    return vehicles