import polars as pl

df = pl.read_csv("titanic.csv")

df_clean = (
    df.drop_nulls("Age")
      .filter(pl.col("Fare") > 100)
)

# 1. Write to Parquet
df_clean.write_parquet("cleaned.parquet")
print("Wrote cleaned.parquet")

# 2. Read back from Parquet
df_new = pl.read_parquet("cleaned.parquet")

print("Reloaded rows:", df_new.height)
print("=== Reloaded head ===")
print(df_new.head())
