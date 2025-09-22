'''
1. main.py – The Orchestrator
This will be your main driver script. It will reads your list of cities, initializes the database, and controls the ETL flow by the functions. So, create functions that will call different scripts to perform differernt operations.

What happens here:

--> Calls create_table() to set up your database
--> Loads the list of cities from india_cities.csv by just itreating over the city column in the csv file you can pass the city name for your further process. (download the csv file from here ~~ indian_cities.csv)

For each city, it:

--> Extracts hourly weather (weather_utils.py)
--> Transforms it into a daily summary (daily_weather.py)
--> Transforms it further into long-term city stats (global_weather.py)

These steps are functions in your script that calls another function in different file and you have to call them in sequence. Segregate the files and import them in here for modularisation.

This is your workflow engine, done in plain Python.

What You Learn Here:

--> How to use helper modules
--> How to handle CLI arguments (sys.argv)
--> The basics of data orchestration

'''

# main.py
import csv
import sys
import datetime
from create_tables import create_tables
from weather_utils import fetch_current_weather
from daily_weather import aggregated_daily_weather
from global_weather import aggregated_global_weather

def run_etl(date):
    # Step 1: Setup DB
    create_tables()

    # Step 2: Load cities
    with open("india_cities.csv", "r") as f:
        reader = csv.DictReader(f)
        cities = [row["city"] for row in reader]

    # Step 3: Extract + Load hourly
    for city in cities:
        print(f"🌤 Fetching weather for {city} ({date})")
        fetch_current_weather(city, date)

    # Step 4: Transform to daily
    print("Aggregating daily data...")
    aggregated_daily_weather()

    # Step 5: Transform to global
    print("Aggregating global city averages...")
    aggregated_global_weather()

    print("ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    run_etl(date)
