import polars as pl
df = pl.read_csv("titanic.csv")
print(df.head())
print(df.schema)
print(df.shape)