from deltalake.writer import write_deltalake
import pandas as pd

DELTA_PATH = "/tmp/delta_weather_daily"

df = pd.DataFrame({
    "location_name": ["Mumbai"],
    "day": ["2025-05-20"],
    "avg_temp": [32.5],
    "avg_humidity": [68.1],
    "hours_count": [24],
    "sample_desc": ["Rain"],
    "precip_mm": [12.6]          # NEW COLUMN
})

write_deltalake(
    DELTA_PATH,
    df,
    mode="append",
    schema_mode="merge"          # IMPORTANT
)

print("Appended new rows with schema evolution enabled.")
