import polars as pl

df = pl.read_csv("events.csv")

print("=== Raw data types ===")
print(df.schema)

df_dt = df.with_columns(
    pl.col("timestamp").str.strptime(pl.Datetime, format="%Y-%m-%d %H:%M:%S")
)

print("\n=== Converted schema ===")
print(df_dt.schema)

print("\n=== Data with datetime ===")
print(df_dt)
