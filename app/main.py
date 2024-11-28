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

conversation_history = []

@app.post("/chat/")
async def chat(request: ChatRequest):
    global conversation_history
    conversation_history.append({"role": "user", "content": request.prompt})
    
    try:
        # Solicitud a la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Cambia a "gpt-4" si tienes acceso
            messages=conversation_history,
            max_tokens=150,
            temperature=0.7
        )

        # Extraer la respuesta del modelo
        model_response = response.choices[0].message["content"]
        
        # Añadir respuesta a la historia de la conversación
        conversation_history.append({"role": "assistant", "content": model_response})
        
        # Retornar la respuesta
        return {"response": model_response}
    
    except Exception as e:
        # En caso de error, mostrar más detalles
        return {"response": f"Error en la respuesta: {str(e)}"}

