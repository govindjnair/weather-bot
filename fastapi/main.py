from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="Weather Bot API")

# Enable CORS to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"Welcome to weather-bot"}

# Endpoint to handle chat messages
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    sender_id = data.get("sender_id", "user")

    # Send message to Rasa
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"sender": sender_id, "message": user_message}
    try:
        response = requests.post(rasa_url, json=payload)
        if response.status_code == 200:
            return {"response": {"responses": response.json()}}
        else:
            return {"error": {"Failed to get response from Rasa. Status code": response.status_code}}
    except Exception as e:
        return {"error": f"Error communicating with Rasa: {str(e)}"}

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok"}