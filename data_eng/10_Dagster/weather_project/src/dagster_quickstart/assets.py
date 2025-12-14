from dagster import asset, MaterializeResult
import pandas as pd

from .utils.create_tables import create_tables
from .utils.weather_utils import fetch_current_weather
from .utils.daily_weather import aggregated_daily_weather
from .utils.global_weather import aggregated_global_weather

# Asset 1 — Setup Database
@asset
def setup_database():
    create_tables()

    return MaterializeResult(
        metadata={
            "status": "SQLite tables created",
            "db": "data.db"
        }
    )


# Asset 2 — Fetch Hourly Weather Data
@asset(deps=[setup_database])
def fetch_weather():
    city = "Delhi"
    date = "2024-12-01"

    fetch_current_weather(city, date)

    return MaterializeResult(
        metadata={
            "city": city,
            "date": date,
            "source": "weatherapi.com"
        }
    )


# Asset 3 — Daily Aggregation 
@asset(deps=[fetch_weather])
def fetch_daily_weather():
    aggregated_daily_weather()

    preview = pd.DataFrame(
        {
            "aggregation": ["hourly → daily"],
            "table": ["daily_weather"]
        }
    )

    return MaterializeResult(
        metadata={
            "preview": preview.to_markdown()
        }
    )

# Asset 4 — Global Aggregation
@asset(deps=[fetch_daily_weather])
def global_weather():
    aggregated_global_weather()

    return MaterializeResult(
        metadata={
            "aggregation": "daily → global",
            "table": "global_weather"
        }
    )
