import os
import openai
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Cargar las variables de entorno desde el archivo '.env'
load_dotenv(dotenv_path="app/.env")

# Asignar la clave API desde el archivo .env
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

conversation_history = [
    {"role": "system", "content": "Eres un asistente de servicio al cliente de Sergio Tech, una compañía que proporciona servicios de análisis de datos y desarrollo de modelos de machine learning para startups."}
]

@app.post("/chat/")
async def chat(request: ChatRequest):
    global conversation_history
    conversation_history.append({"role": "user", "content": request.prompt})
    
    try:
        # Solicitar la respuesta a la API de OpenAI con el modelo actualizado
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usar el modelo actualizado
            messages=conversation_history,
            max_tokens=150,
            temperature=0.7
        )
        
        # Extraer la respuesta del modelo
        model_response = response.choices[0].message["content"]
        
        # Añadir la respuesta a la historia de la conversación
        conversation_history.append({"role": "assistant", "content": model_response})
        
        # Retornar la respuesta
        return {"response": model_response}
    
    except Exception as e:
        # En caso de error, mostrar detalles
        return {"response": f"Error en la respuesta: {str(e)}"}


