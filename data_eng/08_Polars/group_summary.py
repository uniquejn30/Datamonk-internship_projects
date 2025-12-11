import polars as pl

df = pl.read_csv("titanic.csv")

grouped = (
    df.group_by("Pclass")
      .agg(
          pl.col("Fare").mean().alias("avg_fare"),
      )
      .sort("Pclass")
)

print("=== Average Fare by Pclass ===")
print(grouped)
