import polars as pl

DELTA_PATH = "/tmp/delta_weather_daily"

# Latest
print("=== Latest ===")
print(pl.read_delta(DELTA_PATH))

# Specific version (0 = initial write)
print("\n=== Version 0 ===")
print(pl.read_delta(DELTA_PATH, version=0))

# Filter example (partition pruning benefits)
print("\n=== Mumbai only ===")
print(pl.read_delta(DELTA_PATH).filter(pl.col("location_name") == "Mumbai"))
