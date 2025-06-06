from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        if not city:
            dispatcher.utter_message(text="Please specify a city.")
            return []

        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                temp = data["main"]["temp"]
                condition = data["weather"][0]["description"]
                dispatcher.utter_message(text=f"The weather in {city} is {condition} with a temperature of {temp}°C.")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't fetch the weather for {city}. Please check the city name.")
        except Exception:
            dispatcher.utter_message(text="Something went wrong while fetching the weather.")
        
        return []