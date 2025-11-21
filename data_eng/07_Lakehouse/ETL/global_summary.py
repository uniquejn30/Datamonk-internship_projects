import polars as pl

DELTA_PATH = "/tmp/delta_weather_daily"

df = pl.read_delta(DELTA_PATH)

df_global = (
    df
    .group_by("location_name")
    .agg([
        pl.col("avg_temp").mean().round(2).alias("global_avg_temp"),
        pl.col("avg_humidity").mean().round(2).alias("global_avg_humidity"),
        pl.count().alias("days_observed")
    ])
    .sort("location_name")
)

print(df_global)
