# etl/append_new_day.py
import polars as pl
from deltalake.writer import write_deltalake
import pandas as pd
import os

DELTA_PATH = "/tmp/delta_weather_daily"

# New simulated day (could be derived from hourly -> daily logic)
df_new = pd.DataFrame({
    "location_name": ["Mumbai", "Delhi"],
    "day": ["2025-05-19", "2025-05-19"],
    "avg_temp": [33.1, 29.4],
    "avg_humidity": [70.2, 60.8],
    "hours_count": [24, 24],
    "sample_desc": ["Sunny", "Cloudy"]
})

write_deltalake(DELTA_PATH, df_new, mode="append")
print("Appended new rows to", DELTA_PATH)
