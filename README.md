# Weather Database Project

## Overview
This project fetches current weather data from specified latitude and longitude coordinates using the OpenWeatherMap API and stores the data in a PostgreSQL database. It offers a straightforward way to collect and store weather information for various applications, and it can be configured to run automatically using a cron job.

## Features
* Fetches real-time weather data for the coordinates location
* Stores weather information in a PostgreSQL database for historical recording and analysis
* Modular structure for easy extension or customization

## Prerequisites 
* Python 3.x
* `requests` library for making API requests (pip install requests)
* `psycopg2` library for integration with PostgreSQL databases (pip install psycopg2)
* `python-decouple` library for separation of parameters
* Sign up for an API key from [OpenWeatherMap](https://openweathermap.org)
* Install and configure a [PostgreSQL](https://www.postgresql.org) environment and a database management tool

## Configuration
Replace the API key, latitude, longitude, database credentials, and database table name values with your own or create a config file with these settings for a more organized configuration management

## Usage
* Clone this repository to your local machine via HTTPS:
```bash
https://github.com/dwmson/weather-database-project.git
```
Or via GitHub CLI:
```bash
gh repo clone dwmson/weather-database-project
```
* Navigate to the project directory
```bash
cd weather-database-project
```
* Run the main python file
```bash
python3 weather_main.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to OpenWeatherMap for providing weather data.
- A hat-tip to the Python and PostgreSQL communities for their valuable tools and resources.
