# Weather Bot

A simple chatbot for checking city weather, built with Rasa, FastAPI, and a JavaScript frontend.

**Tech Stack**: Python 3.10, Rasa 3.6.10, FastAPI, HTML/CSS/JavaScript

## Setup

1. Create two virtual environments:
   - **Rasa environment**: For running Rasa server and actions.
   - **FastAPI environment**: For running the FastAPI server.

2. Install dependencies in each environment:
   - Rasa environment:
     ```bash
     pip install rasa
     ```
   - FastAPI environment:
     ```bash
     cd fastapi
     pip install -r requirements.txt
     ```

3. Set up OpenWeatherMap API key:
   - Create a `.env` file in the project root:
     ```
     OPENWEATHER_API_KEY=your_api_key
     ```
   - Replace `your_api_key` with your OpenWeatherMap API key.

4. Train the Rasa model:
   - Activate Rasa environment and run:
     ```bash
     cd rasa
     rasa train
     ```

5. Start the servers:
   - Rasa server (port 5005):
     ```bash
     cd rasa
     rasa run --enable-api --cors "*"
     ```
   - Rasa actions server (port 5055):
     ```bash
     cd rasa
     rasa run actions
     ```
   - FastAPI server (port 8000):
     ```bash
     cd fastapi
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```
   - Frontend server (port 8080):
     ```bash
     cd frontend
     python3 -m http.server 8080
     ```

6. Open `http://localhost:8080` in a browser for the chatbot and try messages like `hi`, ask the weather, any city name, or `bye`.