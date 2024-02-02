import requests 
import datetime
from decouple import config
import logging

class WeatherData:
    def __init__(self, data):
        self.api_timestamp = datetime.datetime.fromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        self.city = data["name"]
        self.country = data["sys"]["country"]
        self.conditions = data["weather"][0]["description"]
        self.temp = data["main"]["temp"]
        self.temp_min = data["main"]["temp_min"]
        self.temp_max = data["main"]["temp_max"]
        self.humidity = data["main"]["humidity"]
        self.wind_speed = data["wind"]["speed"]
        self.sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S')
        self.sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S')


def get_weather_data():
    api_key = config('API_KEY')
    lat = config('LATITUDE')
    long = config('LONGITUDE')
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=imperial'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info('API OK: Weather data fetched successfully')
        return WeatherData(data)
    except requests.RequestException as e:
        print(f'Error fetching weather data: {e}')
        logging.error(f'API ERROR: Failed to fetch weather data: {e}')
        return None 

## Test this script ##
    
# if __name__ == "__main__":
#     weather_data = get_weather_data()
#     if weather_data:
#         print("Weather Data Fetched Successfully:")
#         print(f"City: {weather_data.city}")
#         print(f"Temperature: {weather_data.temp}°F")
#     else:
#         print("Failed to fetch weather data.")



