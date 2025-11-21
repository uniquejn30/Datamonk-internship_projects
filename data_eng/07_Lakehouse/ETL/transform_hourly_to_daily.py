# etl/transform_hourly_to_daily.py
import polars as pl
from deltalake.writer import write_deltalake
import os

SRC = "data/hourly_weather.csv"
DELTA_PATH = "/tmp/delta_weather_daily"   # change to your repo path if you want to commit it

os.makedirs(DELTA_PATH, exist_ok=True)

# 1) Load
df = pl.read_csv(SRC)

# 2) Ensure time column parsed to datetime and create 'day' date
df = df.with_columns([
    pl.col("time").cast(pl.Utf8),
    pl.col("time").str.strptime(pl.Datetime, "%Y-%m-%d %H:%M").alias("timestamp")
]).with_columns([
    pl.col("timestamp").dt.date().alias("day")
])

# 3) Aggregate hourly -> daily per location
df_daily = (
    df
    .group_by(["location_name", "day"])
    .agg([
        pl.col("temperature").mean().round(2).alias("avg_temp"),
        pl.col("humidity").mean().round(2).alias("avg_humidity"),
        pl.len().alias("hours_count"),
        pl.col("weather_desc").first().alias("sample_desc")
    ])
).sort(["location_name","day"])

# 4) Persist to delta (initial write -> overwrite)
# write_deltalake accepts pandas or pyarrow tables. Convert to pandas.
write_deltalake(
    DELTA_PATH,
    df_daily.to_pandas(),
    mode="overwrite",
    partition_by=["location_name"]   # recommended partition for fast city-level queries
)

print("Successfully daily delta table to", DELTA_PATH)
