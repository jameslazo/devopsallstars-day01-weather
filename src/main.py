import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime as dt, UTC

load_dotenv()

api_key = os.getenv('API_KEY')
save_directory = './weather_data'

# Thank you @ShaeInTheCloud for this beautiful code :D | https://github.com/ShaeInTheCloud/30days-weather-dashboard/blob/main/src/weather_dashboard.py
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


# Save weather data to a local directory
def save_to_local_directory(weather_data, city):    
    if not weather_data:
        return False

    timestamp = dt.now(UTC).strftime('%Y%m%d-%H%M%S')
    file_name = f"{save_directory}/{city}-{timestamp}.json"
    
    try:
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        weather_data['timestamp'] = timestamp
        with open(file_name, 'w') as f:
            json.dump(weather_data, f)
        print(f"Successfully saved data for {city} to {file_name}")
        return True
    
    except Exception as e:
        print(f"Error saving to directory: {e}")
        return False


# Do the thing
def main():    
    cities = ["Phoenix", "New York", "Tokyo"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = api_call(city).json()
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
        
            success = save_to_local_directory(weather_data, city)
            if success:
                print(f"Weather data for {city} saved locally!")

        else:
            print(f"Failed to fetch weather data for {city}")

if __name__ == "__main__":
    main()

