import os
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path
import fitz
import re
import json
from variable import Vehicle, System, OrderVar, Rute, RuteNode
from py_code_to_string import vehicle_class, tipos_de_combustible
from data import rutas, new_orders 

def estimar_costo_vehiculo(vehicle:Vehicle) -> float:
    k1 = 50000 # constante para escala
    precio_por_tonelada = k1/vehicle.altura
    costo_total = precio_por_tonelada * vehicle.capacidad
    return costo_total

capacidad_rangos = {
    "liviano": "5000-13000",
    "medio": "14000-22000",
    "semipesado": "23000-31000",
    "pesado": "32000-42000",
}

altura_rangos = {
    "pequeno": "2.90-3.30",
    "estandar": "3.30-3.70",
    "grande": "3.70-4.00"
}

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

def generate_prompt_with_context_vehicle_g(documents, use_web=False):
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
            prompt = generate_prompt_with_context_vehicle_g(documents, use_web)
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

def obtain_vehicles(cant:int=None):
    vehicles = []
    documents = load_documents()
    chat = model.start_chat(history=[])

    if cant==None:
        while(True):
            user_input = input("introduzca la cantidad de vehiculos: ")
            try:
                cant = int(user_input)
                break
            except:
                print("numero invalido")

    use_web = False

    try:
        #generar promt para generar vehiculos
        prompt = generate_prompt_with_context_vehicle_g(documents, use_web)
        prompt = prompt + f"Genera {cant} vehiculos en json siguiendo la estructura de la clase: {vehicle_class}. "
        prompt = prompt + f"En los tipos de combustible usa estos {tipos_de_combustible} "
        prompt = prompt + f"y que respete los rangos de {capacidad_rangos} y {altura_rangos}"

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

def obtain_vehicles_grad():
    initial_cant = 0
    cant = initial_cant
    documents = load_documents()
    chat = model.start_chat(history=[])

    use_web = False

    previous_json = ""
    context_feedback = ""

    vehicles = []
    vehicles_id = []

    while(True):
        cant += 10
        if cant >= 100:
            return None

        prompt_base = generate_prompt_with_context_vehicle_g(documents, use_web)
        prompt_base += f"Genera {cant} vehiculos en json siguiendo la estructura de la clase: {vehicle_class}. "
        prompt_base += f"En los tipos de combustible usa estos {tipos_de_combustible}"
        prompt_base += f"y que respete los rangos de {capacidad_rangos} y {altura_rangos}"

        prompt = prompt_base
        if previous_json:
            prompt += f"Estos fueron los vehiculos generados anteriormente {previous_json}"
        if context_feedback:
            prompt += f"Sin embargo no fueron suficientes ya que: {context_feedback}"

        try:
            response = chat.send_message(prompt)
            vehicles_json = obtain_json_str(response.text)
            previous_json = vehicles_json
            print(vehicles_json)
            if vehicles_json:
                vehicles_data = json.loads(vehicles_json)
                for vehicle_data in vehicles_data:
                    if vehicle_data["id"] not in vehicles_id:
                        vehicle = Vehicle(
                            id=vehicle_data["id"],
                            altura=vehicle_data["altura"],
                            capacidad=vehicle_data["capacidad"],
                            tipo_de_combustible=vehicle_data["tipo_de_combustible"]
                        )
                        vehicles_id.append(vehicle.id)
                        vehicles.append(vehicle)
        except Exception as e:
            print(f" Error: {str(e)}")
        
        system = System(rutes=rutas, orders=new_orders, vehicles=vehicles)

        empty_domains = []
        context_feedback = "Hacen falta algunos vehiculos que satisfagan restricciones como: \n"
        for order, order_domain in system.orders_domain.items():
            if len(order_domain) == 0:
                ruta = None
                for ruta_ in rutas:
                    if order.rute_node.rute_id == ruta_.id:
                        ruta = ruta_
                        break
                context_feedback += f"Capacidad mayor o igual a: {order.cant} Capacidad menor o igual a {ruta.peso_m} Altura menor o igual a {ruta.altura_m}\n"
                empty_domains.append(order_domain)
        if len(empty_domains) != 0:
            continue
        initial_solution = system.initial_solution()
        if initial_solution:
            return vehicles
        else:
            print("empty solution")

