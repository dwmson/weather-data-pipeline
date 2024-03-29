# Weather Data Pipeline

## Project Overview
This project serves as an Extract-Transform-Load (ETL) data pipeline, designed to streamline the process of extracting near real-time weather data from an external API, transforming this data by filtering out unwanted information, and loading the refined data into a structured database for efficient storage and retrieval. This ETL pipeline focuses on optimizing data transfer, transformation, and storage, ensuring that the data is not only moved swiftly but is also stored in a format that enhances data quality and utility.

### How It Works
* **Extract:** The first step involves connecting to the OpenWeatherMap API, where the pipeline extracts current weather data. This data includes various weather metrics such as temperature, humidity, wind speed, and other relevant atmospheric conditions.
*  **Transform:** Once the data is extracted, it undergoes a transformation process where unnecessary or irrelevant data is filtered out. This step is crucial for refining the data, ensuring that only relevant and valuable information is retained for analysis. 
* **Load:** After extraction, the data is immediately loaded into a pre-defined PostgreSQL database schema. This process is designed to be efficient and reliable, ensuring that the weather data is available for querying and analysis with minimal latency. The loading step completes the ETL pipeline, making the data accessible for further use in applications, reporting, or analytics.

## Features
* Fetches near real-time weather data for the coordinates location
* Stores weather information in a PostgreSQL database for historical recording and analysis
* Modular structure for easy extension or customization

## Logging
This project uses Python's built-in `logging` module to provide near real-time insight into its operation. Logging captures important events, such as errors, warnings, and informational messages, which are invaluable for troubleshooting and monitoring the application's behavior. 

### Log File Configuration
The default logging level is set to `INFO`, capturing all operational messages, warnings, and errors. Log entries follow the format: `%(asctime)s - %(levelname)s - %(message)s`, including the timestamp, log level, and message.

To customize logging settings, modify the `logging.basicConfig` call in `weather_main.py`.

### Log File Samples
For practical examples of logging in action, please refer to the `Weather_API_Pipeline.log` file located in the `logs` directory of this project. This log file illustrates entries at the `INFO` level, detailing successful operations such as API data retrieval and database insertions. Additionally, it includes instances of deliberately induced `ERROR` messages, demonstrating the logging of issues encountered during both the API fetch process and database operations.

## Prerequisites 
* Python 3.x
* `requests` library for making API requests (pip install requests)
* `psycopg2` library for integration with PostgreSQL databases (pip install psycopg2)
* `python-decouple` library for separation of parameters
* `logging` library for logging API and database operations
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
