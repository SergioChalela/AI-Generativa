import os
from dotenv import load_dotenv
import openai
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Cargar las variables de entorno desde el archivo 'api.env'
load_dotenv(dotenv_path="app/api.env")

# Verificar si la clave API se carga correctamente
print(os.getenv("OPENAI_API_KEY"))

# Asignar la clave API directamente desde el archivo 'api.env'
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Ruta para servir el archivo HTML
@app.get("/", response_class=HTMLResponse)
async def get_home():
    with open("app/index.html", "r") as file:
        return file.read()

# Endpoint para manejar las solicitudes de chat
class ChatRequest(BaseModel):
    prompt: str

# Inicializar el historial de conversación con un mensaje de sistema para definir el contexto
conversation_history = [
    {"role": "system", "content": "Eres un asistente de servicio al cliente para la empresa 'SergioTech'. Tu tarea es ayudar a los clientes con preguntas sobre productos, devoluciones y soporte."}
]

@app.post("/chat/")
async def chat(request: ChatRequest):
    global conversation_history
    # Agregar el mensaje del usuario al historial
    conversation_history.append({"role": "user", "content": request.prompt})
    
    try:
        # Solicitar a la API de OpenAI con el historial de conversación
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usa "gpt-4" si tienes acceso
            messages=conversation_history,
            max_tokens=150,
            temperature=0.7
        )

        # Extraer la respuesta del modelo
        model_response = response.choices[0].message["content"]
        
        # Agregar la respuesta del modelo al historial de conversación
        conversation_history.append({"role": "assistant", "content": model_response})
        
        # Retornar la respuesta generada por el modelo
        return {"response": model_response}
    
    except Exception as e:
        # En caso de error, mostrar un mensaje de error
        return {"response": f"Error en la respuesta: {str(e)}"}


