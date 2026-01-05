# producer/data_models.py
from dataclasses import dataclass

@dataclass
class WeatherData:
    timestamp: str
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    description: str
    wind_speed: float
    wind_direction: float
    cloudiness: int
    visibility: int
    latitude: float
    longitude: float
