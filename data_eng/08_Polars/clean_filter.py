import polars as pl

df = pl.read_csv("titanic.csv")

# 1. Drop rows where Age is null
# 2. Filter to keep rows where Fare > 100
df_clean = (
    df.drop_nulls("Age")
      .filter(pl.col("Fare") > 100)
)

print("Original rows:", df.height)
print("Cleaned rows:", df_clean.height)

print("\n=== Cleaned sample ===")
print(df_clean.head())
