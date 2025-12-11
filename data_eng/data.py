import polars as pl

# 1. Load the Dataset
df = pl.read_csv("titanic.csv")
print("Original shape (rows, cols):", df.shape)

# 2. Remove Messy Data: drop nulls in Age, Fare, Embarked
df_clean = df.drop_nulls(["Age", "Fare", "Embarked"])
print("After drop_nulls values on Age, Fare, Embarked:", df_clean.shape)

# 3. Create Age_Group column
df_clean = df_clean.with_columns(
    pl.when(pl.col("Age") < 18)
      .then(pl.lit("Child"))
      .when((pl.col("Age") >= 18) & (pl.col("Age") <= 60))
      .then(pl.lit("Adult"))
      .otherwise(pl.lit("Senior"))
      .alias("Age_Group")
)
print("Add New age group shape (rows, cols):", df_clean.shape)

# 4. Filter Outliers: remove rows where Fare <= 0
df_clean = df_clean.filter(pl.col("Fare") > 0)
print("After removing non-positive Fare:", df_clean.shape)

# # 5. Sort by Fare (descending)
df_clean_sorted = df_clean.sort("Fare", descending=True)
print("\n=== Top 5 passengers by Fare ===")
print(df_clean_sorted.select(["Name", "Pclass", "Fare", "Age", "Age_Group"]).head())

# 6. Save as Parquet
output_file = "titanic_cleaned.parquet"
df_clean_sorted.write_parquet(output_file)
print(f"\nSaved cleaned dataset to {output_file}")
