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

def main():    
    cities = ["Phoenix", "New York", "Tokyo"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = api_call(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
            
        else:
            print(f"Failed to fetch weather data for {city}")

if __name__ == "__main__":
    main()

