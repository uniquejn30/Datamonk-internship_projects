import json
import time
import requests
from datetime import datetime
from kafka import KafkaProducer
from dotenv import load_dotenv
from pathlib import Path
import os
from .data_models import WeatherData

# Load environment variables
env_path = Path("config") / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY")
TOPIC = os.getenv("KAFKA_TOPIC")
BROKER = os.getenv("KAFKA_BROKER")

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers=BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def get_weather_data():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Handle invalid API response
        if data.get("cod") != 200:
            print("Weather API Error:", data.get("message"))
            return None

        # Build Weather Data payload safely
        weather = WeatherData(
            timestamp=str(datetime.utcnow()),
            city=data.get("name", "Unknown"),
            country=data["sys"].get("country", ""),
            temperature=data["main"].get("temp", 0),
            feels_like=data["main"].get("feels_like", 0),
            humidity=data["main"].get("humidity", 0),
            pressure=data["main"].get("pressure", 0),
            description=data["weather"][0].get("description", ""),
            wind_speed=data["wind"].get("speed", 0),
            wind_direction=data["wind"].get("deg", 0),
            cloudiness=data["clouds"].get("all", 0),
            visibility=data.get("visibility", 0),
            latitude=data["coord"].get("lat", 0),
            longitude=data["coord"].get("lon", 0)
        )

        return weather.__dict__

    except Exception as e:
        print("Exception in get_weather_data:", str(e))
        return None

def start_weather_producer():
    print(f"Weather Producer Started... Fetching: {CITY}")

    while True:
        weather_data = get_weather_data()

        if weather_data:
            try:
                producer.send(TOPIC, value=weather_data)
                print("Sent:", weather_data)
            except Exception as e:
                print("Error sending message to Kafka:", str(e))
        else:
            print("Skipping sending due to API or parsing issue")

        time.sleep(120)  # Wait 2 minutes before next API call
