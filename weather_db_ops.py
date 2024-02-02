import psycopg2
import logging
from decouple import config

db_params = {
    'dbname': config('DB_NAME'),
    'user': config('DB_USER'),
    'password': config('DB_PASSWORD'),
    'host': config('DB_HOST')
}

table_name = config('TABLE_NAME')

def connect_to_db():
    conn = psycopg2.connect(**db_params)
    return conn

def insert_weather_data(weather):
    conn = connect_to_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = f"INSERT INTO {table_name} (api_timestamp, city, country, conditions, temp, temp_min, temp_max, humidity, wind_speed, sunrise_timestamp, sunset_timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(query, (weather.api_timestamp, weather.city, weather.country, weather.conditions, weather.temp, weather.temp_min, weather.temp_max, weather.humidity, weather.wind_speed, weather.sunrise_timestamp, weather.sunset_timestamp))

            conn.commit()
            logging.info("DATABASE OK: Weather data successfully inserted into database")
            cursor.close()
        except psycopg2.Error as e:
            print(f'Error executing SQL query: {e}')
            logging.error(f"DATABASE ERROR: Failed to insert data into database: {e}")
        finally:
            conn.close()
    else:
        print('Unable to connect to database')

