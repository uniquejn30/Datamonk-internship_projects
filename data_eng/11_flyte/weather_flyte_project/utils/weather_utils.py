# # weather_utils.py – The Extractor
# # Here we implement the Extract step of ETL. This script connects to WeatherAPI to fetch hourly weather data for a given city and date.

# # What it handles:

# # Validating the date (no future dates!)
# # Building the API request
# # Reading API keys from .env (make one for yourself on the weatherapi website given above, and add that into .env file)
# # Filtering “future” hourly records for specific date
# # Passing data to insert_weather_data() for storage
# # weather_utils.py

# import requests
# import os
# import datetime
# from dotenv import load_dotenv
# from .hourly_weather import insert_hourly_weather

# load_dotenv()
# API_KEY = os.getenv("WEATHER_API_KEY")

# def fetch_current_weather(city, date, db_name="data.db"):
#     if not API_KEY:
#         raise ValueError("⚠️ API Key missing in .env file")

#     # Prevent future dates
#     today = datetime.date.today()
#     req_date = datetime.date.fromisoformat(date)
#     if req_date > today:
#         raise ValueError("⚠️ Cannot fetch future weather data")

#     url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={city}&dt={date}"
#     response = requests.get(url)
#     data = response.json()

#     if "error" in data:
#         print(f"⚠️ Error for {city}: {data['error']['message']}")
#         return

#     # Get hourly weather data
#     for hour in data["forecast"]["forecastday"][0]["hour"]:
#         record = {
#             "date": date,
#             "time": hour["time"].split(" ")[1],
#             "temperature": hour["temp_c"],
#             "condition": hour["condition"]["text"],
#             "humidity": hour["humidity"],
#             "location_name": data["location"]["name"],
#             "region": data["location"]["region"],
#             "country": data["location"]["country"],
#             "latitude": data["location"]["lat"],
#             "longitude": data["location"]["lon"],
#             "local_time": data["location"]["localtime"]
#         }
#         insert_hourly_weather(record, db_name)
# # print("Hello World from weather_utils.py")


# utils/weather_utils.py

import requests
import os
from dotenv import load_dotenv
from .hourly_weather import insert_hourly_weather

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


def fetch_current_weather(city, date=None, db_name="data.db"):
    if not API_KEY:
        raise ValueError("API Key missing in .env file")

    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={city}"
    )

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print(f"⚠️ Error for {city}: {data['error']['message']}")
        return

    current = data["current"]
    location = data["location"]

    record = {
        "date": location["localtime"].split(" ")[0],
        "time": location["localtime"].split(" ")[1],
        "temperature": current["temp_c"],
        "condition": current["condition"]["text"],
        "humidity": current["humidity"],
        "location_name": location["name"],
        "region": location["region"],
        "country": location["country"],
        "latitude": location["lat"],
        "longitude": location["lon"],
        "local_time": location["localtime"],
    }

    insert_hourly_weather(record, db_name)
