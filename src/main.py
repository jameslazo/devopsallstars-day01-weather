import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

# Thank you @ShaeInTheCloud for this beautiful code :D
def api_call(city):
    """Fetch weather data from OpenWeather API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

print(api_call('Phoenix').json())