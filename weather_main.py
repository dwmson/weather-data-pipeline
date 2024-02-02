import logging
from weather_api import get_weather_data
from weather_db_ops import insert_weather_data

logging.basicConfig(filename='./logs/Weather_API_Pipeline.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    weather = get_weather_data()
    insert_weather_data(weather)

if __name__ == "__main__":
    main()
