# main_wf.py
# This file defines Flyte tasks and the workflow (orchestrator)
import os
import typing
import flytekit as fl
from dotenv import load_dotenv

# Load environment variables (.env)
load_dotenv()

# Import business logic from utils/
from utils.create_tables import create_tables
from utils.weather_utils import fetch_current_weather
from utils.daily_weather import aggregated_daily_weather
from utils.global_weather import aggregated_global_weather

# ---------------------------------------------------------------------
# ImageSpec: Defines the container environment Flyte will use
# ---------------------------------------------------------------------
image_spec = fl.ImageSpec(
    name="weather-pipeline",
    requirements="uv.lock",
    registry=os.environ["FLYTE_IMAGE_REGISTRY"],
)
# image_spec = fl.ImageSpec(
#     name="weather-pipeline",
#     packages=[
#         "requests",
#         "python-dotenv"
#     ],
#     python_version="3.11"
# )



# ---------------------------------------------------------------------
# Flyte Tasks (NO image_spec)
# ---------------------------------------------------------------------

@fl.task
def setup_database():
    """
    Creates required SQLite tables:
    - weather
    - daily_weather
    - global_weather
    """
    create_tables()


@fl.task
def fetch_weather(city: str, date: str):
    """
    Fetches hourly weather data for a city and date
    and stores it into the weather table
    """
    fetch_current_weather(city, date)


@fl.task
def fetch_daily_weather():
    """
    Aggregates hourly weather data into daily summaries
    """
    aggregated_daily_weather()


@fl.task
def fetch_global_weather():
    """
    Aggregates daily data into global (city-level) averages
    """
    aggregated_global_weather()


# ---------------------------------------------------------------------
# Flyte Workflow (Orchestrator)
# ---------------------------------------------------------------------

@fl.workflow
def wf(city: str = "Noida", date: str = "2025-01-17") -> typing.Tuple[str, int]:
    setup_database()
    fetch_weather(city, date)
    fetch_daily_weather()
    fetch_global_weather()
    return "SUCCESS", 200


# ---------------------------------------------------------------------
# Local execution entry point
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print(wf())
