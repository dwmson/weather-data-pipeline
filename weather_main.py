from weather_api import get_weather_data
from weather_db_ops import insert_weather_data

def main():
    weather = get_weather_data()
    insert_weather_data(weather)

if __name__ == "__main__":
    main()
